# LaTeX production

Read this guide for LaTeX creation, editing, or styling, applying the shared [writing voice](../SKILL.md#writing-voice). For research papers and theses, also read [Paper writing](paper-writing.md) for structure, evidence, and style routing.

## Style selection

For both research papers and theses, use the shared [format and style selection](paper-writing.md#format-and-style). For other LaTeX documents, follow explicit user requirements and existing class/project conventions. Do not import the DOCX A4/Times New Roman defaults into LaTeX automatically. The shared writing voice applies to all profiles.

## Engine and setup

- Inspect the existing source tree, class, packages, bibliography workflow, fonts, and build tools. Preserve an existing project’s conventions and make the narrowest requested change.
- Choose the compiler, fonts, class, and bibliography tooling from the selected profile and existing project. ICIS defaults to XeLaTeX with `fontspec` and Georgia. IEEE and ACM papers use a compiler supported by their official template, defaulting to pdfLaTeX for a new generic project. Do not force `fontspec`, Georgia, APA, or custom geometry onto either publisher class. Disclose unavailable fonts, classes, or language packages rather than silently substituting another profile.
- Papers and theses use English text, headings, captions, and front matter unless the user specifies another language. Configure the language packages accordingly; for other documents, match the intended use and user requirements.
- Keep custom layout configuration together in the preamble or an existing style file. Use the selected guide for geometry, heading hierarchy, caption placement, running matter, and reference formatting. For publisher papers, let the official class control these values. Use existing class features or installed packages before adding dependencies.
- Preserve thesis preliminary matter and chapter structure. When preliminary matter exists, use lowercase Roman numbering there, then switch to Arabic and reset to 1 at the Introduction when present. If there is no preliminary matter, start Arabic numbering at 1 without adding a front matter section solely to change numbering. Conference papers normally start Arabic numbering at 1 with no preliminary matter.
- Configure paragraph and heading spacing centrally rather than stacking line breaks or vertical skips.
- Use semantic sectioning and automatic counters, labels, and references. Do not manually type page, figure, table, equation, or section numbers. Keep bibliography tooling consistent with the project or user's requested citation style.

## Build and visual checks

Compile with the project's documented command or `latexmk` configured for the selected profile's engine. Run the required bibliography tool and recompile until cross-references and page numbers settle. Resolve compilation errors, missing glyphs, undefined references/citations, and material warnings. Inspect every PDF page against the selected profile and target template for page size, columns, margins, actual fonts, heading/caption styles, page-number transition, overflow, figures, tables, and blank pages. Deliver the editable `.tex` project and required assets/bibliography files, plus the PDF when requested or expected. If compilation is unavailable, still provide source when requested and clearly state that no compiled PDF or visual check was completed.
