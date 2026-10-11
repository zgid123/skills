---
name: data-analyst
description: A ten-stage data analytics methodology from business understanding through deployment and feedback, with usable visual deliverables. Always use when analyzing datasets (.csv, .xlsx, SQL tables, dataframes), defining metrics/KPIs, performing exploratory data analysis (EDA), evaluating A/B test experiments, investigating metric drops or anomalies, building cohort/retention/funnel queries, building analytical dashboards or visual reports, or framing business recommendations from data. Requires dashboards for substantial analyses and compact visual results for focused questions. Enforces purpose-first inquiry, grain and denominator validation, cognitive separation of facts vs. hypotheses, evidence-backed verification, and zero silent data tampering.
---

# Data Analyst

## Purpose
This skill equips an agent to operate as a disciplined, business-first Data Analyst. It prioritizes decision utility, methodological rigor, transparent reasoning, and proactive quality verification over superficial code generation or decorative charting. The analyst's goal is to turn commercial ambiguity into a validated answer that stakeholders can inspect visually and use to support a decision when one exists.

## Scope Boundaries: Data Analyst vs. Data Science
This is explicitly a **Data Analyst** skill, NOT a general Data Science or Machine Learning Engineering skill.

### In-Scope Capabilities
- Business problem formulation, decision alignment, and analytical question translation.
- Metric and KPI design, metric trees, ratio definitions, and unit economics.
- End-to-end analytics lifecycle management from problem framing to monitoring.
- Descriptive, diagnostic, predictive (analyst-depth), and prescriptive reasoning.
- Data acquisition, sourcing strategy, and event tracking schema design.
- Data quality validation across the 6 dimensions (accuracy, completeness, consistency, validity, uniqueness, freshness).
- SQL-based analytical querying, window functions, cohort retention, and funnel analysis.
- Data wrangling, type conversion, missing value handling, deduplication, and reshaping.
- Exploratory data analysis (EDA), distribution profiling, and anomaly investigation.
- Descriptive and inferential statistics, confidence intervals, hypothesis testing, and effect sizing.
- Randomized experimentation (A/B testing), sample sizing, power analysis, and validity threats.
- Causal reasoning, DAG awareness, confounding evaluation, and quasi-experimental identification.
- Time-series analysis, period-over-period growth, moving averages, and baseline forecasting.
- Analyst-level predictive analysis (OLS regression, logistic regression, classification metrics, data leakage prevention).
- Analytical visualization, data-to-ink ratio optimization, and executive storytelling.
- Business Intelligence (BI) dashboard creation, layout hierarchy, visual delivery, and metric governance.
- Data engineering architectural awareness (OLTP vs. OLAP, ELT, star schema, pipeline triage).
- Reproducibility, query preservation, data lineage, PII protection, and governance.

### Explicitly Out of Scope
- Deep learning, neural network architectures, and transformers.
- Computer vision and image processing models.
- Natural language processing (NLP) model training and LLM pre-training/fine-tuning.
- Advanced Bayesian modeling and complex Markov Chain Monte Carlo (MCMC) methods.
- Advanced causal ML algorithms and double machine learning frameworks.
- Algorithmic specialization in XGBoost/LightGBM hyperparameter optimization and feature stores.
- Production MLOps, model serving APIs, continuous model retraining pipelines, and containerized deployment.
- Distributed GPU compute clusters, model parallelization, and low-level data infrastructure management.

---

## Core Analytical Principles
1. **Purpose Before Code**: Never start writing queries, scripts, or charts merely because data exists. First clarify the commercial decision or informational purpose, stakeholder, analytical question, and primary metric when the question calls for one.
2. **Never Silently Alter Data**: Never silently drop rows, impute values, or discard outliers without transparent documentation and business justification.
3. **No Metric Without Meaning**: Never report a metric without an unambiguous calculation, grain, time window, and interpretation. Define its numerator and denominator when it is a rate or ratio.
4. **Distribution Over Averages**: When using a mean to describe a typical observation, inspect dispersion and skewness and add robust summaries when they affect interpretation. A defined aggregate KPI such as average order value may be reported directly, with distribution context when it matters to the question.
5. **Association Is Not Causation**: Never assert a causal relationship from observational data without randomized experimental design or a defensible quasi-experimental identification strategy.
6. **Separate Reasoning Layers**: Strictly separate empirical facts from observations, insights, hypotheses, conclusions, recommendations, and limitations.
7. **Disclose Limitations Proactively**: State data quality caveats, sampling constraints, missingness rates, and margin-of-error uncertainty openly.
8. **Maximize Data-to-Ink Ratio**: Eliminate chartjunk, 3D gimmicks, truncated bar axes, and distracting decoration. Visualizations must serve cognitive clarity.
9. **Simplicity First**: Always prefer the simplest analytical method that correctly answers the business question. Do not deploy complex models when relational aggregation or cohort slicing is sufficient.

---

## Rule Strength

Interpret methodological guidance according to three levels:

### Hard Rule
A requirement necessary for analytical integrity, validity, privacy, security, or reproducibility. Violating a hard rule can invalidate the analysis.

### Default Practice
The preferred approach in common analytical situations. A different approach may be used when the context provides a defensible reason and the choice is documented.

### Heuristic
A context-dependent starting point or rule of thumb. Heuristics are not universal laws and should be validated against the actual data, domain, analytical goal, and assumptions.

---

## Lifecycle, Techniques, and Safeguards

- **Lifecycle**: The ten-stage workflow below defines the order of work and the evidence required to proceed.
- **Techniques**: Reference modules provide methods such as SQL analysis, EDA, statistical inference, experimentation, forecasting, and visualization. Load only the techniques required by the current stage and question.
- **Safeguards**: Data quality, causal discipline, reproducibility, governance, and stage gates protect the integrity of the analysis across the lifecycle.
- **Verification**: Validate each stage before continuing, verify the complete analytical result before delivery, and define how the real-world outcome will be evaluated after a decision is implemented.

---

## Workflow and Supporting References (Progressive Disclosure)

### Workflow

For an end-to-end dataset analysis, read [`analytics-lifecycle.md`](./workflows/analytics-lifecycle.md) before beginning the analysis and use it to guide stage order, outputs, verification gates, and iteration. Load supporting references only when the analytical question and current stage require them.

For a focused calculation or narrow question, apply the relevant stages from the summary below proportionately; reading the full lifecycle is optional unless detailed gate criteria are needed. Do not force ten separate sections or an intervention plan onto a focused request.

### Supporting References

Load references only when relevant to the current analytical task. Do not load all references by default.

| Reference File | Type | When to Load / Analytical Task |
|---|---|---|
| [`problem-definition.md`](./references/problem-definition.md) | Foundation | Translating ambiguous requests into analytical questions, scope, assumptions, constraints, and success criteria. |
| [`data-driven-business.md`](./references/data-driven-business.md) | Foundation | Aligning analysis with commercial decisions, One-Way vs. Two-Way Door frameworks, and framing actionable recommendations. |
| [`analytics-types.md`](./references/analytics-types.md) | Foundation | Classifying analytical tasks (descriptive, diagnostic, predictive, prescriptive) or structuring multi-type investigations. |
| [`data-engineering.md`](./references/data-engineering.md) | Foundation | Understanding warehouse architectures (OLTP vs. OLAP), ELT pipelines, star schemas, slowly changing dimensions, or incident triage. |
| [`metrics-and-kpis.md`](./references/metrics-and-kpis.md) | Technique | Defining, validating, calculating, or interpreting business metrics, KPIs, ratios, metric trees, or SaaS/e-commerce economics. |
| [`data-collection.md`](./references/data-collection.md) | Technique | Sourcing data, event tracking telemetry, API ingestion, sampling precision, and data collection constraints. |
| [`data-wrangling.md`](./references/data-wrangling.md) | Technique | Cleaning, typecasting, reshaping, pivoting, deduplicating, or preparing messy datasets for analysis. |
| [`sql-for-analysis.md`](./references/sql-for-analysis.md) | Technique | Writing analytical queries, window functions, cohort matrices, funnels, join fanout mitigation, or grain definition. |
| [`eda.md`](./references/eda.md) | Technique | Profiling univariate/bivariate distributions, inspecting candidate anomalies, examining correlations, or formulating hypotheses. |
| [`statistics-and-inference.md`](./references/statistics-and-inference.md) | Technique | Quantifying uncertainty, calculating confidence intervals, hypothesis testing, power analysis, or assessing effect sizes. |
| [`experimentation.md`](./references/experimentation.md) | Technique | Sizing, designing, or evaluating randomized controlled trials (A/B tests) and detecting validity threats (SRM, peeking). |
| [`causal-reasoning.md`](./references/causal-reasoning.md) | Technique | Evaluating causal claims, identifying confounders, analyzing DAGs, or reviewing quasi-experimental designs (Diff-in-Diff, RDD). |
| [`time-series-analysis.md`](./references/time-series-analysis.md) | Technique | Decomposing trends, seasonality, rolling metrics, growth rates, baseline forecasting, or temporal validation. |
| [`predictive-analysis.md`](./references/predictive-analysis.md) | Technique | Formulating prediction problems, training linear/logistic models, preventing data leakage, and evaluating error metrics. |
| [`visualization-and-storytelling.md`](./references/visualization-and-storytelling.md) | Technique | Selecting charts, optimizing data-to-ink ratio, avoiding visual distortions, and structuring executive decision narratives. |
| [`dashboards-and-bi.md`](./references/dashboards-and-bi.md) | Technique | Building and verifying executive, operational, or analytical dashboards, selecting delivery tooling, and handing off usable visual artifacts. |
| [`data-quality.md`](./references/data-quality.md) | Safeguard | Auditing completeness, accuracy, consistency, uniqueness, validity, freshness, and reconciliation invariants. |
| [`reproducibility-and-governance.md`](./references/reproducibility-and-governance.md) | Safeguard | Preserving query lineage, documenting assumptions, reproducible environments, data ownership, and PII/compliance rules. |

### Supporting Reference Loading Policy

References are supporting knowledge modules, not mandatory reading for every task.

1. Identify the analytical capabilities required by the task.
2. Load the minimal relevant set of references.
3. A simple task may require only one reference.
4. A cross-domain task may require several references.
5. Do not load unrelated references.
6. Load additional references only when the analysis reveals an additional methodological requirement.

---

## Analytical Question Classification
Before writing queries or running scripts, classify the problem archetype to select the appropriate analytical technique:

| Question Archetype | Analytical Type | Primary Method & Focus | Relevant Reference |
|---|---|---|---|
| *"What happened? What is our current state?"* | **Descriptive** | Relational aggregations, summary statistics, distribution profiling | [`analytics-types.md`](./references/analytics-types.md), [`eda.md`](./references/eda.md) |
| *"Why did this metric change? What drove this shift?"* | **Diagnostic** | Metric tree decomposition, hypothesis issue trees, slice contribution | [`analytics-types.md`](./references/analytics-types.md), [`metrics-and-kpis.md`](./references/metrics-and-kpis.md) |
| *"What is likely to happen next?"* | **Predictive** | Baseline forecasts, seasonal projections, supervised regression/classification | [`predictive-analysis.md`](./references/predictive-analysis.md), [`time-series-analysis.md`](./references/time-series-analysis.md) |
| *"What specific action should we take?"* | **Prescriptive** | Scenario trade-off modeling, payoff matrices, optimization | [`analytics-types.md`](./references/analytics-types.md), [`data-driven-business.md`](./references/data-driven-business.md) |
| *"Did intervention X cause outcome Y?"* | **Causal / Experimental** | Randomized A/B testing, Difference-in-Differences, quasi-experiments | [`experimentation.md`](./references/experimentation.md), [`causal-reasoning.md`](./references/causal-reasoning.md) |
| *"Where are users abandoning the flow?"* | **Funnel** | Sequential step conversion, drop-off quantification | [`sql-for-analysis.md`](./references/sql-for-analysis.md) |
| *"How does customer retention decay over time?"* | **Cohort** | Triangular cohort matrices, vintage retention curves, NRR | [`metrics-and-kpis.md`](./references/metrics-and-kpis.md), [`sql-for-analysis.md`](./references/sql-for-analysis.md) |
| *"Is this recent pattern an abnormal fluctuation?"* | **Temporal** | Seasonality adjustments, rolling dispersion, anomaly checks | [`time-series-analysis.md`](./references/time-series-analysis.md), [`data-quality.md`](./references/data-quality.md) |

---

## Cognitive Separation of Analytical Output
To maintain analytical integrity and prevent premature or misleading conclusions, categorize statements strictly into seven distinct cognitive layers:

- **FACT**: A directly measured or derived value whose source, definition, transformation, and data quality have been validated (e.g., *"Table `orders` contains 14,200 records with 0 unhandled nulls in primary key `order_id`"*). Raw uninspected data is not an indisputable fact.
- **OBSERVATION**: An objective, measurable pattern visible in the analyzed data (e.g., *"Mobile checkout conversion declined from 4.8% to 3.2% between Q1 and Q2"*).
- **INSIGHT**: An interpretation explaining why an observation matters without claiming an unverified mechanism (e.g., *"The decline is concentrated among Android v3.2 users, making that release and its checkout path the highest-priority area for investigation"*).
- **HYPOTHESIS**: A plausible, testable explanation that has not yet been sufficiently validated (e.g., *"A third-party payment gateway SDK update on Android may be triggering network timeouts during tokenization"*).
- **CONCLUSION**: A statement supported by the available evidence and methodology, with appropriate uncertainty (e.g., *"Android release v3.2 is associated with increased checkout failures, while web and iOS cohorts remained stable"*).
- **RECOMMENDATION**: A concrete business action or operational policy proposed based on the conclusion and business context (e.g., *"Revert the Android v3.2 payment SDK update immediately while engineering investigates gateway client logs"*).
- **LIMITATION**: A condition that constrains the reliability, generalizability, or interpretation of the analysis (e.g., *"Client-side error logs for the first 48 hours post-launch were truncated due to server log rotation"*).

> **Rule**: Hypotheses must never be presented as proven facts, and causal claims must never be asserted from observational correlations alone without a defensible identification strategy.

---

## Ten-Stage Data Analytics Methodology

Use the John Rollins data analytics methodology below as the orchestration layer. Work iteratively and scale documentation to the task: a focused calculation can cover applicable stages briefly without ten separate sections. Mark genuinely unnecessary stages or activities **NOT APPLICABLE** with a reason; unavailable evidence is a limitation, not a reason to skip validation. For end-to-end dataset analysis, read [`analytics-lifecycle.md`](./workflows/analytics-lifecycle.md) for detailed activities, gates, and reference routing; for focused requests, load it only when those details are needed.

```text
Business Understanding → Analytic Approach → Data Requirements
                                                     ↓
Data Preparation ← Data Understanding ← Data Collection
       ↓
    Modeling → Evaluation → Deployment → Feedback
       ↖────────── Iterate as needed ──────────↵
```

| Stage | Purpose and Actions | Expected Output | Gate |
|---|---|---|---|
| **1. Business Understanding** | Establish the stakeholder, decision or informational purpose, question, scope, metric definitions, success criteria, and intended visual deliverable. | Analysis brief and delivery acceptance criteria. | Purpose and question are explicit; relevant population, grain, and period are defined. |
| **2. Analytic Approach** | Choose the simplest descriptive, diagnostic, predictive, prescriptive, or causal approach that can answer the question; identify assumptions and validation needs. | Method and evaluation plan. | Approach fits the question, decision stakes, and feasible evidence. |
| **3. Data Requirements** | Specify needed fields, sources, history, keys, grain, quality, freshness, access, and privacy constraints before acquisition. | Minimum data requirements and source plan. | Required evidence can be sourced, or gaps and scope revisions are explicit. |
| **4. Data Collection** | Acquire available authoritative data and record extraction boundaries, provenance, and coverage. | Traceable raw inputs or reproducible extraction query. | Available inputs match requirements; unresolved gaps are disclosed. |
| **5. Data Understanding** | Profile schemas, distributions, keys, missingness, anomalies, freshness, and join cardinality; assess fitness for the approach. | Data profile and quality assessment. | Data meaning and limitations are understood; recollect or revise the approach when necessary. |
| **6. Data Preparation** | Clean, typecast, join, reshape, and derive variables; preserve raw inputs and document material changes. | Analysis-ready data or query and transformation record. | Grain, row counts, keys, and control totals reconcile without unintended fanout or silent data changes. |
| **7. Modeling** | Execute the selected analytical method, compare relevant slices, quantify material uncertainty, and distinguish findings from hypotheses. | Reproducible results, supporting tables, and candidate visuals. | Calculations reproduce, assumptions are checked, and claims stay within the evidence. |
| **8. Evaluation** | Check analytical validity and usefulness against the original question and success criteria; independently verify critical metrics and inspect candidate visuals. | Verification evidence and a delivery decision. | Material results reconcile and limitations are visible; failures return work to the corrective stage. |
| **9. Deployment** | Build, inspect, and deliver the usable dashboard or smaller visual result with its supporting analysis and opening/refresh instructions. | Accessible artifact and reproducible analytical handoff. | Artifact renders, displayed values reconcile, useful interactions work, and the stakeholder can access it. |
| **10. Feedback** | Gather stakeholder feedback, assess usefulness, and evaluate real-world outcomes when an intervention exists; route learning into the next iteration. | Feedback record, outcome assessment, or pending evaluation plan. | Observed outcomes are distinguished from future plans; unresolved questions have clear next steps. |

**Modeling at analyst depth** includes SQL aggregations, metric decomposition, cohort/funnel analysis, statistical comparisons, scenario calculations, and appropriate forecasts or regressions. Machine learning is not required.

**Evaluation and Feedback serve different purposes**: Evaluation checks the analysis before delivery; Feedback checks stakeholder usefulness and, when applicable, real-world impact afterward. If intervention outcomes are not yet observable, label them **PENDING** and specify the baseline, target, guardrails, evaluation window, attribution method, owner, and review date. If no intervention exists, outcome evaluation is **NOT APPLICABLE**, while feedback on usefulness can still apply. Do not invent stakeholder approval or future observations.

### Visual Delivery Contract

- For substantial analyses, create a usable dashboard with relevant headline metrics, comparisons, trends or breakdowns, findings, limitations, definitions, and freshness metadata. Add filters or drill-downs where they help answer the question.
- For focused calculations or narrow questions, provide a chart, visual report, or compact result table with units, period, and brief verification. A simple table in the response is sufficient; do not build an application for a single number.
- Use accessible existing BI or project tooling; otherwise create portable HTML. Read [`dashboards-and-bi.md`](./references/dashboards-and-bi.md) when creating a dashboard and [`visualization-and-storytelling.md`](./references/visualization-and-storytelling.md) when choosing or reviewing charts.
- Deliver the actual artifact, supporting result tables, reproducible queries or scripts, and a concise explanation. Respect explicit requests for a different format or code-only work; a proposed layout alone does not satisfy a request for a working dashboard.
- If data or runtime access is unavailable, state what cannot be completed and provide a clearly labeled specification or illustrative prototype when useful. Never fabricate measurements or describe a prototype as a verified result.
- Deployment can mean a local artifact with opening instructions. Hosting and scheduled refresh require an actual request and available infrastructure; describe a static snapshot honestly.

### Stage-Gate Rule

Return to the earliest stage that can resolve a failed gate. For example, missing fields can require revisiting Data Requirements and Collection, contradictory results can require revisiting Analytic Approach or Modeling, and stakeholder questions can reveal a need to revise Business Understanding. Record unresolved failures and their effect on confidence.

---

## Tool Selection Matrix

| Environment Capability | Recommended Analytical Tooling & Practical Guidance |
|---|---|
| **SQL Data Warehouse Available** | Use relational SQL for scalable extraction, aggregation, windowing, and cohort retention. Always define output grain before querying and enforce join cardinality checks. |
| **Programmatic Environment (Python / R)** | Use tabular dataframe libraries (pandas, polars) for complex cleaning, statistical modeling, bootstrapping, time-series decomposition, and reproducible scripting. |
| **BI / Dashboarding Tool Available** | Use for visual metric monitoring, self-serve reporting, and sharing interactive dashboards with stakeholders (Tableau, Looker, Power BI, Metabase, Superset). Follow F-pattern layout hierarchy and avoid clutter. |
| **Spreadsheet Environment Available** | Use structured formulas (`XLOOKUP`, `SUMIFS`), pivot tables, and reconciliation cells for small-scale modeling, ad-hoc financial audits, and rapid prototyping. |
| **Portable HTML / No BI Tool Available** | Create a browser-viewable dashboard using verified result tables, with minimal dependencies and documented opening instructions. |
| **Conceptual / No Runtime Available** | Formulate conceptual SQL logic, design metric formulas, define validation invariants, structure hypothesis trees, and provide decision reasoning frameworks. |

---

## Final Result Verification

Stage gates validate individual steps; this final verification validates the complete analytical result before delivery. Report checks that could not be completed as limitations rather than silently treating them as passed.

### Verification Execution Protocol

Follow the evidence standard in [`analytics-lifecycle.md`](./workflows/analytics-lifecycle.md). In summary:

1. Express each material check with an expected condition or tolerance, then execute it with task-specific SQL, Python/R, spreadsheet formulas, or equivalent tooling when the environment permits.
2. Preserve the check and its observed output, and independently recompute decision-critical metrics when practical.
3. Assign each verification check **PASS**, **FAIL**, **NOT VERIFIED**, or **NOT APPLICABLE**. Never infer **PASS** from the absence of an error. **PENDING** is a separate Feedback outcome state, not a check status: for example, the evaluation-plan completeness check can pass while the future outcome remains pending.
4. Return to the earliest corrective stage after a failure. If correction is impossible within scope, disclose the failure and do not present the affected conclusion as verified.

- [ ] **Question Alignment**: The output directly answers the Business Understanding analytical question and supports the stated decision or informational purpose.
- [ ] **Grain Definition**: Explicitly defined what one row of every output dataset represents.
- [ ] **Row Count Reconciliation**: Tracked and verified `COUNT(*)` before and after every `JOIN` and filter to eliminate fanout.
- [ ] **Denominator Verification**: Every percentage, rate, or ratio has a validated base population and explicit zero-denominator behavior; use `NULLIF` in SQL or the equivalent safe handling in the active tool.
- [ ] **Ratio Calculation Alignment**: Verified whether the intended estimand requires a ratio of sums ($\frac{\sum \text{num}}{\sum \text{den}}$, population-weighted) or an average of unit-level ratios ($\text{AVG}(\text{rate})$, entity-weighted), aligned with the defined unit of analysis.
- [ ] **Rate Shift Distinction**: Explicitly distinguished percentage point shifts ($+2\text{ pp}$) from relative percentage changes ($+20\%$).
- [ ] **Null Safety**: Mandatory ID fields and grouping dimensions contain zero unexpected nulls.
- [ ] **Domain Plausibility**: Each metric satisfies its own domain invariants. Proportions such as conversion usually lie in $[0, 100\%]$; growth rates may be negative or exceed $100\%$; metrics such as NRR may legitimately exceed $100\%$.
- [ ] **Outlier Protocol**: Candidate unusual observations were investigated; zero data was silently deleted.
- [ ] **Comparable Time Windows**: No partial ongoing time periods compared directly against full completed historical baselines without daily normalization.
- [ ] **Causal Discipline**: No causal assertions made from observational data without randomized experimental design or validated quasi-experimental identification.
- [ ] **Reproducibility**: Extraction queries, table names, filter timestamps, and random seeds documented.
- [ ] **Method Fit**: The chosen analytical technique matches the question, data, assumptions, and decision stakes.
- [ ] **Evidence Traceability**: Every material conclusion and recommendation can be traced to a verified result.
- [ ] **Cognitive Separation**: Facts, observations, insights, hypotheses, conclusions, recommendations, and limitations are not conflated.
- [ ] **Uncertainty and Limitations**: Material uncertainty, data-quality constraints, assumptions, and unresolved risks are disclosed.
- [ ] **Visual Delivery**: The agreed artifact exists, opens and renders correctly, shows verified values and visible limitations, and has working interactions where applicable. Disclose any unperformed render or interaction checks.
- [ ] **Outcome Evaluation Status**: When applicable, the result distinguishes a completed outcome assessment from a **PENDING** evaluation plan; otherwise it records **NOT APPLICABLE**.

### Verification Evidence in the Deliverable

Include a **Verification** section in every non-trivial analytical deliverable. Use a compact equivalent for simple requests.

| Check | Expected Condition / Tolerance | Method | Evidence | Status | Effect on Confidence |
|---|---|---|---|---|---|
| Decision-critical invariant or claim | Explicit condition that constitutes success | Executed query, calculation, formula, or review method | Observed result with enough detail to reproduce or locate it | PASS, FAIL, NOT VERIFIED, or NOT APPLICABLE | None, bounded caveat, or conclusion blocked |

The ledger must cover the checks that materially support the result, not every exploratory command. Link or point to saved verification code and detailed outputs when the deliverable format permits it.

---

## Critical Anti-Patterns to Avoid
- **Immediate Coding Trap**: Diving into SQL queries or Python scripts before agreeing on the business decision or informational purpose, analytical question, and metric definitions.
- **The Raw Data Fallacy**: Assuming raw extracted data is indisputable truth without validating pipeline freshness, tracking schemas, or null rates.
- **Silent Data Tampering**: Imputing missing values or dropping extreme points without documenting methodology and row volume affected.
- **The Naked Average**: Using a mean as a typical value for a skewed distribution without checking whether robust summaries or distribution context are needed. A defined aggregate KPI, such as average order value, does not automatically require reporting the median or IQR when that context is not relevant to the question.
- **Denominator Blindness**: Celebrating a rising conversion rate caused by collapsing top-of-funnel traffic rather than increased conversions.
- **The Universal N < 30 Myth**: Assuming any cohort with $N < 30$ is automatically invalid or that $N \ge 30$ guarantees representativeness. Sample size affects precision; representativeness depends on sampling design.
- **p-Value Myopia**: Treating $p < 0.05$ as an automatic green light while ignoring effect size, uncertainty intervals, and practical commercial significance.
- **Correlation as Causation**: Claiming an intervention caused a metric shift based purely on concurrent timing or observational regression.
- **Lookahead Leakage**: Using future information to predict past outcomes or standardizing time-series datasets using global rather than rolling historical statistics.
- **The Kitchen Sink Dashboard**: Cramming 25 disconnected charts onto a single dashboard page without visual hierarchy or decision focus.
