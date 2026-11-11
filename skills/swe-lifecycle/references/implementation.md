# Implementation and completion

Read the repository instructions, relevant coding/testing skills, approved requirements, applicable designs/decisions, current knowledge, and issue context. [GitHub workflow](github-workflow.md) governs remote actions.

For delegated work, follow [orchestration](orchestration.md). Task handoffs supply evidence; the lead remains responsible for reviewing and verifying the integrated result.

## Implement or fix

1. Inspect code and tests, establish scope and acceptance, and choose verification appropriate to risk. For bugs establish observed/expected behavior and a reproducer; label suspected causes until verified.
2. Reuse authorization for agreed work. Obtain approval only for consequential changes outside it; continue independent authorized work. Approved documents can be stale and code can be wrong: resolve contradictions explicitly.
3. Make cohesive changes using existing patterns. Preserve required compatibility, migration, and rollback behavior. Test observable behavior, including relevant failure/concurrency cases; avoid implementation-mirroring tests.
4. Run focused checks and record commands/results and unrun checks. Compare actual behavior with acceptance; do not silently change requirements to match accidental implementation.
5. Update [current knowledge](knowledge-management.md) and guides where affected. Add delivery evidence to the existing [change record](change-records.md), or create a retrospective record under policy. Do not create a second history file for the same work.

## Task completion

Each task must satisfy its own applicable acceptance criteria and required checks. A task or PR may complete while its wider change remains implementing; append that contribution and its evidence to the shared change record. The whole change becomes implemented only when its complete scope passes. Significant requirement/architecture deviations need approval. Knowledge, architecture/guides, and meaningful history must reflect verified scope; an allowed trivial-history skip needs a reason. Validate documents and prepare a PR/handoff with actual issues, behavior, why, evidence, compatibility, and limitations. Link the project’s published Definition of Done from issues and PRs; if none exists, define it in the project documentation before relying on it.

Unresolved required checks or criteria block completion unless explicitly removed from scope by the authorized owner. Report partial work honestly. Never claim unrun tests passed or invent causes/history.

## Milestone completion

Review the integrated workflow against milestone exit criteria, not just child issue status. Confirm required combined checks, current knowledge/navigation, reproducible testing/operations guidance, change history, and remaining limitations. Avoid a duplicate milestone history document when linked change records and GitHub evidence suffice.

Creation/update/closure of remote work must be within authorization and reflect actual state. Read back mutations. Preparing a PR does not merge it; completing a task does not establish milestone completion.

When preparing or creating a commit, follow the [commit-message rules](conventions.md#commit-messages) and [PR commit policy](github-workflow.md#commits-and-merge). Finish planned work before the initial commit; later fixes use new commits. Inspect the changes being committed so the short subject accurately describes their scope.
