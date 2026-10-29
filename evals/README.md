# Skill evaluations

Repository-only evaluation cases, fixtures, and test helpers live in `evals/<skill-name>/`. Installable instructions and runtime resources live in `skills/<skill-name>/`, so installing a skill does not copy its evaluation files.

Each `evals.json` uses fixture paths relative to its containing evaluation directory. Copy fixtures into disposable workspaces before running behavioral evaluations. Keep generated results outside the installable skill packages.

Run `python3 scripts/validate_skills.py` from the repository root to validate skill metadata, evaluation cases, fixture paths, and documentation links. Individual evaluation READMEs describe their additional checks.
