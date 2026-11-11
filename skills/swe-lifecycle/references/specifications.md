# Requirements and design

Read [conventions](conventions.md) for document responsibilities, metadata, and approval. Use the requirement, change-proposal, initial technical-design, or ADR template appropriate to the work.

## Discover and specify

1. Read existing requirements, knowledge, architecture, source, and task context. Reuse stable capability requirements instead of creating one for each implementation change.
2. Apply the [missing-context rule](../SKILL.md#missing-context-at-any-stage). Investigate available facts, then use the installed grilling skill for unresolved user decisions about actors, goals, boundaries, rules, failure cases, and acceptance.
3. Capture expected behavior before implementation. Use Problem and goal, Requirements and rules, and Acceptance scenarios as the core. Optional user stories express who needs what and why; do not repeat their purpose in several sections.
4. Keep stable FR/NFR/AC IDs. Acceptance scenarios cover relevant success, invalid/boundary, failure, and recovery cases with measurable results. Label illustrative examples; they are not automatically mandatory tests.
5. Separate requirements from proposed solutions unless technology is an explicit constraint. Record unresolved decisions and their consequences. Obtain approval for significant behavior and record approver/date/scope/evidence before marking approved.

## Change existing behavior or architecture

Use a grouped change file under docs/specs/changes/NNNNN-feature-name/ or a domain folder for significant evolution, compatibility changes, migrations, or architecture replacement. Follow the group numbering in [conventions](conventions.md). The same file contains proposal, design, and later implementation evidence. Refine it for this change; later significant changes get new CHG IDs.

Describe before/after from evidence, motivation, scope, proportional approach, affected requirements, acceptance, and relevant migration/recovery risks. Preserve current approved requirements until the change is approved; then update affected clauses and link the change. Purely technical changes may leave requirements untouched.

A fix restoring expected behavior needs no prospective proposal. Its meaningful delivery history still uses a change record under [change records](change-records.md). Rejected/withdrawn proposals retain their rationale. Withdrawing approved work also requires an explicit disposition for affected requirements and any partial delivery; follow [the lifecycle rules](conventions.md#lifecycle-and-preservation).

## Proportional design

Initial substantial features use docs/architecture/NNNNN-feature-name-design.md linked to the requirement. Later changes include design in their CHG file. Do not invent a change proposal just to host an initial design.

Cover only relevant architecture/flows, contracts/data, reliability/security, trade-offs, verification/rollout, and open decisions. Preserve meaningful constraints and failure behavior while removing empty headings. Link source and accepted decisions rather than copying them.

Create an ADR only for a consequential durable choice. Preserve alternatives, rationale, consequences, revisit conditions, and approval. Supersede accepted decisions explicitly using the conventions; do not rewrite their reasoning.

After verification, link designs to current knowledge. Proposed architecture is not evidence of implemented behavior.
