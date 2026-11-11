---
name: css
description: Apply Alpha's CSS conventions when writing, editing, reviewing, or debugging styles, color palettes, theme tokens, responsive layouts, Tailwind utility classes, suggestCanonicalClasses diagnostics, BEM names, or CSS Modules (*.module.css). Use for styling changes in markup and components even when no CSS file changes. Require token-based colors and role-based themes, follow project-aware canonical Tailwind classes, avoid important overrides, and treat BEM and CSS Modules as independent, optionally combined approaches.
---

# CSS

## Start with the project

Inspect nearby styles, component structure, package versions, theme tokens, and existing build/lint configuration before changing styles. Preserve the project's styling approach and naming conventions; prefer Tailwind for a new project with no established approach unless the user chooses otherwise. Do not migrate styles or add styling dependencies just to apply this skill.

BEM is a naming methodology; CSS Modules provide local scoping. Neither requires the other. Do not impose BEM on global CSS or CSS Modules merely because they contain handwritten classes. Combining BEM and CSS Modules is optional.

Read only the relevant references:

| Work | Reference |
| --- | --- |
| Color declarations, palettes, or theme creation | [Colors and themes](references/colors.md) |
| Tailwind classes, variants, arbitrary values, or canonical-class diagnostics | [Tailwind](references/tailwind.md) |
| BEM naming or BEM-based styles | [BEM](references/bem.md) |
| Local stylesheet modules and their imports | [CSS Modules](references/css-modules.md) |

Read both BEM and CSS Modules references when the project combines them. Apply the host language/framework skill when editing components. Preserve generated-component and framework-specific styling boundaries already defined by the project.

## Shared conventions

- Always consume colors through tokens, never direct hex codes or other literal color values in component styles, inline styles, or arbitrary utilities. Define raw color values only in the central palette. Follow [colors and themes](references/colors.md) for Tailwind-style scales and background/border/text role mappings; one-off colors still require a named token.
- Reuse existing design tokens for spacing, typography, radii, and breakpoints. Add non-color tokens only for a real shared design need; keep legitimate one-off non-color values local.
- Keep selectors shallow and specificity low by default. For overrides, first inspect the winning declaration and fix cascade layer or stylesheet order, then use the smallest scoped increase in selector specificity needed. Do not use `!important` unless these approaches cannot solve the conflict; explain the concrete constraint and scope that last-resort exception narrowly. Reordering HTML classes or adding tag selectors does not necessarily win the cascade; see the override procedure below.
- Use flexible layouts and content-driven sizing. Follow existing responsive breakpoints; check narrow and wide layouts, long content, and overflow rather than assuming a fixed screen size.
- Preserve visible keyboard focus. Do not remove outlines without an accessible replacement, and do not make essential interactions depend only on hover or color.
- Respect `prefers-reduced-motion` when adding nonessential animation or transitions. Keep information and controls usable when motion is reduced.
- Keep changes scoped to the requested styles and states. Avoid unrelated formatting, selector renames, or speculative utility abstractions.

## Verification

Run relevant existing formatting, lint, and build checks. For rendered UI changes, inspect affected viewport sizes and interactive states when a preview is available, including keyboard focus and reduced motion when applicable. Do not add tests that merely repeat declarations.

For Tailwind, follow the canonical-class verification procedure in its reference. Report which checks ran and any unavailable editor or visual verification; a successful build alone does not prove that canonical-class diagnostics are clear.

## Override procedure

1. Inspect the conflicting property, selector, origin, cascade layer, specificity, and source order, including inline styles and existing important declarations.
2. Prefer the component's supported theme/token or variant API, or correct the original rule when owned by the project. Otherwise place the override in the appropriate layer and stylesheet position. Later source order wins only when earlier cascade criteria tie.
3. If necessary, add a meaningful scoped selector such as `.checkout .action` instead of an unrelated ID, repeated selector, or long tag chain. Specificity cannot overcome a higher-priority cascade layer or an important declaration by itself.
4. Use `!important` only as a documented last resort for an actual constraint, such as an immutable third-party important declaration. Verify the resulting cascade; do not enable blanket important mode or use important utilities as the default fix.

Reference: [CSS specificity and cascade precedence](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity).
