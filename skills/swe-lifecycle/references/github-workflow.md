# GitHub delivery workflow

This reference owns work-item planning and remote operations. GitHub is authoritative for milestones, issues, epics/sub-issues, dependencies, PR status, and delivery tracking. Local specifications and knowledge remain authoritative technical documents. Load the relevant milestone, epic, feature-issue, bug-issue, chore-issue, or pull-request template from `../assets/` as needed.

## Inspect capabilities and authorization

Read available connected GitHub tools or authenticated CLI context before selecting a mechanism. Prefer the connected integration when it supports the operation. Read existing milestones, issues, and PRs to avoid duplicates and preserve context. Do not infer authentication or feature availability.

Explicit authorization is required before creating, modifying, or closing remote work items. A request to “create the milestone and issues” can authorize those operations; a request to “plan this feature” alone does not automatically authorize remote publication. Reuse authorization already clearly given in the session. Prepare concrete drafts and links before asking for any missing authorization. Do not request it again for an unchanged authorized operation.

If access, tooling, authentication, or authorization is unavailable, produce structured drafts in the response or a temporary handoff artifact outside the repository's permanent docs. Label them unpublished. Include no invented issue numbers, URLs, dates, assignments, or remote status. Do not maintain local issue mirrors or a task-state database. Once drafts are published, GitHub owns their tracking.

Use an existing issue when one already tracks the work. Prepare a new unpublished bug/issue draft when the user asks for tracking or it materially helps an implementation handoff; a small standalone fix does not need a draft issue merely to satisfy this workflow.

## Plan delivery

1. Read approved requirements, relevant changes, designs, architecture, and existing delivery objectives. Identify unresolved decisions and dependencies.
2. Define a milestone by delivery outcome and completion criteria. A milestone may include several requirements; a requirement may span milestones. Avoid inventing artificial one-to-one mappings.
3. Use an epic only when grouping several issues improves understanding. Use native sub-issues and dependencies when supported and authorized. When unavailable, use accurate checklist links or explicit blocking relationships in issue bodies; do not build a local dependency database.
4. Create independently actionable feature, bug, or chore issues. State problem, scope, relevant specification/design paths, verifiable acceptance criteria, verification, dependencies, and documentation obligations. Split tasks by deliverable behavior or necessary technical dependency, rather than speculative layers.
5. Associate the relevant milestone and known parent/dependencies using actual remote identifiers. Check resulting state after mutations and report created/updated links. On partial failure, report what succeeded before retrying; inspect for duplicates first.

For `M0 Foundation`, plan runtime/tooling, repository conventions, configuration, CI, basic testing, and essential operations as needed. Do not add feature specs or issues for capabilities the user did not request.

## Bug issues and PRs

Bug issues capture observed versus expected behavior, reproduction, environment, impact, investigation evidence, and regression criteria. Label suspected causes as hypotheses. A bug restoring approved behavior generally links an existing requirement instead of generating a new one.

PRs describe concrete behavior changes, scope, specification/design links, verification actually performed, knowledge/changelog updates or an explicit skip rationale, and remaining limitations. Use real issue references; closing keywords imply closure on merge and require authorization for that closure. Preparing a PR description does not mean a PR was created, merged, or its issue completed.

Remote item publication does not establish implementation completion. Follow [implementation](implementation.md) for the Definition of Done, and report blocked or unverified work honestly.
