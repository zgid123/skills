# <Capability or change>: technical design

Owner: <Person or accountable role> · State: <proposed/approved> · Updated: <YYYY-MM-DD>

Source: <Relative link to an existing requirement or change proposal. Initial capabilities may link directly to a requirement.>

<!-- Keep only sections that resolve real technical questions. Describe a proposed approach; verified current behavior belongs in knowledge. Record approval evidence for significant architecture changes. -->

## Scope and constraints

<Requirements and AC identifiers addressed, exclusions, and constraints.>

## Architecture

<System boundaries, dependency direction, and deployment context. Include a small diagram only if useful.>

## Components

<Responsibilities, interfaces, and affected source paths. Prefer existing components.>

## Data flows

<Request/event path, transformations, and failure paths.>

## APIs and interfaces

<Contracts, validation, authentication/authorization, errors, and compatibility.>

## Data and storage

<Data model, retention, indexes, migration requirements, and ownership.>

## Concurrency and consistency

<Invariants, transactions, ordering, races, idempotency, and retry semantics.>

## Security and reliability

<Trust boundaries, secrets, failure modes, recovery, and applicable quality targets.>

## Alternatives and trade-offs

<Credible options, chosen approach, and consequences. Link an ADR for durable significant decisions.>

## Observability

<Signals, diagnostic context, sensitive-data handling, and actionable alerts.>

## Testing

<Verification mapped to requirement AC identifiers; appropriate test layers and migration/failure checks.>

## Deployment and rollback

<Release order, configuration, health checks, rollback triggers, data compatibility, and recovery limits.>

## Open questions and approval

<Outstanding decisions; approver, date, exact scope, and evidence of approval when obtained.>
