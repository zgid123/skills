# SWE lifecycle usage

Load [SKILL.md](SKILL.md) through your agent environment. The skill uses local repository access and Python for read-only documentation validation; connected GitHub tools or an authenticated CLI are needed only for authorized remote work.

## Workflow

Discover and specify expectations, design proportionately, plan milestones/tasks, implement and verify, update current knowledge, and preserve change history. Use only relevant stages. Templates stay short; add detail for real complexity rather than filling every heading.

Each requirement has a change folder, such as docs/specs/changes/00001-catalog/, with sequential files such as 0001-initial-implementation.md. Work without a governing requirement uses a domain folder such as infrastructure/. One file holds each change's proposal, design, and actual result; cross-requirement changes link all affected requirements from one primary folder. Initial features/fixes without proposals can have retrospective records. Requirements remain current expectations; knowledge remains verified implementation. Historical LOG files and older section layouts remain supported for existing repositories.

## Resources

- [Orchestration](references/orchestration.md): lead-agent ownership, specialist assignments, integration, and review. Use the [delegation brief](assets/delegation-brief.md) and [agent handoff](assets/agent-handoff.md) in agent messages or temporary working notes.
- [Lifecycle](references/lifecycle.md): stage inputs and outputs.
- [Conventions](references/conventions.md): document ownership, paths, IDs, metadata, concise writing, and migration.
- [Specifications](references/specifications.md): requirements, change approval, and design.
- [GitHub workflow](references/github-workflow.md): authorized delivery tracking.
- [Implementation](references/implementation.md): task and milestone completion.
- [Knowledge](references/knowledge-management.md): current behavior and question-answering navigation.
- [Change records](references/change-records.md): durable intent and implementation history.
- [Validation](references/validation.md): structural checks and their limits.

Assets contain project, requirement, change-proposal, technical-design, architecture, adr, knowledge, development-guide, milestone, epic, feature-issue, bug-issue, chore-issue, and pull-request templates. ADR means Architecture Decision Record: a consequential choice, its alternatives, rationale, and consequences.

## Verification

```sh
python3 /path/to/swe-lifecycle/scripts/validate_docs.py /path/to/project
python3 -m unittest discover -s /path/to/swe-lifecycle/scripts/__tests__ -p 'test_*.py'
```

Tests use disposable local fixtures and never create GitHub work. Structural validation cannot prove approval, test execution, implementation accuracy, or historical preservation. Review those separately. Installing/updating the skill does not migrate a project's documents or authorize remote publication.
