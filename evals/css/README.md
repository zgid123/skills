# CSS evaluations

The five cases in `evals.json` check canonical Tailwind suggestions and version boundaries, BEM element/modifier naming, CSS Modules with and without optional BEM, palette/theme token mappings, and scoped cascade overrides with last-resort important handling. Inputs are self-contained; no fixture project is required.

Run each prompt with the CSS skill and compare with a baseline that has not read it. Review the produced answers against `expectations`; save generated outputs outside the installable skill directory. These focused scenarios check instruction-following, not a real application's rendered appearance or live IntelliSense integration. Several prompts explicitly state the desired behavior, so a strong baseline may pass them too; passing does not establish a measured improvement over the baseline.

Run `python3 scripts/validate_skills.py` from the repository root to check metadata, links, and evaluation structure. This validator does not execute the behavioral scenarios. When evaluating real UI work, separately run the target project's checks and inspect available editor diagnostics and rendered states.
