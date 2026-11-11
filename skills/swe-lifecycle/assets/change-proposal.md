---
id: "CHG-<requirement-number-or-domain>-<NNNN>"
title: "<Engineering change>"
status: proposed
owner: "<Person or accountable role>"
created_at: "<YYYY-MM-DD>"
updated_at: "<YYYY-MM-DD>"
type: feature
related_requirements: []
---

# <Engineering change>

<!-- One file at docs/specs/changes/NNNNN-feature-name/NNNN-change-name.md or docs/specs/changes/domain/NNNN-change-name.md holds intent, design, and delivery evidence. Use CHG-00001-0001 or CHG-infrastructure-0001 respectively. Numbered groups must include the matching REQ in related_requirements. Cross-requirement changes live in one primary group and reference all affected requirements. For retrospective work start draft; do not fabricate a prior proposal. Keep Reason and scope and Before and after. Proposed/approved/implementing records also require Acceptance and verification plan. Implemented records require Implementation result, Verification, and References. Remove unused sections rather than leaving scaffolding. -->

## Reason and scope

<Problem, motivation, affected capability/components, and boundaries. Link existing rationale instead of repeating it.>

## Before and after

<Established previous behavior and intended new behavior. Identify unknowns. For retrospective records, describe verified changes without inventing earlier intentions.>

## Technical approach

<Proportional design: responsibilities and flows, contracts/data, consistency/security/recovery, and important trade-offs. Use subsections only when helpful. Link initial designs and ADRs instead of copying them.>

## Acceptance and verification plan

<Reference applicable REQ AC IDs and add change-specific checks, relevant failure scenarios, and migration checks. Required for prospective records; retain the plan after delivery. Planned checks are not execution evidence.>

## Risks and rollout

<Compatibility impact, affected consumers/data, deployment order, rollback limits, and unresolved decisions where relevant.>

## Approval

<Record approver, date, scope, and approval evidence. Update affected requirements only after approval. For retrospective records, identify actual authorization when available or state it was not established. If approved work is withdrawn, record the approved disposition of affected requirement clauses and partial implementation. Put general document links in References.>

## Implementation result

<Add completed contributions as work progresses: date, task/PR, behavior delivered, source paths, compatibility, and remaining scope. Link each contribution’s verification below. Keep the overall change implementing while tasks remain; mark implemented only after all scoped criteria pass. Preserve approved intent and record deviations explicitly.>

## Verification

<Checks actually run, commands, environment/date, results, and checks not run with reasons. Mark implemented only when all in-scope required criteria/checks are satisfied.>

## References

<Link current knowledge and guides updated, governing requirements/decisions, actual issues/PRs/commit when available. Explain documentation intentionally unchanged. For historical moved/deleted source use a known commit link or code-formatted old path with context.>

<!-- After implementation preserve this record. Later meaningful changes get new CHG IDs. Factual corrections must identify date, author, original claim, corrected fact, and evidence. -->
