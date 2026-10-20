# IEEE academic style

Use this guide for both research papers and theses when IEEE is selected by the shared [paper style rules](paper-writing.md#format-and-style). The profile applies in either output format. Use [DOCX production](docx.md#style-selection) for Word templates; the class and package instructions below apply to LaTeX only. A controlling university or publication template takes priority.

## Paper layout and typography

- Start from the target venue's official IEEE template and its documented class options. For a generic conference paper without a named venue, use `\documentclass[conference]{IEEEtran}` and the official conference sample. Use a journal variant only when the target is a journal; Computer Society and other variants may differ.
- Default to pdfLaTeX and BibTeX for a new generic project. Preserve another supported engine in an existing project or supplied template. Do not force XeLaTeX, `fontspec`, Georgia, or ICIS formatting onto `IEEEtran`.
- Let the class control page size, margins, columns, fonts, title, headings, line spacing, indentation, captions, and running matter. The generic conference layout is a two-column, 10 pt, Times-based layout; use the selected template's actual settings rather than manually approximating it. Do not load `geometry` or override class dimensions to make a paper fit a page limit.
- Use the native title and author commands with `\maketitle`, and semantic section/subsection commands with the class's automatic heading numbering. Supply author information only when known and appropriate to the submission stage.
- Keep table captions above tables and figure captions below figures, using the class's caption formatting and automatic numbering. Keep tables editable in the LaTeX source. Fit ordinary floats within a column; use two-column floats only when needed and allowed by the template. Do not replace the class's caption style with the ICIS caption rules.
- Use IEEE numbered citations, normally with `\bibliographystyle{IEEEtran}` and a `.bib` file. For a new generic project, use the template's citation package setup and list references in citation order. Preserve an existing bibliography workflow if it can produce the required format; migrate only when the requested style requires it. Do not impose APA 7 or alphabetical reference ordering.
- Retain the class's default header/footer and page-number behavior unless the venue requires a change. Do not add conference names, copyright notices, or identifiers that the user or venue has not supplied.

## Thesis structure and implementation

This is Alpha's IEEE-inspired thesis profile, not an official IEEE thesis standard. Use a chapter-capable `report`/`book` or university class rather than trying to add thesis chapters to `IEEEtran`. A university's requirements control the layout when supplied.

| Element            | Custom thesis default                                                       |
| ------------------ | --------------------------------------------------------------------------- |
| Page               | US Letter, portrait, single column                                          |
| Margins            | 1 inch on every side                                                        |
| Font and body      | Times-based text and compatible math, 10 pt, justified                      |
| Spacing            | Single line spacing, 0 pt between paragraphs, 1 em first-line indent        |
| Thesis title       | 24 pt, regular, centered                                                    |
| Chapter heading    | 14 pt, centered, small capitals, automatically numbered                     |
| Section heading    | 10 pt, centered, small capitals, automatically numbered                     |
| Subsection heading | 10 pt, left aligned, italic, automatically numbered                         |
| Heading spacing    | 10 pt before, 6 pt after; keep with following text                          |
| Captions           | 8 pt, regular; table captions above, figure captions below                  |
| References         | IEEE numbered citations, citation-order bibliography, 10 pt, single-spaced  |
| Running matter     | Short title in 9 pt Times-based text; automatic page number at footer right |

- For a new generic thesis, use a 10 pt `report` class with `letterpaper,margin=1in` geometry. Prefer pdfLaTeX with installed Times-compatible text/math packages such as `newtxtext` and `newtxmath`. This is an explicit Times-based adaptation; use actual Times New Roman with an appropriate engine when the university requires that font specifically.
- Keep required cover information, author details, abstract, contents, chapters, and front matter. Use lowercase Roman preliminary page numbers, then Arabic numbering restarted at 1 at the Introduction. Use chapter-based figure/table counters. Preserve a supplied institution's heading and numbering scheme instead of replacing it with conference conventions.
- Use IEEE bibliography formatting and automatic citation labels. Omit conference branding, copyright blocks, submission labels, anonymous-review requirements, and conference page limits.

## Verification and submission

For a paper submission, establish the venue, year, paper type, review/final stage, page limit, and anonymity instructions from the current official author guidelines. IEEE branding alone does not establish those requirements. Follow any required PDF validation workflow when preparing an actual submission.

Compile with the selected engine and bibliography tool. Check the PDF against the actual class sample: dimensions, columns, font embedding, heading hierarchy, caption placement, table widths, numbered citations, bibliography order, running matter, and overflow. For a thesis, verify the single-column adaptation, front matter, chapter counters, and Roman-to-Arabic pagination instead. Resolve undefined citations/references and font substitutions before claiming verification.

## Sources

- [IEEE conference authoring tools and templates](https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/)
- [IEEE conference manuscript templates](https://www.ieee.org/conferences/publishing/templates.html)
- [IEEEtran class and author documentation](https://ctan.org/pkg/ieeetran)
