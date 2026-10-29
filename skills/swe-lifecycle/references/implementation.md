# Implementation and finalization

This reference owns evidence-based coding, defect repair, and completion. It coordinates existing coding/testing skills rather than replacing them. Read [GitHub workflow](github-workflow.md) for remote changes and the knowledge/changelog references when updating those artifacts.

## implement

1. Read repository instructions, applicable language/domain/testing skills, approved requirement clauses, accepted design/ADRs, current knowledge, and assigned issue context. Inspect code and tests before changing them. Resolve inconsistencies explicitly: code can be wrong, documentation can be stale, and proposals are not approvals.
2. Establish scope, acceptance criteria, affected components, and verification appropriate to risk. Reuse explicit authorization already given for the same scope; do not repeat an approval request unless a consequential decision remains outside it. If significant requirement or architecture changes emerge, prepare the proposal and obtain approval before implementing those changes. Continue independent, authorized work where possible.
3. Follow project conventions with small cohesive edits. Avoid unrelated refactors, speculative abstractions, and unnecessary dependencies. Maintain compatibility, migrations, and rollback obligations from the approved design.
4. Run focused tests and relevant checks, recording actual commands and results. Use regression tests for meaningful defects and observable behavior tests for features. Do not add tests that merely repeat implementation or claim unrun tests passed.
5. Compare resulting behavior against acceptance criteria. Synchronize verified knowledge and current architecture/guides where affected. Create a historical changelog under project policy. Validate documentation and prepare review evidence.

## fix

Capture expected/observed behavior and reproduction first. Inspect timing, state transitions, inputs, logs, and tests relevant to the defect. Establish a root cause from evidence; if unavailable, state that the cause remains unconfirmed. Implement the narrow repair and a deterministic regression test where possible; a concurrency defect should exercise the relevant race/interleaving rather than relying on flaky sleeps.

For refresh-token rotation, an investigation may examine atomicity and concurrent refresh outcomes, but do not assert those are the cause before inspecting code. Use an existing bug issue or prepare a bug draft. Restoring documented behavior needs no new REQ/CHG; a discovered product behavior change or architectural replacement may require the specification workflow. Update knowledge if its description or operational guidance changes. Record significant fixes in changelog with verified reproduction, cause if known, and regression evidence.

## Definition of Done

Before claiming complete, verify all applicable conditions:

- Every in-scope approved acceptance criterion is satisfied with evidence. An unresolved criterion blocks completion unless the authorized owner explicitly removes it from scope.
- Relevant required tests and checks pass. Skipped, unavailable, failing, or unrun checks are clearly reported; unresolved required checks block completion.
- Implementation and migrations match approved scope, design, and accepted decisions; significant deviations have approval.
- Current knowledge, architecture, and guides reflect verified changes and link governing requirements/decisions.
- A finalized meaningful changelog exists, or an explicit policy-permitted skip reason is recorded.
- Document validation passes, cross-references resolve, and no placeholders or unsupported completion claims remain.
- PR summary, actual issue links, verification, compatibility, and remaining risks are ready for review.

Prepare or update the PR only within remote authorization. Check actual remote state after any write. Closing issues or reporting milestone completion requires its own authorized and satisfied completion scope. If criteria or checks remain unresolved, provide a partial handoff with the precise limitation and pending work; do not call the issue complete.

## Evidence handoff

Report what behavior changed, why, actual verification results, documentation/history paths, and remaining limitations. Source paths and local records must explain the implementation without requiring GitHub access. Do not copy raw terminal dumps or transient agent planning notes into permanent knowledge.
