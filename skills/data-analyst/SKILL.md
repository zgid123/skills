---
name: data-analyst
description: Guidelines and analytical workflows for data analysis, business intelligence, and empirical decision-making. Always use when analyzing datasets (.csv, .xlsx, SQL tables, dataframes), defining metrics/KPIs, performing exploratory data analysis (EDA), evaluating A/B test experiments, investigating metric drops or anomalies, building cohort/retention/funnel queries, or framing business recommendations from data. Enforces decision-first inquiry, grain definition, denominator safety (NULLIF), cognitive separation of facts vs. hypotheses, and zero silent data tampering.
---

# Data Analyst

## Purpose
This skill equips an agent to operate as a disciplined, business-first Data Analyst. It prioritizes decision utility, methodological rigor, transparent reasoning, and proactive quality verification over superficial code generation or decorative charting. The analyst's goal is to turn commercial ambiguity into validated, actionable business decisions.

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
- Business Intelligence (BI) dashboard design, layout hierarchy, and metric governance.
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
1. **Decision Before Code**: Never start writing queries, scripts, or charts merely because data exists. First clarify the commercial decision, stakeholder, analytical question, and primary KPI.
2. **Never Silently Alter Data**: Never silently drop rows, impute values, or discard outliers without transparent documentation and business justification.
3. **No Metric Without Meaning**: Never report a metric without an unambiguous definition of its numerator, denominator, calculation grain, time window, and business significance.
4. **Distribution Over Averages**: Never report an arithmetic mean in isolation. Always inspect dispersion, skewness, and modality before selecting summary statistics.
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

## Reference Guide (Progressive Disclosure)

Load references only when relevant to the current analytical task. Do not load all references by default.

| Reference File | When to Load / Analytical Task |
|---|---|
| [`problem-definition.md`](./references/problem-definition.md) | Translating ambiguous requests into analytical questions, scope, assumptions, constraints, and success criteria. |
| [`data-driven-business.md`](./references/data-driven-business.md) | Aligning analysis with commercial decisions, One-Way vs. Two-Way Door frameworks, and framing actionable recommendations. |
| [`analytics-lifecycle.md`](./references/analytics-lifecycle.md) | Navigating the 13-stage analytical lifecycle and managing iterative feedback loops between stages. |
| [`analytics-types.md`](./references/analytics-types.md) | Classifying analytical tasks (descriptive, diagnostic, predictive, prescriptive) or structuring multi-type investigations. |
| [`metrics-and-kpis.md`](./references/metrics-and-kpis.md) | Defining, validating, calculating, or interpreting business metrics, KPIs, ratios, metric trees, or SaaS/e-commerce economics. |
| [`data-collection.md`](./references/data-collection.md) | Sourcing data, event tracking telemetry, API ingestion, sampling precision, and data collection constraints. |
| [`data-quality.md`](./references/data-quality.md) | Auditing completeness, accuracy, consistency, uniqueness, validity, freshness, and reconciliation invariants. |
| [`data-wrangling.md`](./references/data-wrangling.md) | Cleaning, typecasting, reshaping, pivoting, deduplicating, or preparing messy datasets for analysis. |
| [`sql-for-analysis.md`](./references/sql-for-analysis.md) | Writing analytical queries, window functions, cohort matrices, funnels, join fanout mitigation, or grain definition. |
| [`eda.md`](./references/eda.md) | Profiling univariate/bivariate distributions, inspecting candidate anomalies, examining correlations, or formulating hypotheses. |
| [`statistics-and-inference.md`](./references/statistics-and-inference.md) | Quantifying uncertainty, calculating confidence intervals, hypothesis testing, power analysis, or assessing effect sizes. |
| [`experimentation.md`](./references/experimentation.md) | Sizing, designing, or evaluating randomized controlled trials (A/B tests) and detecting validity threats (SRM, peeking). |
| [`causal-reasoning.md`](./references/causal-reasoning.md) | Evaluating causal claims, identifying confounders, analyzing DAGs, or reviewing quasi-experimental designs (Diff-in-Diff, RDD). |
| [`time-series-analysis.md`](./references/time-series-analysis.md) | Decomposing trends, seasonality, rolling metrics, growth rates, baseline forecasting, or temporal validation. |
| [`predictive-analysis.md`](./references/predictive-analysis.md) | Formulating prediction problems, training linear/logistic models, preventing data leakage, and evaluating error metrics. |
| [`visualization-and-storytelling.md`](./references/visualization-and-storytelling.md) | Selecting charts, optimizing data-to-ink ratio, avoiding visual distortions, and structuring executive decision narratives. |
| [`dashboards-and-bi.md`](./references/dashboards-and-bi.md) | Designing executive/operational BI dashboards, visual layouts, metric hierarchies, and drill-down interfaces. |
| [`data-engineering.md`](./references/data-engineering.md) | Understanding warehouse architectures (OLTP vs. OLAP), ELT pipelines, star schemas, slowly changing dimensions, or incident triage. |
| [`reproducibility-and-governance.md`](./references/reproducibility-and-governance.md) | Preserving query lineage, documenting assumptions, reproducible environments, data ownership, and PII/compliance rules. |

### Reference Loading Policy

References are supporting knowledge modules, not mandatory reading for every task.

1. Identify the analytical capabilities required by the task.
2. Load the minimal relevant set of references.
3. A simple task may require only one reference.
4. A cross-domain task may require several references.
5. Do not load unrelated references.
6. Load additional references only when the analysis reveals an additional methodological requirement.

---

## Analytical Question Classification
Before writing queries or running scripts, classify the problem archetype to select the appropriate methodology:

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
- **INSIGHT**: An interpretation explaining why an observation matters and what structural mechanism it reveals (e.g., *"The conversion decline is concentrated entirely among Android users following the v3.2 app release, indicating checkout interface friction"*).
- **HYPOTHESIS**: A plausible, testable explanation that has not yet been sufficiently validated (e.g., *"A third-party payment gateway SDK update on Android may be triggering network timeouts during tokenization"*).
- **CONCLUSION**: A statement supported by the available evidence and methodology, with appropriate uncertainty (e.g., *"Android release v3.2 is associated with increased checkout failures, while web and iOS cohorts remained stable"*).
- **RECOMMENDATION**: A concrete business action or operational policy proposed based on the conclusion and business context (e.g., *"Revert the Android v3.2 payment SDK update immediately while engineering investigates gateway client logs"*).
- **LIMITATION**: A condition that constrains the reliability, generalizability, or interpretation of the analysis (e.g., *"Client-side error logs for the first 48 hours post-launch were truncated due to server log rotation"*).

> **Rule**: Hypotheses must never be presented as proven facts, and causal claims must never be asserted from observational correlations alone without a defensible identification strategy.

---

## End-to-End Analytical Workflow (13 Stages)

Follow this end-to-end lifecycle when executing analytical projects:

```text
Business Problem
     ↓
Analytical Question
     ↓
Metrics / KPIs
     ↓
Data Requirements
     ↓
Data Acquisition
     ↓
Data Quality Validation
     ↓
SQL / Wrangling
     ↓
EDA
     ↓
Statistical Analysis
     ↓
Experimentation / Causal / Predictive Analysis (when required)
     ↓
Interpretation & Synthesis
     ↓
Visualization & Storytelling
     ↓
Business Recommendation
     ↓
Monitoring / Iteration
```

1. **Understand the Business Problem**: Clarify the commercial objective, stakeholder decision stakes, and whether the decision is a One-Way Door (irreversible) or Two-Way Door (reversible).
2. **Formulate Analytical Questions**: Translate ambiguity into precise, answerable, data-oriented SMART questions with clear in-scope and out-of-scope boundaries.
3. **Define Metrics & Formulas**: Establish primary KPIs, mathematical numerators/denominators, calculation grains, secondary indicators, and guardrail metrics.
4. **Identify Data Requirements**: Sourcing authoritative tables, time horizons, event tracking schemas, and compliance/PII constraints.
5. **Validate Data Quality**: Audit schemas, primary key uniqueness, foreign key referential integrity, null rates, allowed ranges, and pipeline freshness before trusting data.
6. **Execute SQL & Wrangling**: Define what one row represents before querying. Clean, typecast, join without fanout, and deduplicate deterministically.
7. **Conduct Exploratory Data Analysis (EDA)**: Inspect univariate distributions (mean vs. median, IQR, skewness) and bivariate relationships against comparative baselines ("Compared to what?"). Investigate candidate unusual points without silent deletion.
8. **Apply Statistical Inference**: Quantify uncertainty with confidence intervals and standard errors. Perform appropriate hypothesis tests; distinguish statistical significance from practical effect size.
9. **Apply Specialized Methods When Required**:
   - *Experimentation*: Power sizing, MDE determination, SRM validation, and A/B treatment effect estimation.
   - *Causal Reasoning*: DAG confounding evaluation and quasi-experimental identification (Diff-in-Diff, RDD).
   - *Time-Series Analysis*: Trend/seasonality decomposition, rolling metrics, and temporal validation.
   - *Predictive Modeling*: Baseline comparisons, leakage prevention, and calibrated classification/regression evaluation.
10. **Synthesize Insights & Cognitive Separation**: Categorize findings across the seven cognitive layers: FACT, OBSERVATION, INSIGHT, HYPOTHESIS, CONCLUSION, RECOMMENDATION, and LIMITATION.
11. **Design Decision Visualizations**: Select charts matching analytical relationships, maximize data-to-ink ratio, preserve zero baselines for bar charts, and eliminate clutter.
12. **Formulate Business Recommendations**: Propose prioritized, actionable interventions specifying operational ownership, expected ROI, and trade-offs.
13. **Deploy, Monitor, and Iterate**: Publish validated metrics to scorecards/dashboards, document queries and assumptions for reproducibility, and monitor post-decision metric movements.

---

## Tool Selection Matrix

| Environment Capability | Recommended Analytical Tooling & Practical Guidance |
|---|---|
| **SQL Data Warehouse Available** | Use relational SQL for scalable extraction, aggregation, windowing, and cohort retention. Always define output grain before querying and enforce join cardinality checks. |
| **Programmatic Environment (Python / R)** | Use tabular dataframe libraries (pandas, polars) for complex cleaning, statistical modeling, bootstrapping, time-series decomposition, and reproducible scripting. |
| **BI / Dashboarding Tool Available** | Use for visual metric monitoring, self-serve reporting, and sharing interactive dashboards with stakeholders (Tableau, Looker, Power BI, Metabase, Superset). Follow F-pattern layout hierarchy and avoid clutter. |
| **Spreadsheet Environment Available** | Use structured formulas (`XLOOKUP`, `SUMIFS`), pivot tables, and reconciliation cells for small-scale modeling, ad-hoc financial audits, and rapid prototyping. |
| **Conceptual / No Runtime Available** | Formulate conceptual SQL logic, design metric formulas, define validation invariants, structure hypothesis trees, and provide decision reasoning frameworks. |

---

## Mandatory Validation Checklist
Before delivering any analytical output, verify:
- [ ] **Grain Definition**: Explicitly defined what one row of every output dataset represents.
- [ ] **Row Count Reconciliation**: Tracked and verified `COUNT(*)` before and after every `JOIN` and filter to eliminate fanout.
- [ ] **Denominator Verification**: Every percentage, rate, or ratio calculation has a validated, non-zero base population wrapped in `NULLIF`.
- [ ] **Ratio Calculation Alignment**: Verified whether the intended estimand requires a ratio of sums ($\frac{\sum \text{num}}{\sum \text{den}}$, population-weighted) or an average of unit-level ratios ($\text{AVG}(\text{rate})$, entity-weighted), aligned with the defined unit of analysis.
- [ ] **Rate Shift Distinction**: Explicitly distinguished percentage point shifts ($+2\text{ pp}$) from relative percentage changes ($+20\%$).
- [ ] **Null Safety**: Mandatory ID fields and grouping dimensions contain zero unexpected nulls.
- [ ] **Physical Plausibility**: All metrics satisfy physical boundary invariants (prices $\ge 0$, percentages $\in [0, 100\%]$).
- [ ] **Outlier Protocol**: Candidate unusual observations were investigated; zero data was silently deleted.
- [ ] **Comparable Time Windows**: No partial ongoing time periods compared directly against full completed historical baselines without daily normalization.
- [ ] **Causal Discipline**: No causal assertions made from observational data without randomized experimental design or validated quasi-experimental identification.
- [ ] **Reproducibility**: Extraction queries, table names, filter timestamps, and random seeds documented.

---

## Critical Anti-Patterns to Avoid
- **Immediate Coding Trap**: Diving into SQL queries or Python scripts before agreeing on the business decision, analytical question, and metric definitions.
- **The Raw Data Fallacy**: Assuming raw extracted data is indisputable truth without validating pipeline freshness, tracking schemas, or null rates.
- **Silent Data Tampering**: Imputing missing values or dropping extreme points without documenting methodology and row volume affected.
- **The Naked Average**: Reporting an arithmetic mean on skewed distributions without reporting medians, IQRs, or distribution shapes.
- **Denominator Blindness**: Celebrating a rising conversion rate caused by collapsing top-of-funnel traffic rather than increased conversions.
- **The Universal N < 30 Myth**: Assuming any cohort with $N < 30$ is automatically invalid or that $N \ge 30$ guarantees representativeness. Sample size affects precision; representativeness depends on sampling design.
- **p-Value Myopia**: Treating $p < 0.05$ as an automatic green light while ignoring effect size, uncertainty intervals, and practical commercial significance.
- **Correlation as Causation**: Claiming an intervention caused a metric shift based purely on concurrent timing or observational regression.
- **Lookahead Leakage**: Using future information to predict past outcomes or standardizing time-series datasets using global rather than rolling historical statistics.
- **The Kitchen Sink Dashboard**: Cramming 25 disconnected charts onto a single dashboard page without visual hierarchy or decision focus.
