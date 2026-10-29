# SWE lifecycle usage

Load [SKILL.md](SKILL.md) in an agent environment that supports Agent Skills, or install this directory using that environment's skill mechanism. The skill needs repository read/write access for local work, Python 3.9+ for validation, and connected GitHub tools or an authenticated CLI only for authorized remote operations. Its metadata uses the portable name/description convention already used by this repository; no vendor-specific tools are mandatory.

## Package

```text
swe-lifecycle/
├── SKILL.md
├── README.md
├── references/          # Eight flat, selectively loaded instruction files
├── assets/              # Fifteen adaptive Markdown templates
└── scripts/
    └── validate_docs.py
```

References separate lifecycle dispatch, conventions, specifications, GitHub work, implementation, current knowledge, historical changelogs, and validation. Load only those routed by the current operation. Templates are `project`, `requirement`, `change-proposal`, `technical-design`, `milestone`, `epic`, `feature-issue`, `bug-issue`, `chore-issue`, `adr`, `knowledge`, `changelog`, `architecture`, `development-guide`, and `pull-request` (all `.md` files under `assets/`).

## What is an ADR?

ADR stands for **Architecture Decision Record**. It documents an important architecture decision, the context and alternatives considered, and the consequences of the chosen approach so future readers can understand why it was made. Use the [ADR template](assets/adr.md) to create a decision record.

All lifecycle documents are written for human readers first, and agents use the same documents. Use natural, direct prose without AI-style boilerplate or em dashes. Explain unfamiliar abbreviations when readers need them, while keeping each document focused on its specific subject. See the [writing standard](references/conventions.md#writing-for-human-readers).

## Example requests

- “Bootstrap this Hono API Gateway. Prepare M0 Foundation and chore drafts; keep GitHub offline.”
- “Specify configurable rate limiting; clarify policy choices and prepare a design and implementation issues.”
- “Propose replacing better-auth with a Go service while retaining the authentication requirement.”
- “Fix the refresh-token race, verify the regression, synchronize knowledge, and record the change.”
- “Propose extending RBAC with ABAC; preserve approved behavior until the revision is authorized.”
- “Finalize this implementation: check acceptance criteria, documentation, history, and prepare the PR.”

All ten operations are available: `bootstrap`, `specify`, `propose-change`, `design`, `plan`, `implement`, `fix`, `sync-knowledge`, `record-change`, and `finalize`. One request can involve several operations. Bootstrap adds useful project navigation, a project brief, architecture/guides, or unpublished M0 drafts as the repository needs them; it does not create empty categories or invent feature specifications. For existing projects, inspect and preserve the established documentation first; agree on structural adoption rather than moving history automatically.

## Verification

From this repository:

```sh
python3 -m unittest discover -s evals/swe-lifecycle -p 'test_*.py' -v
python3 scripts/validate_skills.py
```

Against a target project, from any working directory:

```sh
python3 /absolute/path/to/swe-lifecycle/scripts/validate_docs.py /absolute/path/to/project
```

The target root must contain `docs/`. Errors include an offending path and repair guidance; invalid documentation returns exit code 1. The command reads documents without modifying them. [Conventions](references/conventions.md) defines schemas and numbering; [validation](references/validation.md) defines coverage. Empty category directories are not required; create them only when they contain documents.

The smoke tests exercise the validator and its CLI without GitHub calls. Separate paired runs evaluate lifecycle behavior against fixed repositories and identical authorization; see `evals/swe-lifecycle/README.md` in the source repository for fixture and grading instructions. Evaluation files are not included in skill installations.

## Design assessment and adoption limits

- Approval, current-state accuracy, meaningful acceptance criteria, actual tests, and truthful historical explanations require engineering review. A valid document is not proof of implementation. Trial the five workflow scenarios in disposable repositories before relying on autonomous execution.
- The YAML parser intentionally accepts a documented flat subset. It rejects advanced YAML instead of guessing. If a project needs complex metadata, adopt a maintained YAML parser and extend the schema/tests explicitly.
- Markdown checks cover common inline, image, reference, and heading links; they are not a complete CommonMark parser. Remote links are not fetched. Source paths are validated when expressed as Markdown links; prose paths and component names cannot always be resolved mechanically.
- Snapshot validation cannot establish past approval transitions, append-only history, deletion of tombstones, or whether allocation used the historical high-water mark. Gaps are legal. Inspect history during adoption and preserve retired identifiers. Resolve parallel-branch collisions by retaining established IDs and reallocating only a conflicting unpublished document with all references updated.
- GitHub authentication and available relationship features vary. Discover capabilities at runtime, prepare offline drafts when unavailable, and publish only within explicit authorization. Real remote mutation paths have not been integration-tested by this build.
- Templates deliberately retain a small set of required sections. Remove irrelevant optional sections and keep factual unknowns explicit. Review useful content and duplication manually; avoid turning minor edits into unnecessary ceremonies.
- Existing project layouts may fail the canonical validator. Agree on migration or adapt its contract locally after inspection; never repair failures by deleting or renumbering established records.

Before first real use, choose owners and approval authority, confirm changelog policy and required checks, reconcile existing identifiers and documentation, then perform a dry-run planning/finalization cycle. No automatic publication or deployment is part of installing this skill.
