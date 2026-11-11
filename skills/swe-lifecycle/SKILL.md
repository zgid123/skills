---
name: swe-lifecycle
description: Orchestrate AI-assisted delivery from discovery and requirements through design, GitHub planning, implementation, verification, current knowledge, and durable change history. Use for lifecycle planning, traceable specifications, feature or bug delivery, and documentation synchronization. Apply only the stages needed; small edits need no full ceremony.
---

# Software engineering lifecycle

Connect user intent, approved expectations, delivery work, implementation evidence, and current knowledge. Write concise practitioner prose: concrete behavior, decisions, and evidence, with no filler or repeated explanations. Explain each fact in its authoritative home and link elsewhere.

## Start here

1. Inspect repository instructions, existing documents, source/tests, and relevant remote work. Establish requested scope and authorization; never overwrite unread content. Apply the context rule below at every stage and whenever new uncertainty appears.
2. Read [lifecycle](references/lifecycle.md) for stage boundaries and [conventions](references/conventions.md) before writing documents or GitHub drafts.
3. Load only the references/templates needed below. Keep required sections; remove irrelevant optional ones. Preserve important rules, risks, and evidence rather than targeting a fixed length.
4. Reuse explicit authorization. Seek approval for significant new requirement/architecture changes outside it; continue independent authorized work.
5. Run [documentation validation](references/validation.md) for canonical layouts or established checks otherwise. Report actual verification, unknowns, and unfinished work.

## Missing context at any stage

First investigate facts available in the conversation, repository, tests, documentation, and connected tools. When missing context still requires a user decision, read and use the installed `grilling` skill. `grill-me` is its invocation alias in the current installation; follow the alias to the underlying skill instead of maintaining a second interview procedure here. This applies throughout discovery, planning, implementation, verification, documentation, and finalization, without requiring the user to invoke grilling again.

Use the skill's decision tree and recommendations, asking one question at a time as requested by the user. Keep the interview within the current scope; identify future questions as deferred. Continue independent authorized work while waiting, and wait for the user's decision before taking dependent actions. Record settled decisions in the relevant document and resume once shared understanding is confirmed. Reuse clear answers and existing authorization; do not repeat settled questions without new evidence. If neither skill is available, or the alias cannot load its underlying skill, conduct the clarification directly: choose the unresolved decision that unblocks the most work, ask one concise question with a recommendation and reason, and wait for the answer before asking the next. Missing interview skills do not block clarification or require installation. Continue independent authorized work, but do not guess decisions or proceed with dependent work before the user answers.

## Operations

| Operation | Reference | Template |
| --- | --- | --- |
| orchestrate | [Orchestration](references/orchestration.md), plus references for the stages being coordinated | delegation-brief, agent-handoff |
| bootstrap | [Lifecycle](references/lifecycle.md), [GitHub workflow](references/github-workflow.md) | project, architecture, development-guide; milestone/chore-issue when needed |
| specify | [Specifications](references/specifications.md) | requirement |
| propose-change | [Specifications](references/specifications.md) | change-proposal, combining proposal and design |
| design | [Specifications](references/specifications.md) | technical-design for initial features; existing CHG for changes; adr when warranted |
| plan | [GitHub workflow](references/github-workflow.md) | milestone, epic when useful, relevant issue |
| implement / fix | [Implementation](references/implementation.md) | relevant issue and existing/new change record |
| sync-knowledge | [Knowledge management](references/knowledge-management.md) | knowledge, architecture, development-guide |
| record-change | [Change records](references/change-records.md) | existing CHG or retrospective change-proposal |
| finalize | [Implementation](references/implementation.md), [Validation](references/validation.md) | pull-request |

Templates are Markdown files in [assets/](assets/); read the selected template before use. Apply relevant coding/testing skills for implementation.

Use `orchestrate` when the user requests coordinated agent work. It composes the relevant lifecycle stages; it does not require every stage or a fixed team. Follow runtime delegation permissions and use sequential execution when delegation is unavailable.

## Guardrails

- Requirements describe expectations; designs describe intended implementation; ADRs preserve consequential choices; knowledge describes verified current behavior; change records preserve intent and actual delivery; guides explain procedures.
- Each meaningful engineering change uses one CHG file grouped by its primary requirement, or by domain when no requirement applies. Sequence records within each group; link all affected requirements without duplicating cross-requirement changes. Append delivery evidence to its proposal instead of creating a separate changelog. Initial features and meaningful fixes can use retrospective records without fabricated proposals. Preserve existing historical records until migration is explicitly authorized.
- GitHub owns milestones, tasks, dependencies, PRs, and delivery status. Do not maintain a parallel local issue database. Read existing work to avoid duplicates; remote writes require authorization covering that action.
- Never merge a PR without one explicit user approval for that PR. Follow the [merge approval rule](references/github-workflow.md#commits-and-merge); implementation or PR creation authorization does not include merging.
- Preserve stable IDs, approved intent, and completed history. Record deviations and approval; later work gets a new change record.
- Do not claim tests, completion, causes, or historical behavior without evidence. A valid document or proposed design is not implementation proof.

Run the validator from any installation path:

```sh
python3 /path/to/swe-lifecycle/scripts/validate_docs.py /path/to/project
```
