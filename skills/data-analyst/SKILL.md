---
name: data-analyst
description: Guide appropriately scoped analytical investigations and deliver defensible findings, reports, and visualizations. Use when analyzing datasets (CSV, spreadsheets, SQL tables, dataframes), exploring unfamiliar data, defining metrics/KPIs, investigating changes or anomalies, analyzing surveys, experiments, cohorts, funnels or time series, evaluating analyst-level predictions, or building analytical reports and dashboards. Adapts from concise calculations to substantial projects; enforces evidence traceability, meaningful investigation, valid populations and denominators, transparent preparation, and honest completion.
---

# Data Analyst

Turn the user's objective into an evidence-supported answer. Inventory and methodology support analysis; they do not replace findings. Adapt to the available evidence rather than applying every technique or promising predictions from every dataset.

## Start and scale

1. Establish the objective or informational purpose, audience, intended use, questions, deliverables, constraints, and relevant population, grain, units and period. Use supplied context; ask only about consequential ambiguities that cannot be resolved from accessible documentation. Record inferred acceptance criteria as proposed, never as stakeholder agreement.
2. Classify scope. For a focused calculation, inspect the relevant inputs, calculate and verify the answer, and respond concisely with a compact table or equivalent. Do not force lifecycle headings, a dashboard, an intervention, or a model. For open-ended exploration, inspect enough schema and metadata to prioritize useful answerable questions before extensive analysis; revisit that choice as evidence changes.
3. For substantial projects, read [the ten-stage lifecycle](./workflows/analytics-lifecycle.md), [investigation and synthesis](./references/investigation-and-synthesis.md), and [the analytical quality rubric](./references/analytical-quality.md). Define task-specific success criteria before evaluating results. For focused work, use the gates below proportionately; load detailed guidance only if needed.
4. When producing substantial visual artifacts, read [Dashboards and BI](./references/dashboards-and-bi.md) and [Visualization and storytelling](./references/visualization-and-storytelling.md) before choosing the presentation. Use their finding-to-interface coverage map and reader-task review as delivery evidence.
5. Keep three layers separate: this skill provides reusable methods and gates; the project brief supplies domain goals and constraints; the dataset analysis records actual semantics, transformations, findings and evidence. Do not promote assumptions from one project into universal rules.

## Operational gates

Preserve the lifecycle's order of reasoning while iterating when new evidence changes earlier decisions. Modeling includes ordinary queries and statistics, not mandatory machine learning. Record concise gate evidence alongside the work, not ten boilerplate report sections.

| Stage | Required output and evidence to proceed |
|---|---|
| 1. Business Understanding | Brief with prioritized questions, intended use, scope and task-specific acceptance criteria. Unconfirmed assumptions are identified. |
| 2. Analytic Approach | Simplest valid method and comparisons; assumptions, validation and stopping criteria. |
| 3. Data Requirements | Questions mapped to required evidence: answerable, conditional or unsupported; explicit scope revisions. |
| 4. Data Collection | Traceable raw inputs or reproducible extraction with boundaries, coverage and source version. |
| 5. Data Understanding | Inspected records and documentation establish entities, grain, keys, relationships, units and time semantics; quality and selection constraints are assessed. |
| 6. Data Preparation | Reproducible transformations with affected populations; keys, cardinality, counts, denominators and control totals reconcile. |
| 7. Modeling | Questions investigated with justified comparisons and follow-up where material; findings link numerical evidence to interpretation and limits. Profiling alone cannot satisfy a substantial investigation. |
| 8. Evaluation | Separate numerical correctness/functionality, analytical coverage and reader-facing presentation judgments against the contract and rubric; inspect priority reader tasks and record locations/failures. Material gaps block complete delivery. |
| 9. Deployment | Agreed formats are accessible and essential evidence is readable; coverage map reaches inspected interface locations. Displayed evidence reconciles; rendering, interaction and reader-task checks are observed or NOT VERIFIED. |
| 10. Feedback | Actual feedback, changes and relevant stage revisits recorded; unavailable feedback and future outcomes remain pending. |

## Integrity and completion

- Inspect actual data and relevant dictionaries. Column names alone do not establish consequential variable meanings. Preserve raw inputs; document material exclusions, deduplication, imputation and transformations with affected row/entity counts and rationale.
- Define metrics by grain, population, numerator/denominator, units and window. Validate joins and eligibility before aggregating. Distinguish zero, missing and undefined. Respect survey design, temporal availability, censoring and leakage where relevant.
- Prefer the simplest method that answers the question. Examine distributions when a mean represents typical observations, and meaningful comparisons when interpreting change. Full-population accounting totals do not require artificial confidence intervals. Inferential claims require assumptions and appropriate uncertainty.
- Pursue justified follow-up on material findings, then stop when prioritized questions are answered with adequate validation or have concrete evidence blockers and remaining investigations are unlikely to change the scoped conclusion. Do not slice indiscriminately, hunt significance or add models for appearance.
- Distinguish measured facts and observations from interpretation, hypotheses, conclusions, recommendations and limitations. Observational associations do not prove causation without a defensible identification strategy. Recommendations are optional and must fit the request and evidence.
- Review analytical coverage and reader-facing presentation separately from numerical correctness and working controls. For substantial visual delivery, map priority questions through material findings and comparisons to interface locations, including follow-up that changes interpretation. Important findings confined to supporting files are delivery gaps; use the dashboard guidance to review and resolve them.
- Respect explicit delivery requirements and existing tooling. Default to a usable dashboard for substantial visual analysis when no format is specified; use a report when that better serves the agreed task, and compact results for narrow requests. Do not add hosting, refresh infrastructure or an app framework without need.
- Record analysis status separately from delivery status (complete, partial or unverified, with gaps). Material presentation omissions block fully complete delivery even when the analysis is complete; assess each required report/dashboard against its own role.
- Report status as **complete analysis**, **partial analysis**, **feasibility assessment**, or **unverified work**, with scope and blockers. A bounded conclusion that evidence cannot answer a question can be complete for an explicit feasibility request; it is partial against a broader promised investigation. Do not claim universal lifecycle compliance, chronological execution, stakeholder acceptance or future intervention success from a finished artifact.

## Verification evidence

For non-trivial deliverables, preserve a compact ledger linking material checks to executed code/results or substantive review evidence. For simple answers a brief calculation and check suffice.

| Check / quantity and population | Expected condition / tolerance | Method and evidence location | Actual observed value and unit | Status | Effect on conclusion |
|---|---|---|---|---|---|
| Task-specific invariant or material claim | Define before assigning status | Executed calculation or evidence-backed review | The quantity actually tested, not a related count | PASS / FAIL / NOT VERIFIED / NOT APPLICABLE | None, bounded limitation or blocked |

A PASS requires observed evidence satisfying the stated condition. Check that the ledger's quantity, population, unit and condition match the code; derive logged values from the checked variable where practical. Independently recompute critical quantities when practical. Record failed checks and their corrective work; a caveat cannot rescue a materially invalid claim. NOT APPLICABLE requires a scope-based reason, never missing evidence. PENDING describes future feedback/outcomes, not a verification pass. Apply [the quality rubric](./references/analytical-quality.md) at delivery for substantial work; no score average can offset a critical failure.

## Reference routing

Load only guidance relevant to the current question and stage. Read additional references when investigation reaches their subject.

| Need | Reference |
|---|---|
| Detailed stage activities, outputs, gates and iteration | [Analytics lifecycle](./workflows/analytics-lifecycle.md) |
| Question prioritization, feasibility, follow-up, stopping, finding synthesis | [Investigation and synthesis](./references/investigation-and-synthesis.md) |
| Anchored evaluation and completion decision | [Analytical quality](./references/analytical-quality.md) |
| Illustrations of judgment rather than mandatory templates | [Worked examples](./references/analytical-examples.md) |
| Ambiguity, audience, scope and success criteria | [Problem definition](./references/problem-definition.md) |
| Decision trade-offs and commercial context | [Data-driven business](./references/data-driven-business.md) |
| Descriptive, diagnostic, predictive and prescriptive methods | [Analytics types](./references/analytics-types.md) |
| Definitions, ratios, contributions and metric trees | [Metrics and KPIs](./references/metrics-and-kpis.md) |
| Sources, sampling, surveys and acquisition | [Data collection](./references/data-collection.md) |
| Schemas, distributions, relationships and anomalies | [EDA](./references/eda.md) |
| Cleaning, reshaping and transparent transformations | [Data wrangling](./references/data-wrangling.md) |
| Keys, joins, window queries, funnels and cohorts | [SQL for analysis](./references/sql-for-analysis.md) |
| Quality dimensions and reconciliation | [Data quality](./references/data-quality.md) |
| Uncertainty, tests, effect sizes and assumptions | [Statistics and inference](./references/statistics-and-inference.md) |
| Randomization, power and validity threats | [Experimentation](./references/experimentation.md) |
| Confounding and causal identification | [Causal reasoning](./references/causal-reasoning.md) |
| Calendar coverage, seasonality and temporal validation | [Time series](./references/time-series-analysis.md) |
| Analyst-level linear/logistic models, baselines and leakage | [Predictive analysis](./references/predictive-analysis.md) |
| Spatial comparisons | Validate geographic units, boundaries, exposure/population denominators and spatial dependence; use documented domain methods when these references do not suffice. |
| Visual encodings and finding-led reports | [Visualization and storytelling](./references/visualization-and-storytelling.md) |
| Existing BI tools, dashboards, filters and artifact checks | [Dashboards and BI](./references/dashboards-and-bi.md) |
| Warehouse architecture and pipeline triage | [Data engineering](./references/data-engineering.md) |
| Lineage, reruns, privacy and ownership | [Reproducibility and governance](./references/reproducibility-and-governance.md) |

Stay within analyst-level methods. Advanced model training, production MLOps and infrastructure engineering require a separately justified scope and expertise.
