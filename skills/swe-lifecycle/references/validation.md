# Documentation validation

Run the read-only validator against a project root containing docs/:

```sh
python3 /path/to/swe-lifecycle/scripts/validate_docs.py /path/to/project
```

For noncanonical repositories use established checks and proportionate link/content review. Never delete or renumber records just to pass validation.

## Contract

The validator checks required index/project files, canonical paths, metadata types/dates/status, unique IDs, matching filenames, references, local Markdown links/anchors, reserved IDs, and reciprocal acyclic ADR supersession. New history uses a four-digit file sequence under a requirement/domain folder, with matching CHG-00001-0001 or CHG-infrastructure-0001 IDs. Numbered groups must reference their matching requirement; all relationship targets must exist. Flat legacy CHG files, legacy split proposal/design files, LOG records, and prior full-length section sets remain supported without forcing migration.

Core concise headings:

| Kind | Required |
| --- | --- |
| REQ | Problem and goal; Requirements and rules; Acceptance scenarios |
| CHG | Reason and scope; Before and after |
| ADR | Context; Options and decision; Consequences and revisit conditions |
| KNW | Overview; How it works; Verification and limitations |

Prospective CHG states proposed/approved/implementing also require Acceptance and verification plan. Implemented CHGs require Implementation result, Verification, and References, in addition to their core sections. Retrospective drafts need no fabricated proposal/plan. The validator checks nonempty sections, not whether the evidence proves their claims. New grouped CHGs must use the concise section contract, including delivery evidence when implemented. Historical CHG-NNNNN records at their original flat or split paths may use their complete original section set without adding the new delivery headings. Review their existing evidence, including linked LOG records, separately. The validator recognizes legacy formats; it cannot establish when a file was created.

Required sections reject recognizable unfilled instruction placeholders and standalone TODO/TBD markers. Literal fenced, indented, or inline code, HTML attributes, and autolinks remain valid. This is a conservative scaffold check, not an assessment of evidence quality or writing style.

Other sections are optional and proportional. Existing legacy LOG headings remain Summary, Previous behavior, New behavior, Tests and verification, Documentation updated.

## Limits and verification

The flat YAML parser supports only the subset in [conventions](conventions.md). Validation cannot prove approval, actual test execution, source/spec equivalence, historical immutability, high-water allocation, or remote GitHub state. Markdown parsing is bounded; remote URLs are not fetched. Review these matters separately.

Use temporary fixtures to check new and legacy formats, required delivery evidence, invalid metadata, broken links, missing relationship targets, duplicate/reserved IDs, and ADR supersession. Never create remote work for validator tests. Scenario review should confirm that small fixes avoid fabricated proposals and that partial work never becomes implemented merely because structural checks pass.
