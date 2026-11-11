# Orchestration

One lead agent coordinates delivery and communicates with the user. Specialists receive bounded assignments; the lead owns scope, integration, verification, documentation consistency, and completion. Apply only the lifecycle stages needed for the request.

## Team and authority

Use delegation when requested, permitted by the runtime, and useful for separable work or independent review. Small tasks can stay with the lead. If delegation is unavailable, perform the roles sequentially and disclose that review was not independent.

Choose roles for the work: an analyst clarifies requirements, a designer resolves technical contracts, implementers deliver assigned changes, and a reviewer checks behavior and evidence. Roles do not require permanent agents or a fixed team size. Each specialist reads the applicable repository instructions and skills.

The lead retains GitHub mutations, commit creation, and merge operations unless the user explicitly assigns those actions elsewhere. Existing authorization and [commit/merge rules](github-workflow.md#commits-and-merge) still apply. Delegation does not authorize scope changes, additional external actions, or nested delegation; nested work needs the lead's explicit assignment and runtime permission.

## Assign ready work

1. Inspect current artifacts and establish the approved result, acceptance criteria, and relevant Definition of Done. Separate settled decisions from unknowns.
2. Identify dependencies and file ownership. Settle shared contracts before assigning dependent implementation. Parallelize independent investigation or changes with separate ownership.
3. Send a [delegation brief](../assets/delegation-brief.md) with source references, scope, allowed paths, prerequisites, expected output, and verification. Provide enough context to act without copying the entire conversation.
4. Keep assignment status in the active conversation or temporary working notes. GitHub remains the delivery tracker; do not add a permanent agent-task database under docs.

In a shared workspace, assign each writable file to one agent at a time, including shared schemas, lockfiles, and change records. Use isolated worktrees when edits overlap and later integration is worthwhile; otherwise serialize them. Never overwrite another agent's or the user's work. The lead allocates shared document IDs and coordinates contract changes before dependent work resumes.

For example, after an API contract is settled, backend and admin UI work can proceed separately. A reviewer can inspect the completed integration. If the UI requires an unresolved response shape, settle it first instead of having both agents invent it.

## Resolve uncertainty

Specialists investigate available facts and report unresolved decisions to the lead. The lead applies the [missing-context rule](../SKILL.md#missing-context-at-any-stage), using grilling and asking the user one question at a time. Workers do not run competing user interviews.

Continue independent authorized work while a decision is pending. Pause dependent assignments and distribute the settled answer to affected agents. Record durable decisions in the existing requirement, design, ADR, or change record as appropriate.

## Integrate and review

Require an [agent handoff](../assets/agent-handoff.md) identifying changed artifacts, acceptance coverage, actual check results, and unresolved work. A specialist's report is evidence to inspect, not automatic acceptance.

The lead reviews diffs, integrates in dependency order, and checks contracts and behavior across assignments. Reuse valid check evidence for unchanged scope; run required combined checks against the integrated state and rerun affected checks after fixes. Reconcile current knowledge, guides, and the shared change record without duplicating specialist reports as permanent documents.

For independent review, give a separate reviewer the acceptance criteria, relevant decisions, integrated diff, and verification evidence. Ask for actionable findings with locations, impact, and reproduction or reasoning. Prioritize correctness and missing acceptance coverage over stylistic preferences.

Set a bounded correction loop in the assignment, normally two fix-and-review passes. Stop repeating a failing approach when a pass produces no new evidence. At the bound, the lead diagnoses remaining findings and either applies a concrete alternative within scope or reports the blocker; a user decision goes through grilling. Do not dismiss unresolved required findings to meet the limit or restart the same loop under a new assignment.

## Complete the work

Apply the existing [task and milestone completion rules](implementation.md). The lead checks the integrated outcome, updates authorized tracking, and reports verified results and remaining limitations. A worker finishing, all tasks closing, or a clean document validator alone does not establish completion.

Preserve useful decisions and delivery evidence in their existing authoritative documents. Briefs and handoffs are coordination material, not new specifications or historical records. On resuming interrupted work, inspect current artifacts and outstanding assignments before dispatching duplicate work.
