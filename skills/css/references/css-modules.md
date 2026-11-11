# CSS Modules

Preserve the project's module tooling and import conventions. By default, colocate a `*.module.css` stylesheet with its consuming component, following the component's existing filename convention. Do not add a module loader when the framework already supports modules.

## Local names and scope

- Use simple camelCase local names such as `root`, `title`, `action`, and `isActive`. Local scoping removes the need for a globally unique component prefix.
- BEM is optional inside CSS Modules. Preserve an established BEM convention or use it when requested; do not require or prohibit it because the stylesheet is a module.
- Access exported names through the imported module mapping. Simple names use `styles.title`; BEM names can use `styles['product-card__title']`. Do not assume the build exports camelCase aliases for hyphenated keys.
- Combine base and state classes with the project's existing composition pattern. A modifier supplements rather than replaces the base styles.
- Keep component styles local. Use `:global` only for deliberate integration overrides, scoped beneath a local wrapper where possible. Do not globally redefine generic tags or shared classes to work around module isolation.
- Reuse shared design tokens through the project's existing mechanism. Do not duplicate a global reset or token system inside each module.

For a local `title` class, use the module export rather than the literal string `title` in markup. When BEM is selected, the exported key retains its BEM name while the generated runtime class remains locally scoped. Both naming choices are valid.

## Scoped integration example

When a vendor label is rendered inside this component's local `root`, anchor the override to that root so other instances keep their own styling. Assume the foreground token is defined centrally:

```css
/* DO: only vendor labels inside this module's root are affected. */
.root :global(.vendor-label) {
  color: var(--foreground-secondary);
}
```

```css
/* DON'T: unintentionally override every vendor label in the application. */
:global(.vendor-label) {
  color: var(--foreground-secondary);
}
```

The scoped selector requires a descendant relationship; it will not reach a label rendered through a portal outside the root. Use the integration's supported styling hook in that case.

Verify that imports resolve, referenced keys exist, and styles do not leak to neighboring components. Use the project's build/type tooling where available; do not assert generated class hashes in tests.

Source: [CSS Modules documentation](https://github.com/css-modules/css-modules).
