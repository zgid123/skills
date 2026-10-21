# CSS Formatting

## Purpose

Format CSS class rules inside Slidev Markdown `<style>` blocks so slide-specific styles remain easy to review and maintain.

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
