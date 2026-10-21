# HTML Spacing

## Purpose

Keep HTML spacing intentional inside Slidev Markdown. Blank lines can affect how mixed HTML and Markdown render: unnecessary blank lines can cause incorrect output, while some content needs a blank line to appear correctly.

## ✅ Do

- Keep adjacent HTML elements together by default, without extra blank lines between them.
- Preserve or add blank lines when the specific content needs them to render correctly, including boundaries between HTML and Markdown.
- Check the affected slide in preview after changing spacing. Confirm all intended content appears and the layout remains correct.

Prefer this spacing between adjacent elements:

```html
<p>First paragraph.</p>
<p>Second paragraph.</p>
```

## ❌ Do not

- Insert blank lines between every HTML element just for source readability.
- Remove every blank line mechanically; preserve those needed for correct rendering.
- Let formatting changes override spacing verified in Slidev preview.

Avoid this spacing unless the slide needs the blank line to render correctly:

```html
<p>First paragraph.</p>

<p>Second paragraph.</p>
```

## Verification

Inspect HTML spacing in the Markdown edited by the task and preview the affected slides. If content disappears or renders incorrectly, adjust blank lines at the relevant HTML and Markdown boundaries and check again. Keep the spacing that renders the content correctly. If preview is unavailable, report that limitation instead of claiming the rendering was verified.
