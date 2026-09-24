---
name: slidevjs
description: Create, scaffold, edit, or reorganize Slidev presentations using Alpha's required academic theme, addon, dependency placement, and section-based Markdown structure. Always use when a task mentions Slidev, a Slidev deck, slides.md, seminar slides, or Markdown presentation files intended for Slidev, including decks inside monorepos.
---

# Slidev

## Purpose

Create Slidev seminar decks with a predictable structure, shared visual defaults, and correct dependency placement. Keep the initial scaffold conventional; customize it only when the user asks.

## Workflow

1. Inspect the repository before changing files. Identify the package manager, the workspace root, any existing Slidev deck, and whether the target is a standalone project or a package inside a monorepo.
2. Check the relevant `package.json` before installing packages. Reuse existing dependencies and the repository's package manager.
3. Create or update the required deck structure without deleting unrelated files or overwriting existing content unnecessarily.
4. Before writing article content, read [Component Selection](./references/component-selection.md) and match each slide's information relationship to a suitable addon component.
5. Populate the root deck, section entry files, and numbered article files from the templates below.
6. Verify the dependency location, file paths, source imports, frontmatter, component choices, and referenced PNG assets.

## Dependencies

Every deck uses:

- `@alphacifer/slidev-academic-theme`
- `@alphacifer/slidev-addon-theme`

Place them according to the repository boundary:

- **Standalone project**: check the project's `package.json`; add only missing packages to that project.
- **Monorepo**: find the workspace root and inspect its `package.json`. If both packages are already declared at the root, do not install them again. If either is missing, add only the missing package at the workspace root using the detected package manager's workspace-root option. Do not add either package to each child project.

Treat a package as present when it is a direct entry in the root manifest's dependency sections. Do not switch package managers, rewrite unrelated dependency versions, or reinstall packages merely because the deck is in a new child directory.

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

Use this as the default `slides.md`. Replace angle-bracket placeholders with actual values, repeat the section source block once per section in presentation order, and keep the remaining defaults unchanged unless the user requests customization.

```md
---
title: "<title of seminar>"
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

# <title of seminar>

<Speaker :date="'2026-09-23'" />

---
layout: arc-toc
hideInToc: true
transition: slide-left
indexed: true
---

---
src: ./pages/<section>/main.md
---

---
layout: thanks
---
```

Use the seminar timing supplied by the user. If none is supplied and it cannot be inferred, use `30min` as the initial default. Use `2026-09-23` as the `Speaker` date when creating a new deck or adding a missing `Speaker` component. When editing an existing deck, preserve its current `Speaker` date exactly; treat a different date as an intentional author edit and do not reset it to the default.

## Section entry template

Each `pages/<section>/main.md` starts with this frontmatter and the section title:

```md
---
layout: bg-center
transition: fade
indexed: true
background: ../../assets/heading.png
---

# <section title>
```

After the title, import every numbered article in order using Slidev source blocks:

```md
---
src: ./01-<article-1>.md
---

---
src: ./02-<article-2>.md
---
```

Do not skip an article file or import it out of numeric order.

## Article template

Start every `pages/<section>/0N-<article>.md` with:

```md
---
layout: shifting-intro
hideInToc: true
transition: slide-left
---
```

Write the article's slide content after this frontmatter. Use additional `---` slide separators inside the article when its content needs more than one slide. Keep article-specific content in the numbered article file rather than placing it in the section entry file.

Select components by the meaning and relationship of the content, not merely for visual variety. Read [Component Selection](./references/component-selection.md) whenever creating or substantially rewriting article slides. Use its decision table, fixed item-count constraints, canonical composition names, and plain-content fallback before choosing a component.

## Editing existing decks

- Preserve the required theme, addon, shared defaults, and section organization unless the user explicitly asks to customize them.
- Preserve an existing `Speaker` date exactly, even when it differs from the scaffold default.
- Reuse existing section and article names when extending a deck.
- Add new article files with the next available zero-padded number and update the section's `main.md` import list.
- Add new section source blocks to `slides.md` in the intended presentation order.
- Do not overwrite existing background images just to reapply the default structure.

## Verification

Before finishing, confirm:

- `slides.md`, `assets/main.png`, and `assets/heading.png` exist.
- Every section has `main.md` and at least one numbered article file.
- `slides.md` imports every section, and each section `main.md` imports every numbered article in numeric order.
- All `src` and `background` paths resolve from the file containing them.
- The theme and addon declarations exactly use the two `@alphacifer` packages.
- Diagram and card components fit the content relationship and supported item count described in the component selection guide.
- A monorepo has no duplicate theme or addon declarations in child package manifests introduced by this task.
