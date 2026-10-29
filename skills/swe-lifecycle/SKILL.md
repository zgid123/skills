---
name: swe-lifecycle
description: Orchestrate AI-assisted software delivery across project bootstrap, requirement discovery and evolution, change proposals, technical design, GitHub milestones and issues, implementation, bug fixes, knowledge synchronization, changelogs, and finalization. Use when a repository needs a coherent engineering lifecycle, traceable specifications, current technical knowledge, or durable implementation history. Apply proportionately to the requested operation; ordinary small edits do not require a full lifecycle ceremony.
---

# Software engineering lifecycle

Keep expected behavior, proposed changes, current implementation, historical changes, and delivery tracking distinct. Reuse existing project conventions and documentation before adding files. This skill coordinates engineering work; load the project's language, testing, security, and domain skills for actual implementation.

## Start here

1. Inspect repository instructions, existing documentation, source, tests, and work-item context. Establish the project root and the requested operation. Never overwrite a file before reading it.
2. Read [lifecycle](references/lifecycle.md) for operation boundaries. Read [conventions](references/conventions.md) when writing or revising any lifecycle document or GitHub draft, or changing document paths and identifiers; apply its writing standard and reuse stable identifiers.
3. Load only the operation-specific references and templates below. A request may require several operations; perform only the stages needed for the requested result.
4. Distinguish observed facts, proposals, unknowns, and verified outcomes. Record the document owner and evidence. Obtain approval before significant requirement or architecture changes; existing explicit authorization counts. Ask again only when a consequential decision falls outside that authorization. Prepare a concrete draft before requesting missing approval and continue independent authorized work.
5. Validate canonical `docs/` documentation using [validation](references/validation.md) when the project has adopted that layout. Create only the canonical folders and documents useful to the current work; empty category folders are optional. In existing noncanonical projects, use established project checks and review changed documents, links, and traceability proportionate to the task. Report completed work, actual verification, pending approvals, and unavailable integrations clearly.

## Dispatch

| Operation | Read next | Templates to use when needed |
| --- | --- | --- |
| `bootstrap` | [lifecycle](references/lifecycle.md), [GitHub workflow](references/github-workflow.md) | `project.md`, `architecture.md`, `development-guide.md`, `milestone.md`, `chore-issue.md` |
| `specify` | [specifications](references/specifications.md) | `requirement.md` |
| `propose-change` | [specifications](references/specifications.md) | `change-proposal.md` |
| `design` | [specifications](references/specifications.md) | `technical-design.md`, `adr.md` |
| `plan` | [GitHub workflow](references/github-workflow.md) | `milestone.md`, `epic.md`, relevant issue template |
| `implement`, `fix` | [implementation](references/implementation.md) | relevant issue template; knowledge/changelog templates at completion |
| `sync-knowledge` | [knowledge management](references/knowledge-management.md) | `knowledge.md`, `architecture.md`, `development-guide.md` |
| `record-change` | [changelog management](references/changelog-management.md) | `changelog.md` |
| `finalize` | [implementation](references/implementation.md), [validation](references/validation.md) | `pull-request.md` |

Template names above resolve inside [assets/](assets/). Read the selected template before using it. Replace placeholders, retain mandatory sections, and remove irrelevant optional sections instead of emitting empty scaffolding. Do not copy every template into a project.

## Guardrails

- Write every document for human readers first. Agents use the same readable documents. Use natural, direct prose without AI-style boilerplate or em dashes; follow the [writing standard](references/conventions.md#writing-for-human-readers).
- Requirements describe testable expected behavior. Changes describe significant proposals. Designs explain implementation approaches. ADRs preserve consequential decisions. Knowledge describes verified current code. Changelogs preserve completed history.
- GitHub owns milestones, issues, sub-issues, dependencies, PR status, and implementation tracking. Local documents own durable technical knowledge. Do not create a duplicate local issue database.
- Read remote work when tooling permits. Create, edit, or close remote work only with explicit authorization already covering that operation. If unavailable or unauthorized, prepare clearly labeled drafts with no invented numbers or URLs.
- Do not silently alter approved requirements or accepted decisions. Preserve accepted ADRs through supersession and finalized changelogs through new records or explicitly labeled factual corrections.
- Foundation setup and ordinary bug fixes usually need no new requirement or change proposal. Initial substantial designs may link directly to a requirement.
- No green test, completed issue, root cause, or historical behavior may be claimed without evidence. A proposed implementation is not current knowledge.

## Quick use

Ask “bootstrap this repository,” “specify configurable rate limiting,” “propose an authentication migration,” “fix refresh-token rotation,” or “finalize this change.” For existing projects, adopt the established documentation incrementally rather than renumbering or restructuring history. Run the validator from any installation path:

```sh
python3 /path/to/swe-lifecycle/scripts/validate_docs.py /path/to/project
```

The validator checks document structure and references; engineering review and actual tests establish correctness. See [validation](references/validation.md) for tests and limits.
