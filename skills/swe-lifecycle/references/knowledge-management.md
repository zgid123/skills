# Current implementation knowledge

Use the knowledge, architecture, or guide template for the artifact being updated. [Change records](change-records.md) own history; [conventions](conventions.md) own paths and metadata.

## Synchronize

1. Read existing knowledge and inspect relevant source, configuration, tests, interfaces, and migrations. Separate verified behavior from proposals and unknowns.
2. Update Overview, How it works, and Verification and limitations. Add configuration/operations detail when useful: relevant security, failures, recovery, diagnostics, and constraints. Link reproducible procedures in guides.
3. Record inspected source/test paths, verification date/scope, actual checks, and limitations. Test existence is not execution evidence. Mark verified only for supported claims; otherwise use draft and explicit unknowns.
4. Refresh system architecture and guides where affected. Architecture explains system-wide boundaries; domain knowledge explains capability behavior. Link requirements for intended behavior and ADR/change records for why it exists.
5. Validate links and navigation. Update incrementally as work completes; consolidate and review at milestone completion, not only at that point.

## Navigation and retrieval

Use docs/README.md as the entry point. When needed, specs/requirements/README.md indexes capabilities and links requirements, knowledge, tests, history, and GitHub work without duplicating task status. Domain indexes link focused topic pages. Add docs/glossary.md only for terms shared across domains; keep short definitions and link detailed explanations.

When answering project questions, use project.md for vision, requirements for expectations/stories, architecture for system structure, knowledge and source for actual behavior, change/ADR records for history/rationale, and guides/tests for verification. Cite the source, identify its status and relevant verification scope, and report contradictions or unknowns rather than guessing.

Keep one explanation per concept. Do not copy historical timelines into current knowledge or treat old designs as current implementation.
