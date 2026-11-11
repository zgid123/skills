# Colors and themes

## Palette tokens

Always use named tokens for colors in CSS, CSS Modules, BEM styles, markup utilities, and inline styles. Raw hex, RGB, HSL, or OKLCH values belong only in the central palette definitions, not in component declarations or arbitrary utilities such as `bg-[#123456]`. Changing the color notation does not bypass this rule.

Consume the appropriate semantic token so changing a theme does not require editing component styles. Assuming the token is defined centrally:

```css
/* DO: text consumes the foreground role. */
.card {
  color: var(--foreground-primary);
}
```

```css
/* DON'T: a component hardcodes its text color. */
.card {
  color: #171717;
}
```

Reuse existing palette tokens first. When creating a palette for a new color family, generate a Tailwind-style scale named `<color>-50`, then `<color>-100` through `<color>-900` in steps of 100, and `<color>-950`: eleven stops from light to dark. Use a descriptive family name such as `ocean` or `amber`. Preserve supplied brand colors and choose harmonious shades; do not assume equal numeric steps guarantee perceptually even differences or accessible contrast. Reuse Tailwind's existing scale when it fits instead of recreating it.

Define palette values once in the project's central token mechanism. Semantic theme tokens reference those palette tokens. When adding a genuinely new family, provide its full scale; do not generate unused families or rebuild an existing palette for a small component change. `transparent`, `currentColor`, and inheritance may express transparency or inherited color without introducing a new literal hue.

## Theme roles

Themes normally have three roles: primary, secondary, and tertiary. Use these exact semantic token names for their intended properties:

| Property | Primary | Secondary | Tertiary |
| --- | --- | --- | --- |
| Background color | `primary` | `secondary` | `tertiary` |
| Border color | `stroke-primary` | `stroke-secondary` | `stroke-tertiary` |
| Text color | `foreground-primary` | `foreground-secondary` | `foreground-tertiary` |

These are nine semantic tokens, not three raw values reused for every property. Select the palette shade appropriate for each role and contrast requirement. Keep background, border, and foreground values independently configurable. Do not use `primary` directly as a text or border token, or interpret `stroke-primary` as the text color.

For a color outside these roles, use its own named palette token, such as `amber-600` or `ocean-700`, rather than forcing it into primary/secondary/tertiary or writing a literal value. Theme modes, when required, remap semantic tokens centrally while component styles keep the same token names. Do not add extra modes unless requested or already present.

In plain CSS, assuming the central palette already defines the referenced neutral scale:

```css
:root {
  --primary: var(--color-neutral-50);
  --secondary: var(--color-neutral-100);
  --tertiary: var(--color-neutral-200);
  --stroke-primary: var(--color-neutral-300);
  --stroke-secondary: var(--color-neutral-400);
  --stroke-tertiary: var(--color-neutral-500);
  --foreground-primary: var(--color-neutral-950);
  --foreground-secondary: var(--color-neutral-900);
  --foreground-tertiary: var(--color-neutral-800);
}

.card {
  background-color: var(--primary);
  border: 1px solid var(--stroke-primary);
  color: var(--foreground-primary);
}
```

This illustrates token wiring, not a universally approved palette. Check actual text/background and required non-text contrast for the chosen values and states. Follow existing variable prefixes while retaining the role meanings; do not rename unrelated framework tokens or generated components.

## Tailwind integration

Expose the semantic tokens through the installed Tailwind version's theme mechanism. For v4, the `--color-*` namespace produces color utilities. When aliasing separate runtime theme variables, use `@theme inline` so utilities resolve the variables at their usage scope:

```css
@theme inline {
  --color-primary: var(--primary);
  --color-secondary: var(--secondary);
  --color-tertiary: var(--tertiary);
  --color-stroke-primary: var(--stroke-primary);
  --color-stroke-secondary: var(--stroke-secondary);
  --color-stroke-tertiary: var(--stroke-tertiary);
  --color-foreground-primary: var(--foreground-primary);
  --color-foreground-secondary: var(--foreground-secondary);
  --color-foreground-tertiary: var(--foreground-tertiary);
}
```

Use `bg-primary`, `border-stroke-primary`, and `text-foreground-primary`, and the corresponding secondary/tertiary utilities. `stroke-primary` is the semantic border token; Tailwind's literal `stroke-*` utility controls SVG stroke and is not a CSS border utility. For colors outside the three theme roles, use named utilities such as `bg-amber-600` or `text-ocean-700` when those palette entries exist.

For v3, expose equivalent names in the existing Tailwind color configuration instead of introducing v4 directives. Keep complete class literals and follow `suggestCanonicalClasses`; do not replace a token with a raw color to silence a diagnostic.

Sources: [Tailwind color scales](https://tailwindcss.com/docs/colors) and [theme variables and aliases](https://tailwindcss.com/docs/theme).
