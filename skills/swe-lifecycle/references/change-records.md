# Change records and implementation history

Use one file in docs/specs/changes/NNNNN-feature-name/NNNN-change-name.md, or docs/specs/changes/domain/NNNN-change-name.md for work without a governing requirement, for both intent and delivery. Read [conventions](conventions.md) for IDs, paths, status, and preservation; use [the change template](../assets/change-proposal.md).

## When to record

history_policy defaults to meaningful: record completed functional features, significant fixes, migrations, and meaningful refactors. every-issue requires history coverage for every completed implementation issue. Several issues can share one change record if each completed contribution and its verification can be identified. Trivial formatting/docs work may skip under meaningful with a concrete reason in the handoff/PR. Do not invent proposals for routine fixes.

## Record the work

1. Search existing changes by requirement, scope, issue/PR, and source to avoid duplicates. Extend the existing change record for this work. Allocate a new CHG only for distinct work, using the next four-digit sequence in the requirement/domain group. Multiple changes may reference the same REQ. Cross-requirement work lives under one primary requirement and lists all affected requirements; never duplicate it.
2. For prospective significant evolution, record reason/scope, before/after, proportional technical approach, acceptance/verification plan, risks/rollout, and approval. Update affected requirements after approval.
3. For initial features or fixes without a proposal, start a retrospective draft from evidence. Reference the existing requirement/design or defect report; state unknown previous behavior honestly. Infrastructure may have no related requirement.
4. Add Implementation result, Verification, and References: actual behavior and important source paths, deviations, compatibility/migration effects, commands/results/environment, unrun checks, current documentation updates, and genuine issue/PR/commit links. Plan and actual results remain distinguishable; external links are supplementary, not the only explanation.
5. As tasks finish, add dated contributions identifying the task/PR, behavior delivered, verification, and remaining scope. Use a short list or table only when several contributions need distinction; keep authoritative task status in GitHub. Individual tasks and PRs may finish while the change remains implementing. Verify the full change acceptance and required checks before setting implemented. Retrospective partial records stay draft; prospective partial records stay implementing. For material deviations obtain approval rather than quietly rewriting expectations.
6. If approved work is withdrawn, reconcile the affected requirement clauses and partial implementation under [the lifecycle rules](conventions.md#lifecycle-and-preservation). Preserve the reason and approved disposition.
7. Preserve the completed record. Later work gets a new ID; factual corrections retain original context and identify date, author, reason, and evidence.

Do not create a separate changelog for the same work. Existing LOG records remain historical evidence until an explicitly authorized migration. Do not copy conversation transcripts, debugging dumps, or every edit into permanent history.
