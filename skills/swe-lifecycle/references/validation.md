# Documentation validation

This reference owns validator usage, structural checks, and verification limits. [Conventions](conventions.md) is the metadata/path contract. The script uses Python's standard library and operates on a supplied project root independently of its installation location.

## Run

```sh
python3 /path/to/swe-lifecycle/scripts/validate_docs.py /path/to/project
```

Resolve paths explicitly. The project root contains `docs/`; do not pass the skill directory or `docs/` itself. Run after creating or modifying canonical documents and before finalization when the project has adopted this layout. The validator requires the documentation index and project brief, but category directories are optional until they contain documents. For a noncanonical project, use its established documentation checks and review changed documents and references instead of creating the canonical tree to satisfy this validator. The command reports actionable path-specific errors and exits nonzero when errors occur. Inspect existing content before repairs; do not solve a validation failure by deleting user documentation or renumbering history.

## Checked contract

- Core documentation files, structured document locations when present, kebab-case filenames, five-digit REQ/CHG/ADR numbers, and four-digit changelog streams.
- Flat restricted-YAML frontmatter, malformed or duplicate keys, required fields, scalar/list types, dates, valid statuses, and nonempty mandatory sections.
- Unique stable IDs, filename/ID agreement, changelog parent requirements, relationship target types and existence, and retired ID collisions.
- Current relative Markdown document/source links and paths, including missing targets and paths escaping the supplied root. Historical source paths in finalized changelogs should be code-formatted or commit-pinned; historical code paths are not treated as links to current files.
- ADR supersession relationships, including invalid targets, reciprocal links, self-links, and cycles.
- Non-gapless numbering: gaps are legal; zero/invalid widths are errors. Allocation must use the highest occupied or reserved number, never fill gaps.

Mandatory body headings are REQ: Overview, Functional requirements, Acceptance criteria; CHG: Summary, Current behavior, Proposed behavior, Acceptance criteria; ADR: Context, Decision, Consequences; KNW: Overview, Current implementation, Known limitations; LOG: Summary, Previous behavior, New behavior, Tests and verification, Documentation updated. Other template sections are adaptive; remove irrelevant optional sections. Describe a known unknown explicitly rather than leaving a mandatory section blank.

## Verification limits

The validator is a structural snapshot check. It does not prove owner approval, historical status transitions, factual accuracy, test execution, code/specification equivalence, actual remote GitHub state, or whether a removed ID was omitted from `reserved_ids`. Review history and evidence for those obligations. Category directories need not exist until they contain a document. Markdown link scanning is intentionally bounded; inspect generated navigation and unusual Markdown syntax manually. Remote links are not fetched. An allowed lifecycle state is not evidence that a transition was authorized.

Frontmatter is a documented YAML subset, not a general-purpose YAML implementation. Convert unsupported nested structures or multiline scalars to the flat contract and prose, or explicitly adapt the tooling rather than silently treating malformed metadata as valid.

## Smoke tests and scenario review

Run the bundled local smoke-test procedure described in the skill's test/usage documentation. Keep fixtures isolated in temporary directories. Test valid documents and corrupt copies for malformed IDs, missing references, broken local links, duplicate metadata, duplicate document IDs, missing mandatory sections, and invalid ADR supersession. Include successful gapful sequences and reserved-ID non-reuse checks. No fixture or test should create remote milestones or issues.

Review lifecycle scenarios separately from parser checks: gateway bootstrap yields M0/chore planning without invented feature REQs; rate limiting yields a behavior REQ and proportional design; authentication migration reuses its REQ with CHG/design/ADRs; a refresh-token bug uses reproduction/regression without automatic specification creation; RBAC-to-ABAC evolution preserves approved behavior pending approval. Current knowledge and finalized history are produced only after verified implementation. Automated fixture checks alone do not establish that an autonomous agent follows every workflow; record that evaluation boundary honestly.
