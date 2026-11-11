# Document conventions

## Writing for human readers

Write as an experienced engineer, product owner, business analyst, or QA practitioner documenting real work. State the purpose, behavior, decision, or result directly. Use plain language, precise terms, and concrete evidence. Keep only information needed to understand, implement, verify, or maintain the work.

Remove generic introductions, promotional language, filler, repeated summaries, vague claims such as “robust” or “seamless,” and unnecessary headings. Replace them with observable behavior or measurable constraints. Explain unfamiliar terms once. Preserve quotations and code; avoid em dashes in authored prose. Do not invent facts, experience, approvals, or verification.

Before delivery, read the document as its intended user. Remove repetition, check that decisions and acceptance criteria are actionable, and distinguish evidence from assumptions. Concise means sufficient and direct; it does not impose a word limit.

Use the short templates by default. Remove irrelevant optional sections; add subsections only when complexity warrants them. Do not omit material business rules, acceptance cases, security, recovery, compatibility, or evidence to meet a length target.

Each explanation has one authoritative home. Requirements own expected behavior; designs own proposed implementation; ADRs own consequential choices; knowledge owns verified current behavior; change records own intent and delivery history; guides own procedures. Elsewhere summarize just enough to orient the reader and link. Metadata need not be repeated as prose.

## Commit messages

Use `<type>: <description>` for authored commit subjects. Choose the type that describes the change: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `perf`, `build`, `ci`, `style`, or `revert`. Follow an existing repository scope convention when applicable, such as `fix(auth): reject expired sessions`.

Write a short, concrete description with an imperative verb: `add`, `fix`, `remove`, or `simplify`. Aim for about 50 characters and keep the subject within 72 characters unless the repository requires another limit. Omit a trailing period, filler, promotional language, and commentary about the authoring process. Describe the actual change; avoid vague subjects such as `chore: improve implementation`.

Examples: `feat: add expansion management`, `fix: preserve drafts after upload failure`, `docs: clarify publication rules`. Add a brief body only when rationale, compatibility, migration, or breaking-change details need explanation. Derive the message from the changes being committed and follow repository-required trailers.

## Responsibilities and paths

| Artifact | Location | Purpose |
| --- | --- | --- |
| Index | docs/README.md | Main navigation |
| Project | docs/project.md | Vision, scope, ownership, working policies |
| Requirement | docs/specs/requirements/NNNNN-feature-name.md | Current approved expectations |
| Feature index | docs/specs/requirements/README.md | Optional capability navigation to requirements, knowledge, history, tests, GitHub |
| Change | docs/specs/changes/NNNNN-feature-name/NNNN-change-name.md or docs/specs/changes/domain/NNNN-change-name.md | Proposal, proportional design, and delivery evidence grouped by requirement or domain |
| Initial design | docs/architecture/NNNNN-feature-name-design.md | Substantial initial implementation approach |
| Architecture | docs/architecture/README.md and topic pages | Verified system boundaries and flows |
| ADR | docs/decisions/NNNNN-decision-name.md | Consequential choice and rationale |
| Knowledge | docs/knowledge/domain/README.md or topic.md | Verified domain/capability implementation |
| Guide | docs/guides/topic.md | Reproducible development, testing, or operations |
| Glossary | docs/glossary.md | Optional short definitions shared across domains |

Create indexes and glossary only when useful. Do not create a second feature index or mirror GitHub task status. Architecture explains system-wide structure; domain knowledge explains implementation details. Initial designs link to verified knowledge after delivery and remain identified as design records.

Use lowercase kebab-case names. Each meaningful change gets one file and a CHG ID, including initial implementation and significant fixes. Reuse its proposal for delivery evidence rather than creating a changelog. Later changes get new records. Initial implementation records link the initial design instead of copying it.

Group requirement changes under the matching requirement number and descriptive slug. Each record must list that requirement in related_requirements. For work with no governing requirement, use a descriptive domain folder such as infrastructure. A change affecting several requirements belongs in one primary requirement folder and references all affected requirements; do not duplicate the record. Indexes can link that record from other capabilities.

## IDs and metadata

Allocate REQ-00001 and ADR-00001 independently above the highest occupied or reserved ID. Changes have a four-digit sequence within each requirement/domain: CHG-00001-0001 for requirement REQ-00001, or CHG-infrastructure-0001 for infrastructure. Allocate above the highest occupied or reserved sequence in that group; never restart numbering for a renamed folder. An initial design number matches its requirement. Knowledge IDs use KNW-domain-topic. Preserve FR/NFR/AC clause IDs when editing requirements.

Inspect records, project reserved_ids, and relevant history before allocation. Never fill gaps or reuse removed IDs. Reserve an ID before removing a record; retained retired records already occupy their IDs. Resolve branch collisions by preserving established IDs and reallocating only conflicting unpublished work with all references updated.

Structured documents use flat frontmatter: scalar strings, null, JSON string lists, or two-space YAML list items. No nested mappings, aliases, tags, block strings, or unquoted inline lists. Dates are YYYY-MM-DD. Common fields are id, title, status, owner, created_at, updated_at. Owners must be resolved; dates must reflect real work.

| Kind | Additional fields | Status |
| --- | --- | --- |
| REQ | dependencies, related_changes; optional priority | draft, approved, retired |
| CHG | related_requirements; optional type | draft, proposed, approved, implementing, implemented, rejected, withdrawn |
| ADR | supersedes, superseded_by | proposed, accepted, superseded, rejected |
| KNW | requirements, decisions, components | draft, verified |

CHG type, when present, is feature, fix, migration, refactor, chore, or docs. The template includes it; do not repeat it as a body section. Priority is low, medium, high, or critical. Project metadata requires owner; history_policy is meaningful (default) or every-issue, and reserved_ids is a permanent list of removed IDs. Link actual issues, PRs, commits, and affected source in prose without inventing metadata or remote references.

Relationship fields target existing documents of their expected kind: dependencies/requirements/related_requirements target REQ; related_changes/changes target CHG; decisions/supersedes/superseded_by target ADR. Reserved IDs do not satisfy links to live documents. Components name real source paths or subsystems. Requirement/decision indexes can be plain Markdown; if structured, their usual metadata and sections apply.

## Lifecycle and preservation

- REQ: draft → approved → retired. Material behavior updates need approval; update affected clauses and link the change once approved. Requirements describe expectations, not proof of implementation.
- CHG: proposed → approved → implementing → implemented; proposed may be rejected/withdrawn and approved may be withdrawn. Withdrawal during implementation records partial work and rollback consequences. Retrospective records start draft and become implemented only after verifying completed authorized work; do not fabricate a prior proposal or approval. Drafts can move to proposed if they become prospective.
- ADR: proposed → accepted/rejected. On accepting a successor, mark the predecessor superseded and update reciprocal links together. Proposed replacements link predecessors in prose without prematurely changing supersession metadata.
- KNW: draft → verified only with evidence; return to draft if accuracy becomes uncertain.

An approved change can span several issues and PRs. Record completed contributions and their evidence while keeping the change implementing until its full acceptance criteria pass. Completing a task does not require completing the whole change.

When withdrawing a change that affected approved requirements, record which clauses remain expected for later delivery, which are revised, and which return to their previous rule. Obtain approval for changed expectations and update only affected clauses, preserving unrelated later edits. Record partial implementation, retained behavior, and rollback consequences; do not leave contradictory requirements silently in place.

Preserve approved intent and add actual results separately. Mark CHG implemented only when its in-scope acceptance and required checks are satisfied. Do not turn partial delivery into completion. Preserve implemented records, rejected decisions, and accepted ADR rationale. Later work gets a new record; factual corrections identify date, author, original claim, corrected fact, and evidence.

Use relative links to existing current documents/source. For moved/deleted historical source, use a known commit-pinned URL or code-formatted old path with known revision context. Never invent a commit or knowingly broken link.

## Existing repositories

Do not rewrite project documentation merely to shorten a template. Existing full-length headings, flat CHG-NNNNN files, legacy NNNNN-change/proposal.md with optional design.md, and LOG changelogs remain readable and validated for compatibility. Legacy CHGs using their original full-length sections keep that section contract, including implemented records whose evidence may live in a linked LOG. Existing evidence and links remain subject to review; this compatibility rule does not establish completion. New records use grouped paths and IDs. New history uses CHG records; old changelog_policy is accepted as an alias for history_policy. Conflicting policy values are an error.

Migrating existing flat changes, split proposal/design records, or LOG history requires explicit scope. Preserve IDs, approval evidence, source history, and inbound links; do not delete/renumber historical records automatically. Existing LOG IDs remain reserved/recognized. A template update alone does not authorize migration.
