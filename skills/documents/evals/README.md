# Document evaluations

Run cases against the current skill and an unchanged snapshot of the previous version using the same prompt, fixtures, tools, and environment. Use a fresh output directory for every run. The course-report asset is an editable layout example; the existing-project fixtures are preservation tests.

## Fixtures and coverage

- `files/latex-existing/`: chaptered XeLaTeX project with a BibTeX citation and two referenced figures. Preserve its content and bibliography workflow during the requested style change.
- `files/docx-existing/review-report.docx`: synthetic report containing Vietnamese text, em dashes, a quotation and source title, comment ranges, tracked insertion/deletion, a footnote, bookmark, cached REF field, hyperlink, image, embedded text attachment, sections, and a custom Named Body style. Case 17 requests only a style line-spacing change. Compare ZIP members before and after: only `word/styles.xml` should change. Confirm the precise style delta. Rendering is read-only; render the delivered file unless the chosen updater would save changes to it. If updating fields could alter protected markup, use a copy and do not treat copy-only results as saved in the delivered file.
- Cases 16 and 18 exercise paper-style selection in DOCX. Case 19 exercises TOC and caption refresh after pagination changes. Case 20 simulates unavailable tools. Earlier cases cover DOCX defaults, language, overrides, personal voice, LaTeX styles, and thesis structure.
- Case 4 verifies that an explicit LaTeX editing request overrides the default DOCX route for reports while preserving the existing project.
- `files/writing/report-evidence.md`: case 21 asks for an evidence-backed course report. Check the visit and survey denominators, citation-to-note mapping, causal restraint and distinction between observed results and proposed work.
- `files/writing/research-revision.md`: case 22 contains deliberately unsupported manuscript claims and a separate evidence appendix. Check that revisions preserve supported facts, correct the percentage claim, remove invented statistical and causal certainty, and identify missing evidence.
- `files/writing/personal-reflection.md`: case 23 asks for a substantial personal rewrite with factual, voice and uncertainty constraints. Check the supplied events and tentative plans without requiring the original wording.

The three writing fixtures are explicitly synthetic and self-contained. Their note IDs are supplied internal evidence, not real publications. Do not search for external references or invent bibliographic metadata to make their references look academic. For case 21, count the title, byline, headings, narrative, table cells, caption and table note, excluding only References. For case 22, count the memo title and body, excluding the editorial note and References.

The bundled course-report DOCX examples use a chapter reset on the first table caption in chapter 2. Keep one reset point per chapter and caption sequence. LibreOffice 26.8 did not honor the `SEQ ... \s 1` reset during rendering, while the explicit `\r 1` reset produced the expected chapter caption numbers; evaluate field behavior in the renderer used by each run.

## Trigger evaluation

`trigger-evals.json` contains 20 realistic queries: 10 intended matches and 10 near-misses. Matches cover academic and personal document writing, revision and formatting, including explicit output overrides. Near-misses cover software documentation, math snippets, editor implementation, data analysis, slides, PDF extraction and file-management tasks. Review these boundaries with the user before measurement.

Measure actual skill invocation in fresh sessions with the unchanged description, recording the model, available skill catalog and tool environment. Use three repeats per query. Count a negative only after a clean completion without invoking the target skill; API errors, unavailable discovery and timeouts remain unverified. Report incomplete coverage separately from trigger accuracy. Keep raw logs and results outside the reusable skill, and do not treat one runtime's results as evidence for every agent platform.

## Verification and grading

Keep these outcomes separate in a supplementary `verification.json` for each run:

| Check | Evidence |
| --- | --- |
| Source/package | Required editable files, semantic structure, requested settings, valid relationships and preservation comparison |
| Build or field refresh | Actual command/tool, exit status, settled citations/references or refreshed native field results |
| Visual inspection | Rendered artifact, inspected page count, layout/glyph findings and any corrections |
| Limitation reporting | Accurate explanation of missing tools and dependent unverified checks |

Use `verified`, `failed`, or `unverified` for each outcome, with a reason and evidence path. A requested PDF that cannot be built remains unverified; clear disclosure can pass the limitation-reporting check but cannot pass the PDF or visual check. Compiler presence alone is insufficient: required fonts, classes and bibliography tools must also work. Source checks do not establish rendered quality.

Grade three dimensions separately. **Artifact correctness** is judged from the delivered files themselves: a correct DOCX or source project can pass even if the executor did not independently validate it. **Verification process** is judged from the transcript, commands, and `verification.json`: an unperformed check fails this process expectation, but does not by itself prove the artifact is wrong. **Reporting accuracy** compares the executor's stated statuses with the evidence; claiming `verified` without evidence fails this dimension. Prefix each corresponding `grading.json` expectation with `[artifact]`, `[process]`, or `[reporting]`, and report pass rates separately for these groups. Do not present one blended pass rate as document quality or as validation quality. Cross-check every process result against the reported status: if a required process check fails while the executor labels that check `verified`, fail reporting accuracy too unless evidence shows the check was not applicable.

Every case has explicit, separate source/package, build/field-refresh, visual and limitation-reporting expectations. For DOCX PAGE fields, rendering the final source and confirming that the visible page number matches final pagination is sufficient; inspect the saved cached PAGE result as well when reporting its package state. For TOC, SEQ, REF and similar cached fields, visual rendering alone does not prove the delivered DOCX contains refreshed results: run a supported updater and save the result, or report refresh as unverified. If a protected format-only edit cannot safely refresh fields in the original, use a separate copy for field updates that may alter markup; read-only rendering may use the delivered file. Do not claim that copy-only field changes were saved in the delivered DOCX. Rendering remains required even when no fields exist. In case 20, the simulated missing tools deliberately leave build and visual checks unverified; source delivery and accurate limitation reporting can still pass.

For the skill-creator viewer, retain its standard `grading.json` fields (`text`, `passed`, `evidence`). Grade artifact existence and correctness from the files, and grade independent validation from the process evidence; do not fail a correct artifact merely because its validation process was not demonstrated. Conversely, a truthful limitation statement does not make an unavailable artifact or unperformed check pass. Keep environmental blockers distinct from demonstrated task failures in the accompanying report. Split mixed expectations about delivery, content, validation, build, visual inspection and reporting into individual checks.

Inspect generated outputs and transcripts before assigning results. Process-routing assertions require transcript evidence; mentioning a reference in a final response is insufficient. Check actual typography, citations and editable structures rather than filenames. For format-only preservation, compare content and protected package parts before and after. For a refreshed TOC, inspect the cached entries and page numbers against the final rendered pages, retaining the native field.

## Writing-quality review

Grade observable requirements from the actual artifact: supplied facts and denominators, citation targets, absence of fabricated evidence, preservation of uncertainty, requested structure and word count. Follow the case-specific word-count boundaries above: case 21 includes its title, byline, headings, narrative, table cells, caption and note, excluding References; case 22 includes the memo title and body, excluding the editorial note and References; case 23 counts the reflection itself. Human review should assess reasoning and voice separately from these objective checks:

| Case | Human review questions |
| --- | --- |
| 21 | Does the report synthesize evidence into a justified recommendation rather than reciting notes? Are caveats proportionate and next steps tied to the evidence gaps? |
| 22 | Does the revision remain useful and readable after removing overclaims? Does the editorial note clearly explain material corrections and evidence needs? |
| 23 | Does the reflection sound like the supplied narrator, with natural flow and less repetition? Does it preserve the modest, tentative tone without adding an uplifting conclusion? |

For blind comparison, present paired outputs in randomized order without version labels, use the same questions for both, and allow a tie. Keep the preference and its rationale separate from factual grades; do not turn stylistic preferences into invented numerical pass rates. Collect user feedback through the skill-creator review viewer before claiming that writing quality improved.

Record benchmark pass rates only for cases actually executed. Use the skill-creator review viewer for human inspection, and report blocked or unverified checks beside any aggregate score. Keep transcripts, rendering images, temporary build files and benchmark workspaces outside the reusable skill package.
