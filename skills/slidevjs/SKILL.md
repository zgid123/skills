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
3. Before scaffolding, extending, or reorganizing a deck, read [Deck Structure](./references/deck-structure.md). Use its templates and existing-deck preservation rules without deleting unrelated files.
4. Before drafting slide content or selecting components, read [Content and Presenter Notes](./references/content-and-notes.md). Keep titles concise, show highlights on slides, and put supporting detail in presenter notes.
5. Read [Component Selection](./references/component-selection.md) before creating or substantially rewriting article slides. Match components to the content relationship and supported item count, using plain content when no component improves comprehension.
6. Read the HTML and CSS references below when their triggers apply, then verify the deck using the checklist.

## Dependencies

Every deck uses:

- `@alphacifer/slidev-academic-theme`
- `@alphacifer/slidev-addon-theme`

Place them according to the repository boundary:

- **Standalone project**: check the project's `package.json`; add only missing packages to that project.
- **Monorepo**: find the workspace root and inspect its `package.json`. If both packages are already declared at the root, do not install them again. If either is missing, add only the missing package at the workspace root using the detected package manager's workspace-root option. Do not add either package to each child project.

Treat a package as present when it is a direct entry in the root manifest's dependency sections. Do not switch package managers, rewrite unrelated dependency versions, or reinstall packages merely because the deck is in a new child directory.

## HTML and style blocks in Markdown

Read [HTML Spacing](./references/html-spacing.md) before writing or editing HTML in a Slidev `.md` file. Avoid unnecessary blank lines between elements, preserve spacing required for rendering, and check affected slides in preview.

Read [CSS Formatting](./references/css-formatting.md) before writing any CSS for a deck, including a `<style>` block, `style.css`, or inline `style` attribute. Use theme defaults first; never override theme or addon styles without the user's explicit permission. Apply its multiline class-rule formatting and verification checklist.

## Verification

Before finishing, confirm:

- The deck passes the [Deck Structure](./references/deck-structure.md#verification) checklist, with existing assets and author-edited dates preserved.
- The `thanks` slide is the last slide; no appendix, backup, references, or other slides follow it.
- No visible content extends beyond the slide's content area into the margins or page-number area.
- No theme or addon styles are overridden without the user's explicit permission.
- The theme and addon declarations exactly use the two `@alphacifer` packages at the correct package boundary, with no duplicate declarations introduced in monorepo child manifests.
- Titles, visible highlights, and presenter notes follow [Content and Presenter Notes](./references/content-and-notes.md#verification).
- Diagram and card components fit the content relationship and supported item count described in the component selection guide.
- CSS class rules in Markdown `<style>` blocks created or edited by this task follow [CSS Formatting](./references/css-formatting.md).
- HTML spacing follows [HTML Spacing](./references/html-spacing.md), and affected slides have been checked in preview for missing or incorrectly rendered content. If preview is unavailable, report that limitation.
