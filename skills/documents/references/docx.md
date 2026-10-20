# DOCX formatting and production

Use this guide for Word document creation, editing, or styling. The formatting defaults below are Alpha's DOCX specification supplied on 2026-10-19. Apply the shared [writing voice](../SKILL.md#writing-voice) in every output format.

## Style selection

For research papers and theses, follow the shared [paper style selection](paper-writing.md#format-and-style) and load the selected guide. Use the target publication's official Word template for an actual paper submission. For generic ICIS styling, apply the ICIS typography, captions, citations, and running matter through Word styles and fields. For ACM or IEEE, inspect the official Word template and venue/stage instructions rather than reproducing LaTeX class options in Word. If no suitable template is available, identify the missing input and label any requested approximation as unverified for submission compliance. For a thesis, apply the selected profile's structural adaptation unless a university template controls it.

The A4 layout, heading case, footer typography, caption positions, and TOC typography below are DOCX report/personal-document defaults. Selected paper/thesis profiles and explicit requirements override those values in DOCX as they do in LaTeX.

## Page and body

| Element           | DOCX default                                         |
| ----------------- | ---------------------------------------------------- |
| Paper             | A4 portrait only (21 × 29.7 cm)                      |
| Margins           | Top 3.5 cm; left 3.5 cm; bottom 3.0 cm; right 2.0 cm |
| Font              | Times New Roman                                      |
| Body size         | 13 pt                                                |
| Line spacing      | 1.5 lines                                            |
| Paragraph spacing | 0 pt before; 6 pt after                              |
| Body alignment    | Justified                                            |
| First-line indent | 1.0 cm                                               |

Apply first-line indents to ordinary body paragraphs, not headings, captions, lists, or table cells. Keep list hanging indents legible and distinct from body indentation.

Control vertical layout with paragraph spacing, line-spacing settings, and semantic page or section breaks. Do not insert repeated empty paragraphs, extra Enter presses, or manual line breaks to simulate spacing. Let text wrap naturally. Use keep-with-next and keep-together where appropriate, and reserve explicit breaks for meaningful document boundaries. Cover blocks may use larger paragraph spacing; remove their spacing when optional blocks are omitted. In DOCX, use 1.5-line spacing (`w:line="360"` with `w:lineRule="auto"`), not a fixed 1.5 pt or an arbitrary exact line height.

## Heading hierarchy

| Level | Appearance | Spacing |
| --- | --- | --- |
| Heading 1 / Chapter | 16 pt, bold, uppercase, centered | 12 pt before and after |
| Heading 2 | 14 pt, bold, title case, left aligned | 6 pt before and after |
| Heading 3 | 13 pt, bold italic, left aligned | 6 pt before and after |
| Heading 4 | 13 pt, italic, not bold, left aligned; use sparingly | 6 pt before and after |

Do not use a lower level merely to obtain a desired appearance. Use semantic heading levels, no first-line indent, and keep a heading with the paragraph that follows when the format allows. Do not force a chapter onto a new page unless the user or a controlling template requires it.

## Running matter and page numbering

Use Times New Roman, 11 pt, regular in headers and footers. Place page numbers in the centered footer. Number preliminary pages (declaration, acknowledgments, contents, and lists) with lowercase Roman numerals. Restart with Arabic numeral 1 at the Introduction and continue Arabic numbering to the end. If the document has no preliminary pages, start Arabic numbering at 1. Do not type page numbers manually.

## Figures and tables

Use Times New Roman, 12 pt, regular, centered captions consistently. Put table captions directly above their table and figure captions directly below their figure. Number tables and figures in separate sequences by chapter (for example, Figure 1.1 and Table 2.3). For documents without numbered chapters, use continuous numbering within each figure/table type. Keep each caption with its associated object where possible; do not clip, distort, or overflow tables and figures.

## Case and language

Use uppercase for Heading 1. Use title case for Heading 2 where appropriate to the document language, preserving Vietnamese diacritics. Keep the author's intended wording. Do not corrupt casing or Unicode text in the name of style normalization. Use font fallbacks only when Times New Roman is unavailable and clearly disclose that substitution.

## Creation and editing

- Inspect the existing project, DOCX, available libraries, fonts, and compatible renderers before choosing tools. Do not assume a particular package or application is installed.
- On macOS, use a working Word-compatible renderer such as the headless `soffice` command. Do not launch LibreOffice's app-bundled Python directly from a shell: signed builds can require a LibreOffice parent process and macOS may terminate the interpreter with a launch-constraint violation. If that happens, stop retrying that interpreter and use another working renderer or compatible field updater; report any remaining field-refresh checks as unverified. Keep the application signature and system security settings intact. Use a separate writable LibreOffice user profile for concurrent rendering jobs.
- For a new DOCX, use the available Word document library or a carefully tested OOXML method. Set the selected profile's geometry and all margin, body, heading, caption, header, and footer values explicitly so Word defaults cannot override them.
- Use semantic Title, Heading levels one through four, Normal, caption, list, and table styles. Apply automatic chapter and heading numbering where appropriate. For the default DOCX profile, keep Heading 1 uppercase, and use requested hierarchy rather than direct formatting alone.
- When preliminary matter exists, set it in a section with lowercase Roman page numbering; when an Introduction follows, use a section break there and restart Arabic numbering at 1. If there is no preliminary matter, start Arabic numbering at 1 without adding sections solely to change numbering. Use PAGE fields; under the default DOCX profile, center them in the footer with 11 pt Times New Roman.
- Use Word SEQ fields or another tested automatic mechanism for separate figure and table counters, chapter-based when chapters are numbered and continuous otherwise. Test chapter resets in the selected renderer. If it ignores the `\s 1` heading-level reset, put `\r 1` on the first caption of each figure/table sequence in that chapter and maintain the reset point when captions are inserted or reordered; do not reset every caption. Follow the selected profile for placement: default DOCX report formatting puts table captions above and figure captions below; ICIS puts both below. Do not type numbers that will become stale after edits.
- Preserve content, sections, relationships, bookmarks, comments, tracked changes, footnotes, hyperlinks, and embedded objects during edits. Compare these features and unrelated package parts before and after a narrow edit; use targeted OOXML edits when a high-level library would lose review markup. Do not accept or reject revisions or remove comments unless requested. Refresh fields and render a copy when the updater would alter protected markup in the editable original. Do not flatten complex documents into plain text. If a tool cannot preserve an existing feature, choose a safer path or disclose the limitation before changing it.
- Use real list numbering, deliberate table widths, repeating table headers where useful, and row heights that can expand. Preserve image aspect ratios and keep headings/captions with the related content.
- Configure space before/after and line spacing in named styles. Do not use repeated empty paragraphs to position content. Use section breaks for changes in numbering and page setup; allow body text to flow naturally. When adapting an imported template, resolve duplicate style IDs and conflicting direct formatting so the configured style actually controls the rendered text.

## Table of contents

- Create a DOCX table of contents when the user requests one, the existing document has one, or the document's length and section structure make one useful. Short letters, reflections, and similarly simple documents do not need one. When a TOC is appropriate, use Word's built-in automatic feature with a native `TOC` field driven by semantic Heading styles. In Word, use References > Table of Contents > an automatic table.
- Never hand-type TOC entries or use a generated static list as the default. When creating a DOCX programmatically, insert a real Word TOC field and preserve its editable field code and cached result.
- Under the default DOCX profile, use a plain centered TOC title without a decorative colored rule. Set TOC entries in 12 pt Times New Roman with 1.5 line spacing and 0 pt before/after, including after refreshing the field.
- Include the heading levels needed for the document, normally Heading 1-3. Update the entire table, including page numbers, after content or pagination changes and before rendering or delivery. Save the DOCX after the field update, then read back the saved cached results and compare them with the final pagination; an in-memory update or a PDF from an unsaved copy is not a verified update to the delivered file. Enable field updates on open when supported.
- If Word is unavailable, use a compatible Word processor to refresh the field. If no compatible updater is available, retain the native field and report that its cached result may need updating; do not replace it with manually generated text.

## Verification

Confirm the DOCX is a valid package, expected text and media are present, heading/list structure is semantic, and fields/references are linked correctly. Read the delivered package back to verify the requested style and section values and resolve each internal relationship target; do not infer them only from the code that created the file. A ZIP/XML parse alone confirms basic integrity, not the requested settings. Export the final DOCX to PDF with an available Word-compatible renderer and inspect every page, using page images when useful. Inspect margins, font substitution, page-number restart, heading hierarchy/case, caption positions and numbering, overflow, tables, images, and blank pages. Inspect embedded PDF font names to confirm that the renderer used the selected fonts; a font installed on the host may still be invisible to the renderer. If necessary, configure font discovery for that render process and render again, or disclose substitution. Re-export and inspect after layout changes.

## Delivery

Deliver both the editable `.docx` and its final PDF export by default. The PDF is a user-facing artifact for quick review, not a temporary QA file. Keep it synchronized with the final DOCX; when field updates require a separate copy to preserve protected markup, disclose any field-refresh differences between the PDF and editable document. Honor explicit output overrides. If PDF export is unavailable, deliver the DOCX and clearly report the missing PDF and unverified visual checks.
