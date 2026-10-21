# Deck Structure

## Purpose

Use the required section-based structure and templates when creating, extending, or reorganizing a Slidev deck.

## Required structure

Use this structure for every new deck:

```text
assets/
├── heading.png
└── main.png
pages/
└── <section>/
    ├── main.md
    ├── 01-<article-1>.md
    ├── 02-<article-2>.md
    └── 0N-<article-N>.md
slides.md
```

Use descriptive kebab-case names for section directories and article filename suffixes unless the surrounding project already has a different convention. Number articles in presentation order with zero-padded prefixes.

Keep `assets/main.png` and `assets/heading.png` when they already exist or are supplied by the user. For each missing file, copy the corresponding bundled default from this skill's `assets/` directory into the deck's `assets/` directory. Never replace an existing deck asset with the bundled default unless the user explicitly asks for that replacement.

## Root deck template

Use this as the default `slides.md`. Replace placeholders with the presentation's actual title, timing, presenter information, date, and section names. Repeat the section source block once per section in presentation order. Keep each YAML property on its own line between `---` delimiters.

<!-- prettier-ignore -->
```md
---
title: '<presentation title>'
theme: '@alphacifer/slidev-academic-theme'
colorSchema: light
addons:
  - '@alphacifer/slidev-addon-theme'
background: ./assets/main.png
drawings:
  persist: false
transition: slide-left
mdc: true
comark: true
hideInToc: true
fonts:
  sans: Roboto
  serif: Roboto
  mono: Roboto Mono
duration: <timing>
---

# <presentation title>

## <presentation subtitle>

<Speaker
  author="<author>"
  date="<presentation-date>"
/>

---
layout: arc-toc
hideInToc: true
indexed: true
---

# <contents title>

---
src: ./pages/<section>/main.md
---

---
layout: thanks
hideInToc: true
---
```

Use the seminar timing supplied by the user. If none is supplied and it cannot be inferred, use `30min` as the initial default.

The presentation subtitle is optional. Include `## <presentation subtitle>` beneath the title only when a subtitle is supplied or requested; otherwise omit that heading entirely.

Use one `Speaker` component with a single `author` and no custom classes in the generic cover. Do not use the `team` prop in the generic template. Use the supplied presentation date; retain `2026-09-23` as the fallback only when creating a new deck or adding a missing `Speaker` without a supplied date. When editing an existing deck, preserve its current `Speaker` date exactly unless the user asks to change it.

### Required navigation and closing slides

Every deck must include at least one slide with `layout: arc-toc` and at least one with `layout: thanks`. The default sequence is cover, contents slide, section imports, then the thank-you slide. The contents title is optional: include `# <contents title>` only when supplied or requested; otherwise omit the heading and leave the `arc-toc` slide body empty. Use `hideInToc: true` on both layouts and `indexed: true` on the contents slide. Additional contents and thank-you slides are allowed wherever the presentation needs them; preserve existing additional instances rather than reducing them to exactly one.

### Preserve Slidev frontmatter

Do not turn per-slide YAML into a paragraph, heading, or a single line of multiple properties. Generic Markdown formatters can misinterpret Slidev frontmatter. Use a Slidev-aware formatter for deck files, or exclude them from generic formatting. The ignore comments before template fences in this reference protect their literal syntax during documentation formatting; do not copy those comments into a deck. See the [Slidev Prettier plugin](https://github.com/slidevjs/prettier-plugin) for deck formatter configuration.

## Section entry template

Each `pages/<section>/main.md` contains the section frontmatter, its title, and the numbered article imports. Use this complete template, replacing the placeholders and repeating the source block for every article:

<!-- prettier-ignore -->
```md
---
layout: bg-center
transition: fade
indexed: true
background: ../../assets/heading.png
---

# <section title>

---
src: ./01-<article-1>.md
---

---
src: ./02-<article-2>.md
---
```

Keep each article import in its own `---` frontmatter block, with `src` pointing to the article relative to this section's `main.md`. Import every numbered article in numeric order; do not skip a file or turn an import into a Markdown heading.

## Article template

Each `pages/<section>/0N-<article>.md` starts with the article frontmatter, followed by a concise slide title and its content:

```md
---
layout: shifting-intro
hideInToc: true
transition: slide-left
---

# <slide title>

<slide content>
```

Write the article's slide content after this frontmatter. Use additional `---` slide separators inside the article when its content needs more than one slide. Keep article-specific content in the numbered article file rather than placing it in the section entry file.

Replace `<slide content>` with the actual content for that slide, using Markdown, addon components, or HTML as appropriate. The generic template does not prescribe a table or any other content-specific structure.

## Editing existing decks

- Preserve the required theme, addon, shared defaults, and section organization unless the user explicitly asks to customize them.
- Preserve an existing `Speaker` date exactly, even when it differs from the scaffold default.
- Reuse existing section and article names when extending a deck.
- Add new article files with the next available zero-padded number and update the section's `main.md` import list.
- Add new section source blocks to `slides.md` in the intended presentation order.
- Do not overwrite existing background images just to reapply the default structure.

## ✅ Do

- Keep article content in numbered files and import every file in presentation order.
- Copy missing backgrounds from this skill's `assets/` directory, resolved relative to `SKILL.md`.
- Preserve existing names, custom backgrounds, and author-edited `Speaker` dates when extending a deck.

## ❌ Do not

- Flatten section articles into `slides.md` or section entry files.
- Skip imports, reorder articles unintentionally, or reset an existing `Speaker` date to the scaffold default.
- Collapse per-slide YAML into a paragraph or heading, or remove additional contents or thank-you slides merely to enforce a single instance.
- Replace existing assets or overwrite unrelated content while scaffolding.

## Verification

- Confirm `slides.md`, `assets/main.png`, and `assets/heading.png` exist.
- Confirm every section has `main.md` and at least one numbered article file.
- Confirm at least one `arc-toc` slide and one `thanks` slide exist with the required frontmatter; additional instances are allowed. A contents title is optional and must be omitted when none is supplied or requested.
- Confirm cover placeholders are replaced and the generic cover uses a title, an optional `##` subtitle, and one `Speaker` component with `author`, without `team` or custom classes. Omit the subtitle heading when no subtitle is supplied or requested.
- Confirm the root deck imports every section and section entry files import every numbered article in numeric order.
- Resolve every `src` and `background` path from the file containing it.
- Check the root, section, and article frontmatter against the templates, preserving intentional author customizations.
