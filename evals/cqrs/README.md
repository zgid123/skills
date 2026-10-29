# CQRS behavioral evaluations

Copy the contents of `fixtures/project/` into a fresh disposable directory for each case and configuration; never run an agent against the canonical fixture. Paths in `evals.json` are relative to this evaluation directory. Keep the same revised prompt, fixture, tools, and authorization in both runs; compare the revised skill with a pre-change snapshot. Preserve existing case IDs and grade every expectation against generated files and actual command output.

Use Node.js 24 or newer. In the disposable directory run `pnpm install --ignore-scripts`, then `pnpm check` and `pnpm test`. Dependencies are pinned in the fixture; installing them does not add dependencies to the skills repository. A runner may install once per fixture, then copy the installed tree into isolated run directories. Treat missing tools or installation failures as unverified checks, never as passes.

The compiler extends `@alphacifer/tsconfig/base`; its local overrides select the fixture environment and JSX transform. Existing tests protect baseline behavior; new functionality requires focused behavior coverage. Compiler success does not establish compliance with style and placement expectations, which require code inspection.

The fixture installs the actual @cqrsx/core package. Inspect its declarations instead of inventing a bus shim. Existing domain guards intentionally reject shipped-order cancellation.
