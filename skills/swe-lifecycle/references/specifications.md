# Specifications and design

This reference owns discovery, behavior approval, change scoping, and design. Read [conventions](conventions.md) before allocating identifiers or changing lifecycle status. Load only the relevant requirement, change-proposal, technical-design, or ADR template from `../assets/`.

## Discover and specify

1. Inspect existing requirements, related knowledge, architecture, and relevant source. Reuse a capability's stable requirement when extending or replacing its implementation. Identify what the request actually authorizes and what still needs a decision.
2. If an available `grill-me` skill is suitable, read and use it for ambiguous requirements. Do not recreate it. Otherwise ask focused questions about actors, problem, observable outcomes, non-goals, business rules, constraints, failure cases, security, and acceptance. Infer routine choices from existing conventions and continue independent work while clarification is pending.
3. Draft implementation-independent behavior, unless technology is an explicit constraint. Separate goals from proposed solutions. Write stable `FR-001`, `NFR-001`, and `AC-001` clauses; acceptance criteria specify observable inputs, outcomes, and failure conditions. State measurable limits and assumptions instead of vague adjectives.
4. Keep Overview, Functional requirements, and Acceptance criteria nonempty. Include problem, goals, non-goals, actors, business rules, scenarios, constraints, and open questions where relevant. Explicitly state uncertainty; do not turn guesses into approved behavior.
5. Cross-link dependencies and supporting documents. Check that acceptance criteria cover relevant requirements and edge cases. Seek owner approval for significant behavior decisions and mark approved only when authorization covers that content.

An approved requirement is living expected behavior. Preserve stable clause identifiers and keep a short evolution note linking the change that authorized a revision; Git and associated changelogs preserve the historical implementation. Do not rewrite an approved document to match accidental implementation drift.

## Propose a significant change

Use a proposal for substantial behavior evolution, architecture replacement, compatibility changes, or migration. Small fixes restoring expected behavior and routine implementation details generally need no proposal.

1. Describe current behavior from evidence, proposed behavior, motivation, scope, affected requirements, risks, compatibility, migration, and rollback where applicable. Keep Summary, Current behavior, Proposed behavior, and Acceptance criteria nonempty. If current behavior is unknown, state that and identify how it will be established.
2. Classify impacts: behavior, implementation, architecture, or a combination. A provider replacement may retain existing REQ acceptance criteria while materially changing architecture and migration risk. Do not invent a new authentication requirement solely to replace a library with a service.
3. Link existing requirements and draft proposed amendments separately from their approved text. Record explicit approval before applying significant behavior or architecture changes. Preserve rejected and withdrawn proposals as decisions, not unexplained deletions.
4. Mark implementing only when implementation starts; mark implemented only after all scoped acceptance and documentation obligations are met. Partial delivery remains implementing or is explicitly rescoped with approval.

## Design proportional to risk

Ground design in approved scope, existing architecture, and verified implementation constraints. Use `design.md` beside a change proposal, or `docs/architecture/NNNNN-feature-name-design.md` linked directly to the initial requirement. A new feature does not need a fictitious migration proposal to justify design.

Cover architecture, components, data flow, interfaces, storage, consistency, security, reliability, observability, testing, deployment, and rollback only to the extent the work requires. Explain alternatives and trade-offs for meaningful choices. Link detailed decisions rather than copying them. Identify unvalidated assumptions and experiments; proposed designs do not describe the verified current system until implemented.

Use an ADR for consequential, durable architecture decisions, rather than each implementation preference. Include context, drivers, considered options, decision, consequences, revisit conditions, and supersession links. Obtain approval for significant architecture changes. While a replacement ADR is proposed, link the accepted predecessor in prose and keep supersession metadata empty. Once the successor is accepted, update both records' reciprocal metadata and the predecessor status together. Preserve the original rationale. Synchronize the current architecture overview only after implementation is verified.

## Examples

- Configurable gateway rate limiting: create a capability REQ, define configuration and rejection behavior, and design storage/concurrency if needed. Plan issues; add knowledge and history after implementation.
- Authentication migration: inspect and reuse the existing authentication REQ, create CHG and design for the replacement, record consequential ADRs, and plan compatibility, data migration, rollback, and verification.
- RBAC extended with ABAC: inspect the authorization REQ, propose the substantial evolution, draft revised/new clauses only where capability boundaries justify them, and preserve approved behavior until the revision is authorized.
