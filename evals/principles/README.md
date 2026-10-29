# Principles behavioral evaluations

Copy the contents of `fixtures/project/` into a fresh disposable directory for each case and configuration; never run an agent against the canonical fixture. Paths in `evals.json` are relative to this evaluation directory. Keep the same revised prompt, fixture, tools, and authorization in both runs; compare the revised skill with a pre-change snapshot. Preserve existing case IDs and grade every expectation against generated files and actual command output.

Use Node.js 24 or newer and run `node --test`. No installation is required. The original tests protect existing behavior; each implementation task must add regression coverage for its requested change. The parser null crash and category space bug are intentional input defects; baseline tests pass before either change.
