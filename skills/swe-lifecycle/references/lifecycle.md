# Lifecycle operations

Use only stages relevant to the request. Inspect repository instructions, documentation conventions, source, and remote work first. Preserve user content; migrating an existing layout is separate scope. A solo maintainer may approve their project; an agent's draft does not approve itself.

At every stage, apply the [missing-context rule](../SKILL.md#missing-context-at-any-stage): investigate facts and use the installed grilling skill for decisions that remain unresolved.

## Workflow

For requested multi-agent delivery, use [orchestration](orchestration.md) to coordinate the stages below. It is an execution mode, not an additional approval stage or document hierarchy.

| Stage | Read | Produce or update |
| --- | --- | --- |
| bootstrap | [Conventions](conventions.md), [GitHub workflow](github-workflow.md) | Useful index/project brief, baseline architecture/guides, M0 foundation work if requested |
| specify | [Specifications](specifications.md) | Expected behavior, rules, scenarios, approval evidence |
| propose-change / design | [Specifications](specifications.md) | One CHG with proposal/design for evolution; initial design for a new substantial feature; ADR only when warranted |
| plan | [GitHub workflow](github-workflow.md) | Outcome-based milestone and actionable issues linked to specifications |
| implement / fix | [Implementation](implementation.md) | Code, verification, and authorized deviations |
| sync-knowledge | [Knowledge management](knowledge-management.md) | Verified current behavior and reproducible guides |
| record-change | [Change records](change-records.md) | Actual result and evidence in the same CHG, or retrospective record when no proposal exists |
| finalize | [Implementation](implementation.md), [Validation](validation.md) | Task/milestone completion evidence and authorized remote updates |

Capture expectations before coding. Update knowledge and history as meaningful work completes, then consolidate at milestone review. Do not force bootstrap chores or routine fixes through a full specification/design ceremony. Initial feature delivery links its existing requirement/design in the change record rather than repeating it.

GitHub owns work status; local documents own durable intent, current knowledge, and history. Draft plans remain proposals until approved, and documentation validation alone does not establish readiness or implementation completion.
