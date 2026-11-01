# Ten-Stage Data Analytics Methodology

## Contents

- [Ten-Stage Data Analytics Methodology](#ten-stage-data-analytics-methodology)
  - [Contents](#contents)
  - [How to use this workflow](#how-to-use-this-workflow)
  - [1. Business Understanding](#1-business-understanding)
  - [2. Analytic Approach](#2-analytic-approach)
  - [3. Data Requirements](#3-data-requirements)
  - [4. Data Collection](#4-data-collection)
  - [5. Data Understanding](#5-data-understanding)
  - [6. Data Preparation](#6-data-preparation)
  - [7. Modeling](#7-modeling)
  - [8. Evaluation](#8-evaluation)
  - [9. Deployment](#9-deployment)
  - [10. Feedback](#10-feedback)
  - [Verification ledger](#verification-ledger)
  - [Going back](#going-back)

## How to use this workflow

John Rollins' data science methodology (CRISP-DM based) answers ten questions in order, grouped in five pairs:

| Pair | Stage | Question it answers |
| --- | --- | --- |
| From problem to approach | 1. Business Understanding | What is the problem you are trying to solve? |
|  | 2. Analytic Approach | How can you use data to answer the question? |
| From requirements to collection | 3. Data Requirements | What data do you need to answer the question? |
|  | 4. Data Collection | Where is the data coming from, and how will you get it? |
| From understanding to preparation | 5. Data Understanding | Is the data you collected representative of the problem? |
|  | 6. Data Preparation | What additional work is needed to manipulate and work with the data? |
| From modeling to evaluation | 7. Modeling | In what way can the data be visualized or modeled to get the required answer? |
|  | 8. Evaluation | Does the model really answer the initial question, or does it need adjusting? |
| From deployment to feedback | 9. Deployment | Can you put the result into practice? |
|  | 10. Feedback | Can you get constructive feedback to improve the answer? |

The stages are an order of reasoning, not a report outline. Real work loops back: profiling reveals a problem, a finding raises a new question, feedback changes the population. When that happens, return to the stage that owns the decision, fix it, and note the change in `NOTES.md`. Modeling and evaluation in particular run as a loop.

Scale each stage. For a focused question several stages take one sentence of thought. For a substantial project each stage leaves a short record in `NOTES.md` (a few lines or a small table, not boilerplate). Mark a stage **NOT APPLICABLE** only when the task genuinely does not need it; missing data or unrun checks stay visible as limitations.

The most common failure is rushing into data collection and analysis before framing the problem. Spend real thought on stages 1–3.

## 1. Business Understanding

**Question**: What is the problem you are trying to solve?

**Do**

- **Purpose and reader.** State what the reader needs to decide or learn. For exploratory or informational work, begin with that purpose and inspect the data and its documentation to refine answerable questions; the absence of a business decision does not make the analysis unready.
- **Business goal and decision, when applicable.** For work intended to guide a decision or intervention, identify the goal, decision-maker, action and what success means. Narrow the analysis to evidence that can inform that choice.
- **SMART goal, when a target is needed.** For a decision or intervention with a meaningful target and timeframe, restate it as Specific, Measurable, Achievable, Relevant and Time-bound. Do not invent a target for exploratory work.
- **KPIs, when evaluating a decision or intervention.** Pick a primary KPI that shows whether the goal is met and secondary measures that capture relevant effects or guardrails. Define each by population, numerator/denominator, unit and window. For exploratory work, define the analytical measures needed to answer the questions instead of forcing intervention KPIs.
- **Requirements from stakeholders.** When a stakeholder is available, ask: What are your business goals? How do you define success, and what metric shows it? What are your biggest challenges? What decisions will you make from this analysis? What risks do you see, and what would stop you using it? Synthesize input: organize → identify themes → prioritize → refine questions → validate themes. When the user is available and a consequential answer is missing, grill them one question at a time with [grilling](../references/grilling.md) before finalizing the brief. When no stakeholder is available, write these answers as _proposed_ assumptions.
- **Domain knowledge.** Use it to ask relevant questions, read numbers in context, choose methods suited to the domain and sanity-check results. Read the dataset documentation and domain sources before deciding what a field means.
- **Business questions → analytical questions.** Turn each vague business question into a set of analytical questions that are **Clear** (no ambiguity, assumptions explicit), **Specific** (one aspect each), **Scoped** (population, period), **Data-oriented** (names the data needed) and **Answerable** (you know what the answer looks like, its unit and a plausible range). Example: "How successful was my campaign?" → "What was the overall positive response rate for the Q3 campaign?", "How did it differ by channel?", "…by demographic group?"
- **Classify the decision.** Strategic, tactical or operational; programmed (recurring) or non-programmed (one-off); one-way door (hard to reverse) or two-way door (reversible). Irreversible, strategic decisions justify more rigor; reversible operational ones need a fast, good-enough answer.
- **Deliverable.** Agree or propose the format: inline answer, report, dashboard, or the user's own required structure. Check the [playbooks](../SKILL.md#playbooks) for a matching problem type.

**Produce**: a proportionate brief in `NOTES.md` — purpose, reader, prioritized analytical questions, scope and deliverable; include business/SMART goals and primary/secondary KPIs when a decision or intervention needs them, otherwise mark them not applicable. Label proposed assumptions.

**Gate**: questions pass the Clear/Specific/Scoped/Data-oriented/Answerable test; define decision success criteria, metric definitions, grain and period when they affect the answer.

**References**: [Problem definition](../references/problem-definition.md), [Data-driven business](../references/data-driven-business.md), [Metrics and KPIs](../references/metrics-and-kpis.md)

## 2. Analytic Approach

**Question**: How can you use data to answer the question?

**Do**

- **Match each question to an analytics type**:
  - _Descriptive_ — what happened / current status → descriptive statistics, summaries, KPIs, charts.
  - _Diagnostic_ — why did it happen → segmentation, drill-down, correlation, root-cause analysis, inferential statistics.
  - _Predictive_ — what will happen next → forecasting, classification or regression with baselines and holdouts.
  - _Prescriptive_ — what should we do → what-if scenarios, optimization, decision analysis under uncertainty.
- **Match the model to the requirement**: probabilities of an outcome → predictive model; relationships → descriptive model; yes/no answer → classification; natural segments → clustering. Causal questions need an identification strategy (experiment or quasi-experiment).
- Name the comparison that answers each question (before vs after, group vs group, model vs baseline) and the baseline a reader would use without your analysis.
- Name the alternative explanation most likely to fool you and how you will test it.
- Decide when to stop: priority questions answered or concretely blocked, and further work unlikely to change the answer.

**Produce**: one line per question in `NOTES.md`: analytics type, method, comparison, baseline, main threat.

**Gate**: the approach can answer the question with feasible evidence; the simplest adequate method is chosen.

**References**: [Analytics types](../references/analytics-types.md), [Statistics and inference](../references/statistics-and-inference.md), [Causal reasoning](../references/causal-reasoning.md), [Predictive analysis](../references/predictive-analysis.md)

## 3. Data Requirements

**Question**: What data do you need to answer the question?

**Do**

- **Step 1 — outcomes of interest**: which measured outcome answers each question (the KPI, the target event)?
- **Step 2 — context data**: which data explains the outcome — who (entity attributes), what (products, courses), when (time), where (region, channel), how (behaviour, events)?
- For each, specify content, format, grain, keys, period, population, and the measurement scale (nominal, ordinal, interval, ratio; discrete vs continuous; time series vs cross-sectional), because the scale decides valid summaries and methods.
- Know the data type you need: reference data (permitted values), master data (entities), transactional data (events), metadata and the data dictionary.
- **Map availability**: mark each question **answerable**, **conditional** (state the condition) or **unsupported** (state exactly what is missing). For unsupported questions, narrow the question, collect more data (with permission), or pivot to the most valuable related question the data supports.

**Produce**: a question → required data → available data → status table in `NOTES.md`.

**Gate**: every priority question has a status; gaps trigger a revision rather than silent substitution.

**References**: [Data collection](../references/data-collection.md), [Data quality](../references/data-quality.md), [Investigation and synthesis](../references/investigation-and-synthesis.md)

## 4. Data Collection

**Question**: Where is the data coming from (all sources), and how will you get it?

**Do**

- Use supplied data first. Identify all relevant sources — structured, semi-structured and unstructured; internal (databases, files, experiments, proofs of concept, surveys) and external (open, government, purchased; first-, second- or third-party).
- Collect the minimum relevant data. Merge sources where needed, eliminate redundant data, and defer data that is inaccessible — recording it as a gap.
- If collection reveals gaps, go back to Data Requirements.
- **Privacy and ethics**: analyze only data you are authorized to use; work in a secure environment; remove or pseudonymize personal identifiers before sharing outputs; use data and insights fairly and for the stated benefit. Do not expose individual records in shared reports or dashboards.
- Record source, version or download date (only if known — never invent one), filters, row counts and coverage. Keep raw inputs untouched.

**Produce**: a source inventory in `NOTES.md` (source, owner, format, coverage, access, sensitivity); extraction code in `code/`.

**Gate**: inputs trace to their source; missing coverage is resolved or disclosed before claims depend on it; sensitive data is handled appropriately.

**References**: [Data collection](../references/data-collection.md), [Data engineering](../references/data-engineering.md), [Reproducibility and governance](../references/reproducibility-and-governance.md)

## 5. Data Understanding

**Question**: Is the data you collected representative of the problem to be solved?

**Do**

- **Profile first**: run `scripts/profile_data.py` for record counts, column types, fill rates, distinct values, candidate keys and duplicates. Then read actual records and the metadata (how was it collected or generated? what quality?).
- **Move from native view to analytics view**: establish entities, grain, keys, relationships, units, category codes, measurement scales and time semantics (what does each date record: event, submission, logging, release?).
- **Descriptive statistics and visualization**: central tendency (mean, median, mode), position (percentiles, quartiles), spread (range, SD, IQR, coefficient of variation) and shape (skew: right skew means mean > median). Central tendency alone is never enough. Use histograms and box plots for distributions, scatter plots and correlation heatmaps for relationships, line charts for time.
- **Assess data quality** against the dimensions that matter for this task (Southekal's twelve): completeness, consistency, conformity (validity), uniqueness, correctness, accuracy, accessibility, security, timeliness, redundancy, coverage, integrity. For each relevant dimension record the evaluation criterion, what you found and its consequence. When a scored quality report is requested (e.g., a 1–5 score per dimension), base each score on the measured criterion.
- Look for the usual mess: bad formats, trailing spaces, duplicates, empty rows, synonyms and abbreviations, scale differences, skew and outliers, missing values (also coded as "?", 0, N/A or blank).
- **Representativeness**: does the population, period and coverage match the problem? Check selection effects, missingness patterns across groups and periods, and join fanout.
- Note preliminary insights, and whether more data is needed. If the data cannot support the approach, go back to stage 2 or 3.

**Produce**: data dictionary notes and a data quality summary in `NOTES.md` (dimension → criterion → finding → consequence).

**Gate**: meanings come from records and documentation, not column names; quality issues and representativeness limits are known well enough to prepare and analyze responsibly.

**References**: [EDA](../references/eda.md), [Data quality](../references/data-quality.md), [SQL for analysis](../references/sql-for-analysis.md)

## 6. Data Preparation

**Question**: What additional work is required to manipulate and work with the data?

**Do**

- **Blend**: combine sources with joins and unions; check join cardinality so joins do not multiply rows.
- **Clean** with the checklist: character variables have valid values; numeric variables are in range; missing values and duplicates are handled; ID variables are unique; dates are valid; files that need combining are combined.
- **Missing values**: check with the source first. Options — drop the variable or the rows, impute (zero, mean/median, mode, similar records or interpolation, a model), mask with a "missing" category, or leave missing. Choose by why data is missing; record what you chose and how many rows it affects. Never treat "missing" as zero by default.
- **Outliers**: ask whether each is an error or legitimate and whether it belongs to the population. Detect with plots, IQR rules, z-scores or residuals. Correct, remove, transform, treat as missing, or keep and use robust methods (medians, resistant models) — and document the choice.
- **Format and transform**: standardize units and formats; extract date parts (month, weekday, elapsed time); encode categories (ordinal → ordered codes, nominal → dummy/one-hot); bin numbers when categories serve the question; normalize (min-max, z-score) when scales differ for modeling. Check strongly correlated features (multicollinearity).
- **Feature engineering**: build variables that answer the questions — and for predictive work, only from information available at the prediction time.
- **Sampling** (when data is too large or for surveys): set the margin of error and confidence level, record the sampling frame, seed and size.
- Reconcile row counts at each step, key uniqueness, control totals and denominators. Validate consequential transformations with stakeholders or documentation. A good plan today beats a perfect plan tomorrow: prepare what the questions need, not everything possible.

**Produce**: reproducible prepared tables (or queries) plus a preparation log in `NOTES.md` (step → rows/entities affected → reason).

**Gate**: grain, keys, counts and totals reconcile; every material exclusion, imputation or transformation is recorded with affected counts.

**References**: [Data wrangling](../references/data-wrangling.md), [SQL for analysis](../references/sql-for-analysis.md), [Data quality](../references/data-quality.md)

## 7. Modeling

**Question**: In what way can the data be visualized or modeled to get the answer required?

**Do**

- Run the planned analysis: descriptive aggregations and visualizations, diagnostic drill-downs and decompositions, cohort/funnel analyses, statistical comparisons, or baseline-first predictive models (descriptive vs predictive as chosen in stage 2). Sometimes a well-chosen visualization is the whole model.
- For each material initial result, ask what else could explain it and run the check that tells the explanations apart (within-segment comparison, standardization, alternative definition, sensitivity, later holdout). Record: observation → why follow up → result → how the interpretation changed.
- **Form and challenge hypotheses**: state what you think explains the pattern, then actively look for evidence that would disprove it. Be aware of your own bias (confirmation, anchoring) before concluding.
- Quantify magnitude and, where inference is claimed, uncertainty.
- Draft each finding in the report voice: claim, number, comparison, meaning, main limit. Draft its chart with `scripts/chart_style.py`.
- Stop when the stage 2 stopping rule is met. Do not slice indiscriminately, hunt significance or add models for appearance.

**Produce**: result tables in `results/`, charts in `figures/`, draft findings.

**Gate**: every finding traces to code and numbers, has a comparison, and has survived its most plausible alternative or carries that limit. Profiling alone cannot pass this gate for a substantial investigation.

**References**: [Investigation and synthesis](../references/investigation-and-synthesis.md), [Statistics and inference](../references/statistics-and-inference.md), [Experimentation](../references/experimentation.md), [Causal reasoning](../references/causal-reasoning.md), [Time series](../references/time-series-analysis.md), [Predictive analysis](../references/predictive-analysis.md), [Visualization and storytelling](../references/visualization-and-storytelling.md)

## 8. Evaluation

**Question**: Does the model or analysis really answer the initial question, or does it need adjusting?

**Do**

- **Answer check**: re-read the brief. Does each analytical question have an answer, a partial answer with a stated blocker, or an explicit unsupported status? Does the result meet the SMART goal's success criteria?
- **Diagnostic check — does it work as intended?** Independently recompute decision-critical numbers (different code path or query); check leakage, wrong denominators, residuals and errors; for models, evaluate on held-out data (temporal holdout or cross-validation) against baselines with metrics suited to the decision.
- **Statistical check — is it real?** Check significance and uncertainty where inference is claimed (intervals, effect sizes; account for multiple comparisons). Avoid unsupported causal language.
- Fill the [verification ledger](#verification-ledger).
- Review against [the quality rubric](../references/analytical-quality.md) privately. Fix what fails, iterating with Modeling; do not write self-assigned scores into a deliverable.

**Produce**: ledger in `NOTES.md`; status: complete analysis, partial analysis, feasibility assessment or unverified work.

**Gate**: no critical failure; material claims are supported; failed checks are fixed or the claim is removed or limited.

**References**: [Analytical quality](../references/analytical-quality.md), [Data quality](../references/data-quality.md), [Statistics and inference](../references/statistics-and-inference.md)

## 9. Deployment

**Question**: Can you put the result into practice?

**Do**

- **Communicate in the required format**: follow the user's explicit format or outline first. Otherwise use the project's existing report or BI tooling. If neither applies, build from `assets/report-template.html` and add `assets/dashboard-template.html` when interactive exploration helps. Structure it with the Pyramid principle (answer first, then supporting findings) and keep to about three key messages (Rule of Three). Tell the story: highlight what matters, arrange for clarity, sequence the findings.
- Address every relevant stakeholder — direct, indirect, upstream, downstream — at the right level of detail.
- Open the rendered artifact. Check that numbers match `results/`, charts render, filters work, and that the main findings are readable in the artifact itself (not only in linked CSV or Markdown).
- **Plan the rollout** when the result will be used operationally: start with a limited group or test setting, state how it will be monitored and maintained, and what would trigger a change. Give users time and guidance to adopt it.
- Give the reader the path or link and how to rerun.

**Produce**: report and/or dashboard, with `code/` and `results/` alongside; a rollout and monitoring plan when relevant.

**Gate**: the artifact opens, shows the findings and their key comparisons, and its values reconcile. Checks you could not run are listed as NOT VERIFIED.

**References**: [Visualization and storytelling](../references/visualization-and-storytelling.md), [Dashboards and BI](../references/dashboards-and-bi.md), [Example report](../references/example-report.md)

## 10. Feedback

**Question**: Can you get constructive feedback to improve the answer?

**Do**

- Record actual feedback from users and stakeholders and what it changed. If none has arrived, say feedback is pending; never invent acceptance.
- **Set up a review mechanism** for decisions made from the analysis: baseline, target, guardrails, evaluation window, owner, review date. Mark the outcome PENDING until data exists. Ask: did the decision lead to the intended outcome? Are stakeholders satisfied? What is the long-term impact?
- Fail, fix and learn fast: route feedback to the right stage — a new question to stage 1, a new population to stage 3, a data issue to stage 5–6, a wording problem to stage 9 — then refine and redeploy. Re-verify what changed.

**Produce**: a feedback log and, where relevant, an outcome evaluation plan in `NOTES.md`.

**Gate**: observed feedback and outcomes are distinguished from plans.

**References**: [Data-driven business](../references/data-driven-business.md), [Experimentation](../references/experimentation.md), [Dashboards and BI](../references/dashboards-and-bi.md)

## Verification ledger

Keep a compact ledger in `NOTES.md` for every non-trivial deliverable. Include only checks that protect a material claim.

| Check (quantity, population) | Expected condition | Method / evidence | Observed | Status | Effect |
| --- | --- | --- | --- | --- | --- |
| Joined order revenue equals source total | Equal to the cent | `code/checks.py::revenue_total` | 300.00 = 300.00 | PASS | None |

Rules that keep it honest:

- State the condition before assigning a status. PASS means the condition was evaluated and met.
- Log the quantity the code actually checked (unique users are not response rows).
- Status is PASS, FAIL, NOT VERIFIED or NOT APPLICABLE (scope reason only, never "no evidence"). PENDING is for future outcomes, not checks.
- A FAIL sends the work back to the stage that caused it, or removes or limits the affected claim. A caveat cannot rescue an invalid number.
- Prefer executable checks. Add a reusable script only after the same check recurs across analyses.

## Going back

- **Question or approach fails** → stage 1 or 2.
- **Missing fields, coverage or access** → stage 3 or 4, or pivot.
- **Profiling or reconciliation finds a problem** → stage 5 or 6.
- **Contradictory findings or failed checks** → the stage whose method or data caused them.
- **Rendering defects** → stage 9. **New stakeholder questions** → stage 1.

Related: Kevin Hanegan's 12-step data-informed decision-making process (Ask → Acquire → Analyze → Apply → Announce → Assess) covers the same ground from the decision-maker's side. Its Apply steps (form a hypothesis, try to disprove it, mitigate bias) are folded into stage 7, its Announce steps (Pyramid principle, Rule of Three, all stakeholders) into stage 9, and its Assess step into stage 10.
