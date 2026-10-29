# Current implementation knowledge

This reference owns verified current-state documentation. Use [changelog management](changelog-management.md) for historical changes and [conventions](conventions.md) for metadata and paths. Load the knowledge, architecture, or development-guide template only for the artifact being updated.

## Organize for retrieval

Group knowledge by domain/capability, with a useful `README.md` and focused topic pages where needed. Give each structured page a stable `KNW-domain-topic` ID, meaningful title, owner, dates, status, requirement/decision relationships, and affected components. Add relative links from `docs/README.md` and domain indexes so humans and future agents can discover the content.

Use requirement IDs, technical topic names, component paths, and cross-links consistently. Keep one canonical explanation for each concept and link to it rather than repeating whole sections. Source paths should be useful evidence, not massive code dumps. No vector database or RAG pipeline is required to make local Markdown searchable.

## sync-knowledge

1. Read relevant existing knowledge and inspect the current implementation, configuration, tests, interfaces, and migrations. Identify what is actually verified and what remains uncertain.
2. Compare documentation claims with code. Update substantive differences, remove obsolete current-state claims, and preserve user-written explanations that still apply. A proposed design does not establish implemented behavior.
3. Explain current behavior, important components, APIs/interfaces, data flow, storage/algorithms, configuration, dependencies, operational constraints, security, failure behavior, observability, test references, and limitations where relevant. Keep Overview, Current implementation, and Known limitations nonempty; state “No additional limitations established by this review” only if that is truthful, rather than claiming no limitations exist.
4. Record verification evidence in Current implementation or the appropriate section: inspected source/test paths and checks actually run. Set `verified` only for supported claims; use `draft` and explicit unknowns otherwise. Update `updated_at` after substantive changes.
5. Refresh architecture overviews and reproducible development/operations guides where affected. Link requirements, ADRs, designs, and historical records instead of copying their purpose into knowledge.
6. Validate references, links, metadata, and navigation. Summarize gaps discovered, including contradictory requirements needing approval or code investigation.

Keep behavior changes and historical explanations in changelog, not as an ever-growing timeline inside current knowledge. A short link explaining why a current constraint exists may point to its ADR or historical record. Neither old changelogs nor accepted ADRs should be rewritten merely to describe the latest implementation.

## Knowledge quality

Prefer precise statements such as “the refresh endpoint consumes tokens through this transaction” backed by a source link. Avoid unsupported claims like “fully secure” or “all tests passed.” Describe limitations in terms useful for development and operation. Reproducible guide commands must match actual project tooling; document environment assumptions and avoid including secrets.
