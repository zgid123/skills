# ICIS-based academic style

Use this profile for both research papers and theses when selected by the shared [paper style rules](paper-writing.md#format-and-style), in either LaTeX or DOCX. The ICIS 2026 paper baseline supplies the typography and citations. The thesis section adapts structure to chapters and front matter; it is not an official ICIS thesis standard. Recheck the target conference's year-specific requirements before a submission.

## Page and typography

| Element                         | Default                                          |
| ------------------------------- | ------------------------------------------------ |
| Page                            | US Letter, portrait, single column               |
| Margins                         | 1 inch / 2.54 cm on every side                   |
| Main font                       | Georgia                                          |
| Body                            | 10 pt, justified                                 |
| Line spacing                    | Single / 1.0                                     |
| Paragraph spacing               | 0 pt before, 6 pt after                          |
| First-line indent               | None                                             |
| Title                           | 20 pt, bold, centered, title case                |
| Main heading                    | 13 pt, bold, left aligned, title case            |
| Second-level heading            | 11 pt, bold italic, left aligned, title case     |
| Third-level heading             | 10 pt, bold, left aligned, title case            |
| Heading spacing                 | 10 pt before and after; keep with following text |
| Figure and table captions       | Georgia 10 pt, bold, centered, below the object  |
| References                      | Georgia 10 pt, single-spaced, alphabetical       |
| Reference hanging indent        | 0.25 inch / 0.635 cm                             |
| Space between reference entries | 0 pt                                             |
| Citation style                  | APA 7 author-year                                |

Use Georgia in table cells as well as body text. Keep tables editable in the LaTeX source, with readable text and widths that fit the text area. Number figures and tables automatically in separate sequences; spell out Figure and Table in captions and references. Let long captions wrap readably. Use semantic labels and references rather than typed counters.

## Paper layout

- For a new paper, use a 10 pt `article` class with XeLaTeX, `fontspec`, `\setmainfont{Georgia}`, and `geometry` configured with `letterpaper,margin=1in`. Set `\parindent` to `0pt`, `\parskip` to `6pt`, and single spacing. Configure the typography above explicitly rather than retaining the article class's default title and section sizes.
- Map the heading hierarchy to `\section`, `\subsection`, and `\subsubsection`. Keep these headings unnumbered; do not introduce deeper levels for the default paper profile.
- Use continuous figure and table numbering. Do not add a thesis cover, contents page, preliminary Roman numbering, or chapter-based counters to a conference paper.
- Use a short running title of at most eight words, right aligned in Georgia 9 pt italic. Set header/footer distances to 0.5 inch. For a conference submission, use the target year's prescribed conference footer and automatic Arabic page numbers; the ICIS 2026 template uses Georgia 9 pt italic conference text and a bold page number at the right. For a general draft without a target, use a right-aligned page number and omit conference branding rather than inventing a venue, location, or year.
- Use APA 7 author-year citations with a complete alphabetical bibliography. For a new project, prefer `biblatex` with `style=apa`, `backend=biber`, `\bibhang` set to `0.25in`, `\bibitemsep` set to `0pt`, and single-spaced bibliography text. Preserve an existing BibTeX or other bibliography workflow when editing; changing typography alone does not authorize migrating it.

## Thesis structure and implementation

- Use a 10 pt chapter-capable `report` or `book` class, or the existing university class. Apply the page, body, title, caption, and bibliography values above when no university style controls the document. Preserve an existing thesis's content and structure during format-only work.
- Keep thesis chapters, contents, and required front matter. For a new chaptered thesis, map the three heading appearances above to chapter, section, and subsection; retain automatic chapter and section numbering. An institution's heading hierarchy takes priority.
- Use lowercase Roman numerals for preliminary pages, then Arabic numbering restarted at 1 at the Introduction. Use a short running title in Georgia 9 pt italic and automatic page numbers at the right of the footer. Omit conference branding and submission-type labels.
- Number figures and tables by chapter in a chaptered thesis, or continuously in a chapterless document. Use APA 7 by default unless the user, university, or existing bibliography specifies another style.
- Do not apply conference page limits, anonymous-review rules, or instructions to omit an abstract to a thesis. Keep its required abstract and author information.

## Conference submission checks

These are submission requirements, not universal typography rules. For an actual ICIS submission, inspect the current official template and checklist, then compare the compiled LaTeX PDF against them. A LaTeX reproduction of the appearance is not evidence that the venue accepts that source format.

For the verified ICIS 2026 baseline, completed research papers have a 16-page limit and short papers an 8-page limit, including references and appendices. The anonymous review PDF omits author information, acknowledgements, abstract, and impact statement; the latter two are entered separately in the submission system. Remove identifying metadata, comments, and review markup. Apply different requirements when the target year or submission stage specifies them.

Check the compiled PDF for Letter dimensions, margins, embedded Georgia fonts and sizes, single spacing, heading alignment, caption placement, readable tables/figures, reference indentation, bibliography order, running title length, and correct page numbering. Do not claim submission compliance from successful compilation alone.

## Sources

- [ICIS 2026 submission formatting checklist](https://icis2026.aisconferences.org/submissions/submission-formatting-checklist/)
- [ICIS 2026 paper templates](https://icis2026.aisconferences.org/submissions/paper-templates-pcs-guide-for-authors/)
- [ICIS 2026 submission requirements](https://icis2026.aisconferences.org/submissions/types-of-submissions/)
