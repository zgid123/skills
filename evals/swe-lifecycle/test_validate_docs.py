"""Behavior tests with isolated project fixtures; no remote services are used."""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[2] / "skills" / "swe-lifecycle" / "scripts" / "validate_docs.py"
SPEC = importlib.util.spec_from_file_location("swe_validate_docs", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)

BODY = {
    "REQ": "# Capability\n\n## Overview\nControl access to the gateway.\n\n## Functional requirements\nFR-001: Enforce the configured policy.\n\n## Acceptance criteria\nAC-001: Requests exceeding the configured limit return HTTP 429.\n",
    "CHG": "# Policy evolution\n\n## Summary\nReplace the policy evaluator.\n\n## Current behavior\nThe fixture uses role checks.\n\n## Proposed behavior\nEvaluate approved attributes as well.\n\n## Acceptance criteria\nPolicy evaluation preserves denial by default.\n",
    "ADR": "# Decision\n\n## Context\nThe gateway needs a consistent policy boundary.\n\n## Decision\nUse a dedicated evaluator.\n\n## Consequences\nCallers delegate policy evaluation to that boundary.\n",
    "KNW": "# Current capability\n\n## Overview\nGateway policy enforcement.\n\n## Current implementation\nThe fixture's middleware evaluates policy before routing.\n\n## Known limitations\nDistributed counters are outside this fixture.\n",
    "LOG": "# Implementation record\n\n## Summary\nIntroduce fixture policy enforcement.\n\n## Previous behavior\nNo limiter existed in the fixture.\n\n## New behavior\nThe middleware checks the configured limit.\n\n## Tests and verification\nFixture-only example; no production tests claimed.\n\n## Documentation updated\nCurrent capability knowledge was added.\n",
}


def document(kind, identifier, **overrides):
    """Small explicit public-schema fixture factory, independent of validator constants."""
    fields = {
        "id": identifier, "title": "Fixture capability", "owner": "maintainer",
        "status": {"REQ": "approved", "CHG": "proposed", "ADR": "accepted", "KNW": "verified", "LOG": "finalized"}[kind],
    }
    if kind == "LOG":
        fields.update(date="2026-10-23", type="feature", commit=None,
                      requirements=[], changes=[], decisions=[], github_issues=[], github_prs=[], components=[])
    else:
        fields.update(created_at="2026-10-22", updated_at="2026-10-23")
    fields.update({
        "REQ": {"dependencies": [], "related_changes": []},
        "CHG": {"related_requirements": []},
        "ADR": {"supersedes": [], "superseded_by": []},
        "KNW": {"requirements": [], "decisions": [], "components": []},
        "LOG": {},
    }[kind])
    fields.update(overrides)
    frontmatter = "\n".join(f"{key}: {json.dumps(value)}" for key, value in fields.items())
    return f"---\n{frontmatter}\n---\n\n{BODY[kind]}"


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        self.root.mkdir()
        self.write("README.md", "# Documentation\n\n[Project](project.md)\n")
        self.write("project.md", "---\nowner: \"Gateway team\"\nchangelog_policy: meaningful\nreserved_ids: []\n---\n\n# API Gateway\n\nA disposable fixture project.\n")

    def write(self, relative_path, content):
        path = self.root / "docs" / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def assert_valid(self):
        self.assertEqual(VALIDATOR.validate(self.root), [])

    def assert_invalid(self, *fragments):
        errors = VALIDATOR.validate(self.root)
        self.assertTrue(errors, "Invalid fixture was accepted")
        output = "\n".join(errors).lower()
        for fragment in fragments:
            self.assertIn(fragment.lower(), output)

    def requirement(self, number="00001", **fields):
        return self.write(f"specs/requirements/{number}-capability.md", document("REQ", f"REQ-{number}", **fields))

    def test_designed_feature_with_current_knowledge_and_history(self):
        requirement = self.requirement()
        design = self.write("architecture/rate-limiting-design.md", "# Rate limiting design\n\n[Requirement](../specs/requirements/00001-capability.md)\n")
        requirement.write_text(requirement.read_text() + "\n[Design](../../architecture/rate-limiting-design.md)\n")
        self.write("knowledge/rate-limiting.md", document("KNW", "KNW-rate-limiting", requirements=["REQ-00001"], components=["src/rate-limiter.py"]))
        self.write("changelog/00001-capability/0001-initial.md", document("LOG", "LOG-00001-0001", requirements=["REQ-00001"]))
        self.assertTrue(design.is_file())
        self.assert_valid()
        self.assertFalse((self.root / "docs/specs/changes").exists())

    def test_migration_reuses_requirement_and_preserves_adr_supersession(self):
        self.requirement(related_changes=["CHG-00001"])
        self.write("specs/changes/00001-migrate-auth/proposal.md", document("CHG", "CHG-00001", related_requirements=["REQ-00001"]))
        self.write("specs/changes/00001-migrate-auth/design.md", "# Migration design\n\n[Proposal](proposal.md)\n")
        self.write("decisions/00001-original-auth.md", document("ADR", "ADR-00001", status="superseded", superseded_by=["ADR-00002"]))
        self.write("decisions/00002-service-auth.md", document("ADR", "ADR-00002", supersedes=["ADR-00001"]))
        self.write("knowledge/authentication.md", document("KNW", "KNW-authentication", requirements=["REQ-00001"], decisions=["ADR-00002"]))
        self.write("changelog/00001-capability/0002-migration.md", document("LOG", "LOG-00001-0002", type="migration", requirements=["REQ-00001"], changes=["CHG-00001"], decisions=["ADR-00002"]))
        self.assert_valid()
        self.assertEqual(len(list((self.root / "docs/specs/requirements").glob("*.md"))), 1)

    def test_proposed_replacement_links_predecessor_without_supersession_metadata(self):
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001"))
        proposed = document("ADR", "ADR-00002", status="proposed")
        proposed += "\n[Accepted predecessor](00001-policy.md)\n"
        self.write("decisions/00002-replacement.md", proposed)
        self.assert_valid()

    def test_proposed_replacement_cannot_apply_supersession_metadata_early(self):
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001"))
        self.write("decisions/00002-replacement.md", document("ADR", "ADR-00002", status="proposed", supersedes=["ADR-00001"]))
        self.assert_invalid("must reciprocate")

    def test_bug_record_needs_no_new_requirement_or_change(self):
        self.write("changelog/authentication/0001-race-fix.md", document("LOG", "LOG-authentication-0001", type="fix"))
        self.assert_valid()
        self.assertFalse((self.root / "docs/specs/requirements").exists())
        self.assertFalse((self.root / "docs/specs/changes").exists())

    def test_requirement_evolution_links_existing_capability(self):
        self.requirement(related_changes=["CHG-00002"])
        self.write("specs/changes/00002-introduce-abac/proposal.md", document("CHG", "CHG-00002", status="implemented", related_requirements=["REQ-00001"]))
        self.write("specs/changes/00002-introduce-abac/design.md", "# ABAC design\n\n[Proposal](proposal.md)\n")
        self.write("knowledge/authorization.md", document("KNW", "KNW-authorization", requirements=["REQ-00001"]))
        self.write("changelog/00001-capability/0003-abac.md", document("LOG", "LOG-00001-0003", requirements=["REQ-00001"], changes=["CHG-00002"]))
        self.assert_valid()

    def test_numbering_gaps_are_allowed(self):
        self.requirement("00001")
        self.requirement("00009")
        self.write("changelog/foundation/0007-tooling.md", document("LOG", "LOG-foundation-0007", type="chore"))
        self.assert_valid()

    def test_invalid_ids_are_rejected(self):
        for identifier in ("REQ-1", "REQ-00000", "REQ-auth", "CHG-00001"):
            with self.subTest(identifier=identifier):
                self.write("specs/requirements/00001-capability.md", document("REQ", identifier))
                self.assert_invalid("invalid REQ document ID", "00001-capability.md")

    def test_duplicate_metadata_key_is_rejected(self):
        self.write("specs/requirements/00001-capability.md", document("REQ", "REQ-00001").replace('"REQ-00001"\n', '"REQ-00001"\nid: REQ-00002\n', 1))
        self.assert_invalid("duplicate metadata key id")

    def test_duplicate_document_id_is_rejected(self):
        self.requirement()
        self.write("specs/requirements/00001-other.md", document("REQ", "REQ-00001"))
        self.assert_invalid("duplicate document ID", "REQ-00001")

    def test_missing_required_fields_and_status_are_rejected(self):
        for field in ("status", "owner", "dependencies", "created_at"):
            with self.subTest(field=field):
                content = "\n".join(line for line in document("REQ", "REQ-00001").splitlines() if not line.startswith(field + ":"))
                self.write("specs/requirements/00001-capability.md", content)
                self.assert_invalid("missing required metadata field " + field)

    def test_invalid_lifecycle_status_is_rejected(self):
        self.requirement(status="done")
        self.assert_invalid("lifecycle status")

    def test_missing_mandatory_section_is_rejected(self):
        self.write("specs/requirements/00001-capability.md", document("REQ", "REQ-00001").replace("## Acceptance criteria", "## Other notes"))
        self.assert_invalid("missing mandatory section", "Acceptance criteria")

    def test_empty_mandatory_section_is_rejected(self):
        content = document("REQ", "REQ-00001")
        content = content.replace("AC-001: Requests exceeding the configured limit return HTTP 429.", "<!-- Fill later -->")
        self.write("specs/requirements/00001-capability.md", content)
        self.assert_invalid("empty mandatory section", "Acceptance criteria")

    def test_headings_inside_html_comments_do_not_satisfy_required_sections(self):
        content = document("REQ", "REQ-00001")
        body_start = content.index("# Capability")
        self.write("specs/requirements/00001-capability.md", content[:body_start] + "<!--\n" + content[body_start:] + "\n-->\n")
        self.assert_invalid("missing mandatory section", "Overview", "Functional requirements", "Acceptance criteria")

    def test_empty_subheading_does_not_count_as_section_content(self):
        content = document("REQ", "REQ-00001").replace(
            "AC-001: Requests exceeding the configured limit return HTTP 429.", "### Later"
        )
        self.write("specs/requirements/00001-capability.md", content)
        self.assert_invalid("empty mandatory section", "Acceptance criteria")

    def test_inline_code_and_nonempty_fenced_example_count_as_section_content(self):
        inline = document("REQ", "REQ-00001").replace(
            "Control access to the gateway.", "`MAX_CONNECTIONS=1`"
        )
        self.write("specs/requirements/00001-capability.md", inline)
        self.assert_valid()
        fenced = inline.replace("AC-001: Requests exceeding the configured limit return HTTP 429.", "```text\nAC=429\n```")
        self.write("specs/requirements/00001-capability.md", fenced)
        self.assert_valid()

    def test_structured_knowledge_overview_is_validated(self):
        self.write("knowledge/authentication/README.md", document("KNW", "KNW-authentication-overview", requirements=["REQ-99999"]))
        self.assert_invalid("REQ-99999")

    def test_zero_changelog_namespace_is_rejected(self):
        self.write("changelog/00000/0001-invalid.md", document("LOG", "LOG-00000-0001"))
        self.assert_invalid("invalid LOG document ID")

    def test_invalid_optional_priority_is_rejected(self):
        self.requirement(priority="urgent-ish")
        self.assert_invalid("priority must be")

    def test_heading_inside_code_does_not_satisfy_required_section(self):
        content = document("REQ", "REQ-00001").replace("## Acceptance criteria", "```md\n## Acceptance criteria") + "\n```\n"
        self.write("specs/requirements/00001-capability.md", content)
        self.assert_invalid("missing mandatory section", "Acceptance criteria")

    def test_filename_must_match_stable_identifier(self):
        self.write("specs/requirements/00002-Wrong_Name.md", document("REQ", "REQ-00001"))
        self.assert_invalid("filename must match", "REQ")

    def test_dates_must_be_real_and_ordered(self):
        for fields, message in (({"created_at": "2026-02-30"}, "valid YYYY-MM-DD"), ({"updated_at": "yesterday"}, "valid YYYY-MM-DD"), ({"updated_at": "2026-10-01"}, "precedes")):
            with self.subTest(fields=fields):
                self.requirement(**fields)
                self.assert_invalid(message)

    def test_dangling_and_wrong_namespace_references_are_rejected(self):
        self.requirement(dependencies=["REQ-99999"], related_changes=["ADR-00001"])
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001"))
        self.assert_invalid("REQ-99999", "CHG reference", "ADR-00001")

    def test_reference_fields_require_lists(self):
        self.requirement(dependencies="REQ-00002")
        self.assert_invalid("dependencies must be a list")

    def test_indented_yaml_lists_and_quoted_scalars_are_accepted(self):
        self.requirement("00002")
        content = document("REQ", "REQ-00001", dependencies=["REQ-00002"], title="Policy: request admission")
        content = content.replace('dependencies: ["REQ-00002"]', "dependencies:\n  - REQ-00002")
        content = content.replace('owner: "maintainer"', "owner: 'gateway team'")
        self.write("specs/requirements/00001-capability.md", content)
        self.assert_valid()

    def test_dangling_supersession_is_rejected(self):
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001", status="superseded", superseded_by=["ADR-00002"]))
        self.assert_invalid("ADR-00002", "reference")

    def test_supersession_requires_reciprocal_relationship_and_status(self):
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001", superseded_by=["ADR-00002"]))
        self.write("decisions/00002-replacement.md", document("ADR", "ADR-00002"))
        self.assert_invalid("superseded status", "reciprocate")

    def test_supersession_cycle_is_rejected(self):
        for number, other in (("00001", "00002"), ("00002", "00001")):
            self.write(f"decisions/{number}-policy.md", document("ADR", f"ADR-{number}", status="superseded", supersedes=[f"ADR-{other}"], superseded_by=[f"ADR-{other}"]))
        self.assert_invalid("supersession cycle")

    def test_numbered_log_must_match_requirement_and_sequence(self):
        self.requirement()
        self.write("changelog/00001-capability/0002-fix.md", document("LOG", "LOG-00001-0001", type="fix"))
        self.assert_invalid("record sequence", "matching requirement")

    def test_reserved_identifiers_cannot_be_reused(self):
        self.write("project.md", "---\nreserved_ids: [\"REQ-00001\"]\n---\n\n# Project\n")
        self.requirement()
        self.assert_invalid("reserved ID REQ-00001", "reused")

    def test_change_directory_requires_a_proposal(self):
        self.write("specs/changes/00001-migration/design.md", "# Migration design\n")
        self.assert_invalid("requires proposal.md")

    def test_malformed_yaml_is_rejected_without_crashing(self):
        self.write("specs/requirements/00001-capability.md", "---\nid: [not valid\n---\n# Invalid\n")
        self.assert_invalid("00001-capability.md", "array")

    def test_wrong_scalar_field_types_are_rejected_without_crashing(self):
        for field in ("status", "title", "owner", "id", "created_at"):
            with self.subTest(field=field):
                self.write("specs/requirements/00001-capability.md", document("REQ", "REQ-00001", **{field: []}))
                self.assert_invalid("00001-capability.md", field)

    def test_invalid_log_type_is_rejected_without_crashing(self):
        self.write("changelog/foundation/0001-tooling.md", document("LOG", "LOG-foundation-0001", type=[]))
        self.assert_invalid("type")

    def test_invalid_project_policy_is_rejected_without_crashing(self):
        self.write("project.md", "---\nowner: \"Gateway team\"\nchangelog_policy: []\n---\n\n# Project\n")
        self.assert_invalid("changelog_policy")

    def test_project_requires_resolved_owner(self):
        invalid_frontmatter = (
            "---\nchangelog_policy: meaningful\nreserved_ids: []\n---\n",
            '---\nowner: ""\nchangelog_policy: meaningful\nreserved_ids: []\n---\n',
            "---\nowner: []\nchangelog_policy: meaningful\nreserved_ids: []\n---\n",
            '---\nowner: "<Person or accountable role>"\nchangelog_policy: meaningful\nreserved_ids: []\n---\n',
        )
        for frontmatter in invalid_frontmatter:
            with self.subTest(frontmatter=frontmatter):
                self.write("project.md", frontmatter + "\n# Project\n")
                self.assert_invalid("owner must be a nonempty resolved string")
        self.write("project.md", "---\nowner: \"Gateway team\"\nchangelog_policy: meaningful\nreserved_ids: []\n---\n\n# Project\n")
        self.assert_valid()

    def test_null_supersession_list_is_rejected_without_crashing(self):
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001", status="superseded", superseded_by=["ADR-00002"]))
        self.write("decisions/00002-replacement.md", document("ADR", "ADR-00002", supersedes=None))
        self.assert_invalid("supersedes", "list")

    def test_malformed_link_is_reported_without_crashing(self):
        self.write("README.md", "# Documentation\n\n[Malformed](http://[)\n")
        self.assert_invalid("README.md", "link")

    def test_links_cannot_escape_project_root(self):
        self.write("README.md", "# Documentation\n\n[Outside](../../outside.md)\n")
        self.assert_invalid("escapes project root")

    def test_bootstrap_needs_no_feature_specifications(self):
        self.write("architecture/README.md", "# Architecture\n\nHono gateway scaffold; behavior is not yet implemented.\n")
        self.write("guides/development.md", "# Development\n\nUse the repository's documented checks.\n")
        self.assert_valid()
        self.assertFalse((self.root / "docs/specs/requirements").exists())

    def test_unused_canonical_categories_need_not_exist(self):
        self.assert_valid()
        self.assertFalse((self.root / "docs/specs").exists())
        self.assertFalse((self.root / "docs/knowledge").exists())
        self.assertFalse((self.root / "docs/changelog").exists())

    def test_core_documentation_files_remain_required(self):
        (self.root / "docs/project.md").unlink()
        self.assert_invalid("project.md", "required document missing")

    def test_local_link_forms_are_checked(self):
        for link in (
            "[Missing](missing.md)",
            "![Diagram](images/missing.png)",
            "[Missing][target]\n\n[target]: missing.md",
            "[Missing heading](project.md#does-not-exist)",
            "[Missing heading](#does-not-exist)",
        ):
            with self.subTest(link=link):
                self.write("README.md", "# Documentation\n\n" + link + "\n")
                self.assert_invalid("README.md")

    def test_valid_local_links_and_external_links_are_accepted(self):
        self.write("diagram.svg", '<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.write("space name.md", "# Space Name\n")
        self.write("README.md", "# Documentation\n\n"
                   "[Project](project.md#api-gateway)\n"
                   "[Project reference][project]\n"
                   "![Diagram](diagram.svg)\n"
                   "[Space](space%20name.md)\n"
                   "[External](https://example.invalid/not-fetched)\n"
                   "[Mail](mailto:owner@example.invalid)\n"
                   "[Self](#documentation)\n\n"
                   "[project]: project.md#api-gateway\n")
        self.assert_valid()

    def test_requirement_and_decision_indexes_can_be_plain_or_structured(self):
        self.write("specs/requirements/README.md", "# Requirements\n\n[Gateway](00001-capability.md)\n")
        self.requirement()
        self.write("decisions/README.md", "# Decisions\n\n[Policy](00001-policy.md)\n")
        self.write("decisions/00001-policy.md", document("ADR", "ADR-00001"))
        self.assert_valid()
        structured = document("REQ", "REQ-00002")
        self.write("specs/requirements/README.md", structured)
        self.assert_valid()
        self.write("specs/requirements/README.md", "# Requirements\n\n[Missing](missing.md)\n")
        self.assert_invalid("broken local link", "README.md")

    def test_heading_anchor_preserves_inline_code_text(self):
        self.write("README.md", "# Documentation\n\n## Using `refresh()`\n\n## Using refresh()\n\n[First usage](#using-refresh)\n[Second usage](#using-refresh-1)\n")
        self.assert_valid()

    def test_minimal_docs_remain_valid_after_checkout_without_empty_directories(self):
        git_env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True, text=True, timeout=10, env=git_env)
        subprocess.run(["git", "-C", str(self.root), "add", "--all"], check=True, capture_output=True, text=True, timeout=10, env=git_env)
        subprocess.run(
            ["git", "-C", str(self.root), "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "-c", f"core.hooksPath={os.devnull}", "-c", "commit.gpgsign=false", "commit", "-qm", "bootstrap docs"],
            check=True, capture_output=True, text=True, timeout=10, env=git_env,
        )
        checkout = self.root.parent / "checkout"
        subprocess.run(["git", "clone", "--quiet", str(self.root), str(checkout)], check=True, capture_output=True, text=True, timeout=10, env=git_env)
        self.assertEqual(VALIDATOR.validate(checkout), [])

    def test_historical_source_path_is_not_a_current_link(self):
        self.write("changelog/foundation/0001-rename.md", document("LOG", "LOG-foundation-0001", type="refactor") +
                   "\nImplementation was previously in `src/old_module.py` (revision 91a2b3c).\n")
        self.assert_valid()

    def test_cli_uses_supplied_project_root_from_unrelated_directory(self):
        with tempfile.TemporaryDirectory() as unrelated:
            passed = subprocess.run(
                [sys.executable, str(SCRIPT), str(self.root)], cwd=unrelated,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(passed.returncode, 0, passed.stdout + passed.stderr)
            self.write("README.md", "# Documentation\n\n[Missing](missing.md)\n")
            failed = subprocess.run(
                [sys.executable, str(SCRIPT), str(self.root)], cwd=unrelated,
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn("README.md", failed.stdout + failed.stderr)


if __name__ == "__main__":
    unittest.main()
