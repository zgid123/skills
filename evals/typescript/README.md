# TypeScript behavioral evaluations

Copy the contents of `fixtures/project/` into a fresh disposable directory for each case and configuration; never run an agent against the canonical fixture. Paths in `evals.json` are relative to this evaluation directory. Keep the same revised prompt, fixture, tools, and authorization in both runs; compare the revised skill with a pre-change snapshot. Preserve existing case IDs and grade every expectation against generated files and actual command output.

Use Node.js 24 or newer. In the disposable directory run `pnpm install --ignore-scripts`, then `pnpm check` and `pnpm test`. Dependencies are pinned in the fixture; installing them does not add dependencies to the skills repository. A runner may install once per fixture, then copy the installed tree into isolated run directories. Treat missing tools or installation failures as unverified checks, never as passes.

The compiler extends `@alphacifer/tsconfig/base`; its local overrides select the fixture environment and JSX transform. Existing tests protect baseline behavior; new functionality requires focused behavior coverage. Compiler success does not establish compliance with style and placement expectations, which require code inspection.

The workspace includes `packages/users`; the root already supplies lodash-es. The compressed profile implementation is an intentional style fixture, and profile filtering is an implementation task. EventListenerObject comes from TypeScript’s DOM library and EventTarget is available in Node.js 24.

Case 5 separately exercises existing guard clauses through a formatting-only task. Case 3 can legitimately filter profiles without a conditional statement, so its conditional-style expectation alone does not establish brace-rule coverage. The label fixture's compressed guards are intentional; its baseline tests already pass.
