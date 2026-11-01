# Investigation and synthesis

Use this guidance for substantial or open-ended work and when an initial answer needs follow-up. It supplements the existing lifecycle; it does not require another report template.

## Analytical contract and feasibility

Record the objective, audience, intended use, priority questions, deliverables, constraints and analytical acceptance criteria. Identify which were supplied, inferred or confirmed. Success concerns answering questions with valid evidence, not getting a desired result or producing a chart quota. On an unfamiliar dataset, preliminary inspection can precede a final question list; retain scope revisions rather than implying the final plan existed from the start.

For each priority question, map the required population, fields, units, relationships, period and evidence to what is actually available. Classify it as answerable, conditionally answerable (state the condition), or unsupported (state the missing evidence). Resolve consequential meanings through dictionaries, metadata, documentation or targeted clarification. Do not infer sensitive or consequential meanings from column names alone.

When evidence fails, return to approach, requirements or collection. Preserve the original objective and explain the impact of any narrowed scope. A profile of unrelated columns does not satisfy a blocked request; label the changed scope and status.

### Pivot, do not stop

A feasibility verdict alone is a thin deliverable. When the main question is unsupported:

1. State the blocker precisely in one or two sentences: the missing linkage, timing, outcome or field, and what data would remove it.
2. List the questions the data *can* answer that still serve the original purpose. Rank them by usefulness to the reader.
3. Pick the best one or two and analyze them properly: real comparisons, follow-up, findings with numbers. For example, a dataset with outcomes but no usable timing can still show which behaviours differ between outcome groups; a survey without student linkage can still show how practices differ across schools or countries.
4. Lead the report with the finding, and put the feasibility verdict in the summary's status line and in Limitations, not as the headline.
5. Label the result as partial analysis against the original aim. Do not present a substitute question as if it answered the original one, and do not fabricate data to keep the original question alive.

If no related question is worth answering, say so plainly and keep the deliverable short.

## From profiling to investigation

Profiling establishes fitness for use. Investigation answers the question. Select a line of inquiry by relevance, potential magnitude, evidence quality and whether its resolution could change the scoped conclusion. For open-ended work, prioritize a small defensible set of questions after inspecting semantics and coverage; do not apply every method to every column.

For a material initial result:

1. State the observation and what it leaves unresolved. Separate planned comparisons from exploratory discoveries.
2. Choose a discriminating follow-up. Explain what competing explanation or uncertainty it addresses and what would change the conclusion.
3. Execute it when feasible, recording the population, comparison, result and effect on interpretation. A list of proposed analyses is not evidence that follow-up occurred.
4. Challenge the finding with the most consequential alternative explanation or sensitivity check. If blocked, identify exactly what evidence would resolve it and limit the claim.

Possible follow-ups depend on the question: compare within segments or standardize composition after an aggregate shift; compare distributions after a mean change; separate volume from rates; examine cohort age or incomplete follow-up; check calendar coverage and seasonal comparability; inspect event order; distinguish repeated observations from independent entities; examine survey weighting and nonresponse; or validate a baseline using temporal holdout before forecasting. These are choices, not a mandatory checklist.

Use domain-appropriate descriptive, diagnostic, comparative, temporal, spatial, survey, experimental or predictive methods. For spatial rates, validate boundary changes and exposure denominators rather than ranking raw counts alone. For survey estimates, establish target population, sample design, weights and estimand; do not calculate design-based precision from weights alone when cluster/stratum information is missing. For exploratory inference, account for selection and multiplicity; do not describe selected discoveries as prespecified confirmatory tests.

## Challenge and stop

Recompute critical quantities where practical. Assess assumptions, uncertainty, bias, sensitivity, baselines and alternative explanations in proportion to their effect on conclusions. Avoid automatic confidence intervals on descriptive census totals and false precision where sampling design is unknown. Treat confounding, censoring, leakage and distribution shift as material only when they affect the task, then address or bound them explicitly.

Stop when prioritized questions have supported answers or specific blockers, material contradictions have been resolved or visibly bounded, and further feasible work is unlikely to change the intended interpretation at the required precision. If time or access stops work earlier, disclose partial delivery and the highest-value remaining investigation. Do not pad reports with unrelated slices, extra models or limitations detached from claims.

## Synthesize and deliver

Make every major finding traceable to its question, population/comparison, method, numerical evidence and magnitude, uncertainty/limits, interpretation, and implication or next question where relevant. These elements can share a paragraph, figure and evidence link; they need not become repeated headings. Preserve query/script and result locations and definitions so another analyst can reconstruct the claim.

Organize substantial reports around prioritized questions, findings and supporting evidence. Lead with the supported answer and its scope; put extended inventories and methodology in supporting material. Identify answered, partially answered and unsupported questions, with their impact. Recommendations are optional; do not invent stakeholder needs, owners or interventions.

Build dashboard views around the comparisons the reader needs to assess a finding. Explain why the encoding serves that comparison: a distribution for heterogeneity, aligned segment/period views for composition, an interval plot for uncertain differences, or an annotated time series for temporal patterns. Validate the default view and material filtered populations, ratios of sums, empty states and missing periods. A working generic card grid is not proof of analytical value. For substantial visual delivery, carry consequential follow-up into the [finding-to-interface coverage map and reader-task review](./dashboards-and-bi.md), so the supported interpretation survives translation into the interface.

At review, apply [the quality rubric](./analytical-quality.md). If the analysis fails a material gate, return to the earliest corrective stage and rerun affected calculations, findings and visuals. Record what changed. When feedback arrives, distinguish requests that need revised questions/metrics, new data, further analysis or only communication changes, and revisit those stages before asserting completion.
