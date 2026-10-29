"""Regression checks for repository documentation links; no network calls."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import validate_skills


class RepositoryLinkTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.skills = self.root / "skills"
        self.skills.mkdir()
        (self.root / "README.md").write_text("# Skills\n", encoding="utf-8")
        (self.root / "AGENTS.md").write_text("# Instructions\n", encoding="utf-8")
        for name, value in (("ROOT", self.root), ("SKILLS", self.skills)):
            patcher = patch.object(validate_skills, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_valid_root_links_are_accepted(self):
        (self.skills / "guide.md").write_text("# Guide\n", encoding="utf-8")
        (self.root / "README.md").write_text(
            "[Instructions](AGENTS.md)\n[Guide](skills/guide.md#guide)\n", encoding="utf-8"
        )
        (self.root / "AGENTS.md").write_text("[Catalog](README.md)\n", encoding="utf-8")
        self.assertEqual(validate_skills.validate(), [])

    def test_missing_root_link_reports_document_and_target(self):
        for document in ("README.md", "AGENTS.md"):
            with self.subTest(document=document):
                path = self.root / document
                path.write_text("[Results](skills/missing-workspace/README.md)\n", encoding="utf-8")
                self.assertEqual(
                    validate_skills.validate(),
                    [f"{path}: broken link skills/missing-workspace/README.md"],
                )
                path.write_text("# Restored\n", encoding="utf-8")

    def test_external_links_and_same_document_anchors_are_ignored(self):
        links = "\n".join((
            "[HTTPS](https://example.invalid/not-fetched)",
            "[HTTP](http://example.invalid/not-fetched)",
            "[Mail](mailto:maintainer@example.invalid)",
            "[Section](#local-section)",
        ))
        for document in ("README.md", "AGENTS.md"):
            (self.root / document).write_text(links, encoding="utf-8")
        self.assertEqual(validate_skills.validate(), [])

    def test_skill_directory_links_are_still_checked(self):
        path = self.skills / "guide.md"
        path.write_text("[Missing](missing.md)\n", encoding="utf-8")
        self.assertEqual(validate_skills.validate(), [f"{path}: broken link missing.md"])

    def test_root_evaluations_resolve_fixtures_and_reject_bundled_evals(self):
        skill = self.skills / "sample"
        skill.mkdir()
        (skill / "SKILL.md").write_text("---\nname: sample\ndescription: Example\n---\n")
        evaluation = self.root / "evals" / "sample"
        evaluation.mkdir(parents=True)
        fixture = evaluation / "input.txt"
        fixture.write_text("Example")
        (evaluation / "evals.json").write_text(json.dumps({
            "skill_name": "sample",
            "evals": [{"id": 1, "prompt": "Read", "expected_output": "Example",
                       "expectations": ["Reads input"], "files": ["input.txt"]}],
        }))
        self.assertEqual(validate_skills.validate(), [])
        fixture.unlink()
        self.assertEqual(validate_skills.validate(), [f"{evaluation / 'evals.json'}: missing fixture input.txt"])
        fixture.write_text("Example")
        (skill / "evals").mkdir()
        self.assertEqual(validate_skills.validate(), [f"{skill}: keep evaluations outside installable skills"])

    def test_evaluation_documentation_links_are_checked(self):
        evaluation = self.root / "evals"
        evaluation.mkdir()
        path = evaluation / "README.md"
        path.write_text("[Missing](missing.md)\n")
        self.assertEqual(validate_skills.validate(), [f"{path}: broken link missing.md"])


if __name__ == "__main__":
    unittest.main()
