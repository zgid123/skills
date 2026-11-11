# Tailwind CSS

## Canonical classes

Always follow `tailwindCSS.lint.suggestCanonicalClasses` for classes you create or modify. Fix the class spelling rather than disabling the diagnostic, lowering its severity, or adding a suppression. Keep cleanup within the requested scope.

1. Identify the installed Tailwind version and active project theme/configuration. Check the lockfile and CSS entrypoint as well as package declarations.
2. Use the project's IntelliSense/language-server suggestions when available. Canonicalization depends on the project design system; do not apply a universal replacement table from memory.
3. Apply suggested replacements while preserving variants, values, and intended rendering. If a suggestion appears incompatible, investigate version/configuration mismatches rather than blindly changing behavior or suppressing it.
4. Recheck affected classes through the available editor/language-server diagnostics. Run the project's normal build/lint checks as separate verification.
5. If diagnostics are unavailable, use version-matched official documentation and inspect the classes, then state that canonical-class diagnostics could not be verified. Do not claim zero warnings from a build or formatter alone.

The current IntelliSense implementation gates this diagnostic on Tailwind v4 and the design system's canonicalization capability. Do not upgrade a v3 project or introduce v4-only syntax merely to satisfy this rule. Consult current version-compatible guidance if tooling changes.

For example, when the project diagnostic recommends `print:flex`, apply that replacement rather than suppressing the warning. This illustrates equivalent canonical syntax, not a mandate to replace every arbitrary value.

```html
<!-- DO: use the suggested canonical class. -->
<div class="print:flex">Report</div>
```

```html
<!-- DON'T: retain a class flagged by the project's canonical diagnostic. -->
<div class="[@media_print]:[display:flex]">Report</div>
```

## Utilities and custom styles

- Follow [colors and themes](colors.md) for all color utilities: use `bg-primary`, `border-stroke-primary`, and `text-foreground-primary` for theme roles, or a named palette token for other colors. Never use raw hex or other literal color values in arbitrary utilities. Arbitrary non-color values remain allowed when needed; still use the canonical spelling supported by the project.
- Keep dynamically selected classes as complete literal strings in scanned source. Select between `bg-red-600` and `bg-green-600`; do not construct fragments such as `bg-${color}-600`. For truly runtime values, use a CSS custom property or inline style with an appropriate static utility.
- Follow existing class-composition and sorting tools. Reuse helpers already present; do not install one merely to join a few classes. Sorting is distinct from canonicalization.
- Prefer utilities in markup. Use `@apply` only when established project patterns or a concrete integration need justify it, following the installed version's stylesheet context requirements.
- Keep responsive, focus, and reduced-motion variants consistent with the shared CSS conventions. Do not add incompatible declarations and assume class-string order controls the CSS cascade.
- Follow the shared override procedure before considering important utilities. Do not use an important modifier or global important mode to avoid resolving layer order and selector specificity.

## Override example

Follow the [shared override procedure](../SKILL.md#override-procedure). Suppose a vendor stylesheet declares `.vendor-panel .button { color: var(--foreground-secondary); }`. Both declarations are normal author styles in the same cascade layer, and the local override is loaded afterward. An equally specific scoped selector then wins by source order:

```css
/* DO: scoped override loaded after the vendor rule in the same layer. */
.checkout .button {
  color: var(--foreground-primary);
}
```

```css
/* DON'T: use important for a conflict that normal cascade rules can solve. */
.button {
  color: var(--foreground-primary) !important;
}
```

This example assumes the button is inside both `.checkout` and `.vendor-panel`. Different layer precedence or an existing important declaration changes the solution. Important overrides remain a narrowly scoped, documented last resort; moving class names around in HTML does not change cascade priority.

## Sources

- [IntelliSense canonical-class diagnostic](https://github.com/tailwindlabs/tailwindcss-intellisense#tailwindcsslintsuggestcanonicalclasses)
- [Canonicalization implementation and version gate](https://github.com/tailwindlabs/tailwindcss-intellisense/blob/main/packages/tailwindcss-language-service/src/diagnostics/canonical-classes.ts)
- [Tailwind source detection and complete class names](https://tailwindcss.com/docs/detecting-classes-in-source-files)
