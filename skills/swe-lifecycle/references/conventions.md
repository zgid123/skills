# Document conventions

This reference owns writing standards, paths, identifiers, metadata, and lifecycle states. Templates own section scaffolding. [Validation](validation.md) explains executable checks and limits.

## Writing for human readers

Every lifecycle document is written for people: indexes, project briefs, requirements, proposals, designs, decision records, knowledge pages, changelogs, guides, and GitHub milestones, issues, and pull requests. Agents read the same documents; do not create a separate agent-oriented version.

- Write for the person who needs to understand, decide, maintain, or use the subject. Give enough context to follow the document without the authoring conversation. Explain what matters, why it matters, and the evidence or action the reader needs.
- Use natural, direct prose, concrete names, and precise verbs. Explain unfamiliar abbreviations on first use when the intended reader needs them. Keep technical detail that helps the reader make a decision or do the work.
- Avoid AI-style boilerplate: generic introductions, inflated claims, buzzwords, formulaic transitions, repetitive summaries, and commentary about generating the document. Replace vague claims with specific behavior, rationale, examples, or evidence.
- Do not use em dashes in newly written or revised prose. Use a period, comma, colon, or parentheses as the sentence requires. Preserve verbatim quotations, code, source titles, and historical evidence faithfully rather than silently editing them for style.
- Use paragraphs for explanations, lists for parallel items or steps, and tables for comparisons. Keep headings useful and remove empty template sections. Metadata supports traceability; the body must remain understandable without decoding IDs or frontmatter.
- Before delivery, read the changed text as its intended reader. Remove filler, unexplained jargon, repetition, and em dashes from authored prose. Structural validation does not establish readability.

## Responsibilities and paths

| Artifact | Location | Purpose |
| --- | --- | --- |
| Index | `docs/README.md` | Human and agent navigation |
| Project | `docs/project.md` | Objective, owners, workflow policy, retired identifiers |
| Requirement | `docs/specs/requirements/NNNNN-feature-name.md` | Expected capability behavior |
| Change | `docs/specs/changes/NNNNN-change-name/proposal.md` | Significant proposed evolution |
| Change design | Same change directory, `design.md` | Proposed implementation |
| Initial design | `docs/architecture/NNNNN-feature-name-design.md` | Substantial initial implementation approach |
| Knowledge | `docs/knowledge/domain/README.md` or `topic.md` | Verified current implementation |
| Changelog | `docs/changelog/NNNNN-feature-name/NNNN-description.md` or `docs/changelog/domain/NNNN-description.md` | Permanent completed implementation history |
| ADR | `docs/decisions/NNNNN-decision-name.md` | Consequential architecture decision |
| Architecture | `docs/architecture/README.md` and focused Markdown pages | Current system structure |
| Guide | `docs/guides/topic.md` | Reproducible procedure |

Use lowercase kebab-case slugs, five digits for requirement/change/ADR namespaces, and four digits for each changelog stream. Do not encode technology or status in stable IDs. An initial design number matches its requirement; link it directly to that requirement. Other architecture pages have descriptive kebab-case names.

Requirement and decision directories may include a plain `README.md` navigation index. If it has frontmatter, it is treated as a structured REQ or ADR and needs a unique valid ID and the usual required fields; its index filename is exempt from the numbered document filename rule.

## Allocation and non-reuse

- Allocate `REQ-00001`, `CHG-00001`, and `ADR-00001` independently, using one more than the highest allocated numeric suffix in that namespace.
- Knowledge uses `KNW-domain-topic` (for a domain overview, `KNW-domain-overview`). Keep the ID stable if a title or path changes.
- Requirement changelogs use `LOG-00001-0001`; the parent number matches `REQ-00001`. Domain streams use `LOG-foundation-0001`. Increment within the stream, regardless of gaps.
- Inspect all documents and `docs/project.md` frontmatter `reserved_ids` before allocating. Add an identifier to that list before removing its document; never reuse it. IDs of retained retired documents already remain occupied and need no duplicate reservation. Include abandoned allocated IDs if documents were never committed.
- Reserve identifiers in one cohesive local edit and recheck before finalization. If parallel branches assign the same ID to different new documents, keep the ID already integrated or otherwise established; reallocate the conflicting unpublished document and update its filename and all references in the same change before integration. Do not renumber established records or create a central allocation service. The validator can detect current collisions, but cannot prove an identifier was never removed from Git history. Review history when adopting an existing project.
- Do not renumber, compact gaps, or create an extra identifier database. Stable local clauses such as `FR-001`, `NFR-001`, and `AC-001` remain stable inside a requirement.

## Frontmatter schema

Use frontmatter only for requirement, change proposal, ADR, knowledge, changelog, and project configuration. Designs are ordinary Markdown with links to governing documents. The validator supports a deliberately limited YAML subset: unique flat keys; scalar strings; `null`; JSON-style inline string arrays; and two-space-indented block lists of strings. Quote strings with punctuation that YAML could interpret, especially colons and `#`. Use no nested mappings, anchors, tags, multiline scalars, or YAML-style unquoted inline arrays. Dates are `YYYY-MM-DD`; lists contain only strings. Empty relationships use `[]`, not null. Empty commit uses `null`.

REQ, CHG, ADR, and KNW require `id`, `title`, `status`, `owner`, `created_at`, and `updated_at`. Owners are accountable people or established team names. Dates reflect actual creation and last substantive update; `updated_at` cannot precede `created_at`.

| Kind | Additional required fields | Status values |
| --- | --- | --- |
| REQ | `dependencies`, `related_changes` | `draft`, `approved`, `retired` |
| CHG | `related_requirements` | `proposed`, `approved`, `implementing`, `implemented`, `rejected`, `withdrawn` |
| ADR | `supersedes`, `superseded_by` | `proposed`, `accepted`, `superseded`, `rejected` |
| KNW | `requirements`, `decisions`, `components` | `draft`, `verified` |
| LOG | `id`, `title`, `status`, `owner`, `date`, `type`, `requirements`, `changes`, `decisions`, `github_issues`, `github_prs`, `commit`, `components` | `draft`, `finalized` |

LOG replaces the common date fields with `date`. Its `type` is `feature`, `fix`, `migration`, `refactor`, `chore`, or `docs`. `commit` is a string or null. Other fields ending in relationships or components are lists of strings. REQ may include `priority` (`low`, `medium`, `high`, `critical`). Project frontmatter requires a resolved `owner`, and includes `changelog_policy` (`meaningful` default or `every-issue`) and `reserved_ids` (list of retired identifiers). More context belongs in prose; do not invent a parallel task tracker.

IDs in relationship fields resolve to existing documents of the appropriate kind. `dependencies`, `requirements`, and `related_requirements` target REQ; `related_changes` and `changes` target CHG; `decisions`, `supersedes`, and `superseded_by` target ADR. Reserved IDs prevent reuse but do not satisfy a live reference. Keep retired referenced documents when traceability needs them. Components identify real source paths or clear subsystem names. GitHub references are known URLs or real issue/PR references; leave unavailable references empty.

Use relative Markdown links for current supporting documents and source files. Metadata IDs support retrieval but do not substitute for navigable body links. Update inbound links when moving a document. Avoid linking a nonexistent future artifact: describe it as planned prose until created. In finalized changelogs, prefer a commit-pinned source link when the revision is known. If the source has moved or the revision is unavailable, preserve the historical path as code text and state the known revision, commit, PR, or date context; do not make a broken relative link or invent revision data. The validator checks current Markdown links, not code-formatted historical paths.

## Valid lifecycle transitions

| Kind | Allowed transitions and authority |
| --- | --- |
| REQ | `draft → approved → retired`; approval/retirement needs the owner or authorized user. An approved behavioral revision retains the ID, records the approval and related change, and remains approved only once that revision is approved. Prepare proposals separately while approval is pending. |
| CHG | `proposed → approved → implementing → implemented`; `proposed → rejected` or `withdrawn`; `approved → withdrawn`; `implementing → withdrawn` only after assessing partial implementation and rollback. Rework rejected/withdrawn proposals under a new ID if scope materially changes. |
| ADR | `proposed → accepted` or `rejected`; `accepted → superseded` only when an accepted successor exists. While a replacement is proposed, link the predecessor in prose and explain the intended relationship there; keep supersession metadata empty. On acceptance, add reciprocal `supersedes`/`superseded_by` metadata and mark the predecessor superseded together. Preserve prior rationale and avoid self-links or cycles. |
| KNW | `draft → verified` after evidence; `verified → draft` if accuracy becomes uncertain; refresh verified content and verification evidence as implementation changes. |
| LOG | `draft → finalized` after verification; finalized records stay finalized and historically intact. Mark factual corrections explicitly with date, author, reason, and evidence. |

Approval and state transitions are workflow obligations: a snapshot validator validates allowed statuses and relationships, not the authority or historical transition that produced them. Record significant approvals and evidence in the document body without duplicating GitHub status.
