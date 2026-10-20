# ACM academic style

Use this guide for both research papers and theses when ACM is selected by the shared [paper style rules](paper-writing.md#format-and-style). The profile applies in either output format. Use [DOCX production](docx.md#style-selection) for Word templates; the class and package instructions below apply to LaTeX only. A controlling university or publication template takes priority.

## Paper layout and typography

- Start from the official `acmart` template and the target venue's prescribed format options. For a generic conference layout, use `sigconf`. For a draft with no actual ACM publication metadata, use `\documentclass[sigconf,nonacm]{acmart}` to retain the layout without inventing ACM rights or publication information. This draft option does not establish submission compliance.
- For an actual submission, select the format and review stage from the venue's current instructions. Some venues require `manuscript,review,anonymous` for a single-column review copy; others require `sigconf` or a different format. Do not infer column count or anonymity solely from the word ACM. Ask for missing venue/stage information when needed to prepare a submission; use the generic draft layout when only styling is requested.
- Default to pdfLaTeX and the official sample's bibliography workflow for a new generic project. Preserve another class-supported engine in an existing template. Let `acmart` load its own fonts and packages; do not replace its Libertine-based font setup with Georgia or a forced system-font configuration.
- Let the selected class variant control body/title sizes, page dimensions, margins, columns, heading numbering, spacing, caption typography, and running matter. Do not apply ICIS geometry or manually recreate an ACM layout in `article`. The generic `sigconf` paper uses a two-column proceedings layout; other ACM formats differ.
- Use native title, author, affiliation, abstract, and sectioning commands. Populate metadata only from supplied facts. Use the venue's requested anonymity mode rather than manually hiding only the printed author names.
- Keep table captions above tables and figure captions below figures, using native class formatting and counters. Keep tables editable in the LaTeX source, fit them to the selected column width, and provide meaningful figure descriptions with `\Description` when figures are present. Use class-compatible packages permitted by the target publication workflow.
- For a new generic project, use BibTeX with `\bibliographystyle{ACM-Reference-Format}` and the class's default numeric citations. Use an author-year mode, such as `\citestyle{acmauthoryear}`, only when the venue or user requires it. Let the ACM reference style determine bibliography ordering and formatting. Do not impose IEEE citation-order sorting or APA 7.
- Keep class-managed running titles, page numbering, rights information, and reference-strip behavior for an actual submission. Set only venue-provided values for DOI, ISBN, conference details, and copyright. For a generic non-ACM draft, omit those publication fields instead of inserting fabricated metadata.

## Thesis structure and implementation

This is Alpha's ACM-inspired thesis profile, not an official ACM thesis standard. Use a chapter-capable `report`/`book` or university class rather than forcing a thesis into `acmart`. A university's requirements control the layout when supplied.

| Element | Custom thesis default |
| --- | --- |
| Page | US Letter, portrait, single column |
| Margins | 1 inch on every side |
| Font and body | Libertine-based text and compatible math, 10 pt, justified |
| Spacing | Single line spacing, 0 pt between paragraphs, 1 em first-line indent |
| Thesis title | 18 pt, bold, centered |
| Chapter heading | 14 pt, bold, left aligned, automatically numbered |
| Section heading | 12 pt, bold, left aligned, automatically numbered |
| Subsection heading | 10 pt, bold italic, left aligned, automatically numbered |
| Heading spacing | 10 pt before, 6 pt after; keep with following text |
| Captions | 9 pt, regular with bold label; table captions above, figure captions below |
| References | ACM numeric citations by default, ACM reference formatting/order, 10 pt, single-spaced |
| Running matter | Short title in 9 pt Libertine-based text; automatic page number at footer right |

- For a new generic thesis, use a 10 pt `report` class with `letterpaper,margin=1in` geometry and installed Libertine-compatible text/math packages. With pdfLaTeX, a supported setup is `libertine` with `newtxmath` using its `libertine` option. Disclose missing font support rather than silently falling back to Georgia or Computer Modern.
- Keep required cover information, author details, abstract, contents, chapters, and front matter. Use lowercase Roman preliminary page numbers, then Arabic numbering restarted at 1 at the Introduction. Number figures and tables by chapter, retaining semantic labels and references.
- Use `ACM-Reference-Format` with a compatible citation package such as `natbib` for a new thesis. Default to numeric citations; preserve an existing or institution-required author-year workflow when applicable. Do not add ACM rights blocks, conference branding, submission labels, anonymous-review requirements, or conference page limits to a thesis.

## Verification and submission

For an actual submission, verify the venue, year, format variant, review/final stage, citation mode, anonymity, page/word limit, and package restrictions. Do not treat a two-column draft or successful `acmart` compilation as proof that a review submission uses the required options.

Compile with the selected engine and bibliography tool. Inspect the PDF for the selected variant's page dimensions, columns, embedded fonts, headings, caption placement, table widths, citations, bibliography, running matter, metadata, and overflow. For a thesis, verify its custom single-column layout, chapters, front matter, and pagination. Resolve missing figure descriptions, undefined references/citations, and material class warnings as appropriate to the document and publication stage.

## Sources

- [ACM proceedings template and author workflow](https://www.acm.org/publications/proceedings-template)
- [ACM class maintainer's documentation and source](https://github.com/borisveytsman/acmart)
- [ACM class samples](https://github.com/borisveytsman/acmart/blob/primary/samples/samples.dtx)
- [ACM LaTeX package and user guide](https://ctan.org/pkg/acmart)
