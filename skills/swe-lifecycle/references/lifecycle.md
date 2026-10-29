# Lifecycle operations

Use this reference to choose scope and the next operation. Naming and state rules live in [conventions](conventions.md); content discovery lives in [specifications](specifications.md). A solo developer may own and approve documents; an agent's draft does not approve itself.

## Inspect before initializing

Read instructions, project documentation, repository state, and relevant code before editing. Identify the current documentation convention, owners, actual implementation, active work, and explicit authorization. Preserve user-written content. If an existing layout differs, map its responsibilities and preserve it for ordinary scoped work. Treat migration to the canonical layout as separate work requiring approval; report incompatibilities without silently moving history.

## bootstrap

1. Inspect runtime, tooling, repository layout, and stated project objective. Separate established facts from choices needing confirmation.
2. Add a documentation index or project brief when it helps people navigate or maintain the repository. Use the canonical locations when creating a category, but create a directory only when it contains useful work. Do not create empty folders or `.gitkeep` files just to satisfy the validator.
3. Document architecture and reproducible development procedures only when they help the current project or requested work. Mark unimplemented architecture as proposed until verified.
4. Plan `M0 Foundation` and actionable chore issues for repository setup, runtime, configuration, CI, basic tests, and operational foundations only where actually needed. Read [GitHub workflow](github-workflow.md) before managing remote items.
5. Validate any canonical documents created, report drafts versus published items, and identify unresolved technical choices. Create requirement specs only if meaningful system behavior is being defined. A small repository may need only a project brief or index; a Hono API Gateway bootstrap need not invent authentication or rate-limiting requirements.

## specify, propose-change, design

Use [specifications](specifications.md). Discover behavior and approval first, then design. Requirement IDs survive implementation replacement. Initial capabilities may have standalone designs without migration proposals. Material evolution of approved behavior needs a change record and approval before the approved requirement changes.

## plan

Use [GitHub workflow](github-workflow.md). Map approved scope and accepted design into delivery objectives and verifiable work. Milestones and requirements are many-to-many. Use epics only when grouping helps. Resolve consequential open design decisions before presenting implementation as ready.

## implement and fix

Use [implementation](implementation.md). Inspect requirement, design, knowledge, and issue context; implement within approved boundaries and verify. For a defect, reproduce and investigate before asserting a cause. Do not create requirement/change records solely because an issue is a bug.

## sync-knowledge and record-change

Use [knowledge management](knowledge-management.md) to update current implementation descriptions and [changelog management](changelog-management.md) to preserve completed history. One does not replace the other. Perform these after evidence establishes the implementation; draft notes remain clearly unverified.

## finalize

Apply the Definition of Done in [implementation](implementation.md). Run the canonical validator only when the project has adopted the canonical layout; otherwise use established project checks and review affected documentation and references. Leave unmet criteria and unavailable checks explicit. Do not close remote work unless authorized and actually complete. A partially implemented proposal remains implementing even if its documentation passes validation.
