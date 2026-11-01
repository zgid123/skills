# HTML Formatting and Spacing

## Purpose

Keep HTML inside Slidev Markdown readable and intentionally spaced. The Markdown formatter (oxfmt or Prettier) treats raw HTML blocks as opaque and prints them verbatim, so it never fixes compressed markup; the author must format it by hand. Blank lines also affect how mixed HTML and Markdown render: unnecessary blank lines can cause incorrect output, while some content needs a blank line to appear correctly.

## Formatting

### ✅ Do

- Put each block-level element on its own line, such as `div`, `section`, `ul`, `li`, `h1`–`h6`, `p`, `img`, and addon components.
- Indent children one level deeper than their parent. Follow the deck's existing indentation; use two spaces when none exists.
- Put the opening and closing tags of a container on their own lines.
- Keep a leaf element whose content is short text on one line, for example `<h3>Title</h3>` or `<span class="eyebrow">Label</span>`.
- Keep inline elements that sit inside running text, such as `<strong>`, `<em>`, `<code>`, `<br>`, or a highlight `<span>`, inline within that text.

```html
<div v-click class="intro-definitions">
  <div class="definition">
    <span class="eyebrow">Challenge</span>
    <h3>Open questions, many solutions</h3>
    <p>Methods, parameters, and rounding can produce <strong>different answers</strong>.</p>
  </div>
</div>
```

### ❌ Do not

- Chain sibling or nested block elements on one line.
- Leave nested containers unindented or mix indentation styles.
- Rely on the formatter to reflow HTML; it will not.

```html
<div v-click class="intro-definitions">
  <div class="definition"><span class="eyebrow">Challenge</span><h3>Open questions, many solutions</h3><p>Methods, parameters, and rounding can produce different answers.</p></div>
</div>
```

### Exceptions

Do not reflow content where whitespace or line structure is meaningful. Leave these as written:

- Mermaid, PlantUML, and other diagram blocks, plus fenced code blocks and their contents.
- Existing `<pre>` blocks the task does not convert, `<textarea>`, and KaTeX/LaTeX math.
- Inline elements inside a sentence, where adding a line break would insert visible whitespace between words or punctuation.
- Markup where the slide preview shows that the added whitespace changes the layout, such as `inline` or `inline-block` siblings meant to touch. Keep the minimal layout that renders correctly.

## Code blocks

Show code with a Markdown fenced code block and a language tag, so Slidev highlights it with Shiki. Do not write code samples as raw HTML such as `<pre><code>`; it bypasses Shiki and loses highlighting, line highlighting, and theme styling. Inline `<code>` inside running text is fine.

### ✅ Do

````md
```python
import pandas as pd

df = pd.read_csv('/mnt/test_ave.csv')
df['FamilySize'] = df['SibSp'] + df['Parch']
r = df['FamilySize'].corr(df['Fare'], method='pearson')
print(r)
```
````

Use Slidev's Shiki features on the fence when they help, such as line highlighting (`` ```python {2,4} ``) or click-stepped highlighting (`` ```python {1|3-4|all} ``). See the [Slidev code block syntax](https://sli.dev/guide/syntax#code-blocks).

### ❌ Do not

```html
<pre class="pearson-code"><code>import pandas as pd

df = pd.read_csv('/mnt/test_ave.csv')
print(df.head())</code></pre>
```

When a code block sits inside an HTML container, leave a blank line before and after the fence so Slidev parses it as Markdown. When a component needs code styling, style the Shiki output through the container class instead of rebuilding the block in HTML, following [CSS Formatting](./css-formatting.md).

## Spacing

### ✅ Do

- Keep adjacent HTML elements together by default, without extra blank lines between them.
- Preserve or add blank lines when the specific content needs them to render correctly, including boundaries between HTML and Markdown.
- Check the affected slide in preview after changing spacing. Confirm all intended content appears and the layout remains correct.

Prefer this spacing between adjacent elements:

```html
<p>First paragraph.</p>
<p>Second paragraph.</p>
```

### ❌ Do not

- Insert blank lines between every HTML element just for source readability. Inside an HTML block, a blank line ends the block and the rest may render as Markdown or code.
- Remove every blank line mechanically; preserve those needed for correct rendering.
- Let formatting changes override spacing verified in Slidev preview.

Avoid this spacing unless the slide needs the blank line to render correctly:

```html
<p>First paragraph.</p>

<p>Second paragraph.</p>
```

## Verification

Inspect the HTML in the Markdown edited by the task. Confirm block elements sit on their own indented lines, short leaf and inline elements stay on one line, and the exceptions above were left untouched. Run the repository's formatter and confirm it leaves the HTML unchanged.

Preview the affected slides. If content disappears or renders incorrectly, adjust blank lines at the relevant HTML and Markdown boundaries and check again. Keep the spacing that renders the content correctly. If preview is unavailable, report that limitation instead of claiming the rendering was verified.
