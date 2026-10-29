# Durable implementation history

This reference owns completed historical records. It does not track in-progress work or describe the current system canonically. Read [conventions](conventions.md) for IDs, metadata, and finalization rules; load `../assets/changelog.md` when creating a record.

## Policy and placement

Default `docs/project.md` `changelog_policy` to `meaningful`: record each completed functional feature, significant defect fix, migration, and meaningful refactor. `every-issue` requires a record for every completed implementation issue. Trivial documentation/formatting work may skip a record under meaningful policy with an explicit reason in the completion handoff or PR. Do not create meaningless records to inflate coverage.

Use the affected requirement stream (`docs/changelog/00001-feature-name/`) when one exists, matching its five-digit REQ number. Use a domain stream such as `foundation/` or `infrastructure/` for work with no capability REQ. Each stream has its own four-digit sequence. For cross-domain work, choose one primary record and cross-link all affected requirements, components, and domains; create independent records only when they provide distinct useful history.

## record-change

1. Identify the completed work, affected domains, governing requirements/changes/ADRs, and verification evidence. Search existing changelogs by scope, issue/PR, components, and date to avoid duplicate descriptions of the same completed work.
2. Inspect code changes, tests, migrations, prior source, or reliable supplied context. Establish previous behavior only where evidence exists. State “Previous behavior not established” if needed; never infer history merely from a current implementation or issue title.
3. Allocate the next unused stream ID using all current records and `reserved_ids`. Create a draft record with accurate date, owner, change type, affected components, relationships, and available genuine GitHub/commit references. Leave unavailable external fields empty/null.
4. Explain what changed, why, previous behavior if established, new behavior, important implementation details, source paths, compatibility/migration impact, and verification. Keep Summary, Previous behavior, New behavior, Tests and verification, and Documentation updated nonempty. Record actual checks and limitations, not expected future outcomes. Link current source files relatively; for moved or deleted historical source, use a commit-pinned link when known or code-format the old path and state the available revision context. Never invent a commit or leave a knowingly broken source link.
5. Explain consequential technical choices concisely and link ADRs for full rationale. Include enough context for a future agent to answer historical questions without querying GitHub. External links supplement the record; they must not contain its only useful explanation.
6. Update current knowledge separately. Link the actual knowledge/architecture/guide changes, or give an evidence-based reason they were unnecessary. Finalize only once the record accurately describes completed, verified scope; partial or unverified records stay draft.
7. Preserve previous records. After finalization, add new records for later behavior changes. Make factual corrections only when explicitly identified with date, author, reason, and supporting evidence; retain enough original context to avoid rewriting history silently.

## Useful history versus notes

A durable record answers which behavior changed, which components implement it, why the change happened, how it was verified, and whether deployment or consumers were affected. It does not need an exhaustive list of edits, temporary debugging transcripts, fabricated root causes, or a copied PR conversation. Exact dates and change types enable chronological retrieval; requirement IDs and component paths support capability and technical-topic search.
