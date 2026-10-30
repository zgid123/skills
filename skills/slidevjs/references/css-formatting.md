# CSS Formatting

## Purpose

Format CSS class rules inside Slidev Markdown `<style>` blocks so slide-specific styles remain easy to review and maintain.

## Theme defaults first

The theme and addon styles are the default look of every deck. Use them as provided: pick a layout, set supported frontmatter such as `background`, and use addon components before writing any CSS. Never override theme or addon styles without the user's explicit permission. If the defaults cannot produce the requested result, stop and ask, explaining which theme style you would change and why; apply the override only after the user approves it.

Without permission, do not:

- Target theme or addon selectors, such as `.alpha-*` layout classes, `.slidev-layout`, or component classes, in a `<style>` block, `style.css`, `styles/`, `uno.config`, or inline `style` attribute.
- Redefine theme CSS variables, fonts, colors, spacing, or backgrounds globally.
- Use `!important`, or add lint suppressions such as `biome-ignore lint/complexity/noImportantStyles`, to win against theme styles.
- Reapply an asset through CSS when a frontmatter property already sets it, for example overriding a layout's `background-image` instead of setting `background: ./assets/main.png`.

```css
/* ❌ Overrides theme layouts without permission */
.alpha-academic-cover {
  background-image: url('./assets/main.png') !important;
}
```

Slide-local classes for the task's own content elements are allowed when no layout or component provides the needed arrangement; they must not change theme-owned elements.

## ✅ Do

- Write every class rule as multiline CSS, with the opening brace on the selector line and the closing brace on its own line.
- Write one declaration per line, with a space after the property colon and a trailing semicolon.
- Use consistent indentation. Follow the deck's existing convention; use two spaces when none exists.
- Separate rules with a blank line.

```md
<style>
.slide-title {
  font-size: 2rem;
  font-weight: 700;
}

.slide-content {
  line-height: 1.5;
}
</style>
```

## ❌ Do not

- Compress class rules onto a single line.
- Put multiple declarations on the same line or omit declaration spacing and semicolons.
- Mix indentation styles or run adjacent rules together without a blank line.

```md
<style>
.slide-title { font-size:2rem; font-weight:700 }
.slide-content { line-height:1.5 }
</style>
```

## Verification

Before finishing, inspect every Markdown `<style>` block created or edited by the task. Confirm its class rules use multiline declarations, consistent indentation, property spacing, trailing semicolons, and blank lines between rules.

Search the deck's styles for theme or addon selectors, `!important`, and style-related lint suppressions. Confirm none were added without the user's explicit permission.
