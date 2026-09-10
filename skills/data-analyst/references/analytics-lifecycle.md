# The Analytics Lifecycle

## Operational Overview
The analytics lifecycle is an iterative, non-linear progression from an ambiguous business concern to a validated, communicated decision and ongoing monitoring. While formal methodologies depict a sequential pipeline, real-world data analysis requires continuous feedback loops between stages as data quality realities and unexpected empirical patterns emerge.

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

## The Complete Analytical Lifecycle Stages

### 1. Business Problem & Decision Stakes
- Identify the primary business stakeholder, operational symptom, and commercial decision to be supported.
- *Reference*: [Problem Definition and Framing](./problem-definition.md), [Data-Driven Business](./data-driven-business.md).

### 2. Analytical Question Formulation
- Translate commercial ambiguity into precise, answerable, data-oriented inquiries satisfying SMART criteria.
- Establish in-scope boundaries, out-of-scope constraints, and pre-agreed success criteria.

### 3. Metric and KPI Definition
- Define the primary metric, mathematical formulas, numerators, denominators, and eligible population grain.
- Identify secondary diagnostic metrics and operational guardrail metrics.
- *Reference*: [Metrics and KPIs](./metrics-and-kpis.md).

### 4. Data Requirements & Sourcing
- Identify authoritative source tables, historical time windows, and required dimensional attributes.
- Evaluate first-party vs. third-party data, storage grain, and compliance/PII constraints.
- *Reference*: [Data Sourcing and Collection](./data-collection.md).

### 5. Data Quality Validation
- Verify primary key uniqueness, foreign key referential integrity, null rates, allowed value ranges, and freshness.
- Rule out pipeline stalls, tracking drops, and schema drift before assuming real-world behavioral changes.
- *Reference*: [Data Quality](./data-quality.md), [Data Engineering for Analysts](./data-engineering.md).

### 6. SQL Extraction and Wrangling
- Define output grain (what one row represents) before writing queries.
- Clean, typecast, deduplicate, filter, and join tables while avoiding fanout and duplicate amplification.
- *Reference*: [SQL for Analysis](./sql-for-analysis.md), [Data Wrangling and Transformation](./data-wrangling.md).

### 7. Exploratory Data Analysis (EDA)
- Inspect univariate distributions (mean vs. median, skewness, dispersion) and bivariate relationships.
- Investigate candidate unusual observations without deleting data silently; formulate testable hypotheses.
- *Reference*: [Exploratory Data Analysis (EDA)](./eda.md).

### 8. Statistical and Inferential Analysis
- Quantify estimation uncertainty using standard errors and confidence intervals.
- Conduct appropriate hypothesis tests; distinguish statistical significance from practical effect size.
- *Reference*: [Statistics and Statistical Inference](./statistics-and-inference.md).

### 9. Specialized Analytical Methods (When Required)
- **A/B Testing**: Evaluate randomized experiments, verify Sample Ratio Mismatch (SRM), and estimate treatment effects. *Reference*: [Experimentation and A/B Testing](./experimentation.md).
- **Causal Reasoning**: Evaluate counterfactual assumptions and quasi-experiments (Diff-in-Diff, RDD). *Reference*: [Causal Reasoning](./causal-reasoning.md).
- **Time-Series Analysis**: Decompose trends, seasonality, and rolling metrics. *Reference*: [Time-Series Analysis](./time-series-analysis.md).
- **Predictive Modeling**: Formulate prediction targets, prevent leakage, evaluate classification/regression baselines. *Reference*: [Predictive Analysis](./predictive-analysis.md).

### 10. Interpretation and Cognitive Separation
- Categorize findings strictly across the seven cognitive layers: FACT, OBSERVATION, INSIGHT, HYPOTHESIS, CONCLUSION, RECOMMENDATION, and LIMITATION.
- Synthesize root drivers and isolate core mechanisms.

### 11. Visualization and Storytelling
- Select charts strictly aligned with analytical objectives (comparisons, trends, distributions, relationships).
- Strip chartjunk, preserve zero baselines for bar charts, and frame narratives around business decisions.
- *Reference*: [Visualization and Storytelling](./visualization-and-storytelling.md).

### 12. Business Recommendations
- Propose concrete, prioritized operational actions specifying assigned owners and expected commercial ROI.
- Acknowledge trade-offs, decision reversibility (One-Way vs. Two-Way Doors), and residual risks.

### 13. Deployment, Monitoring, and Iteration
- Publish validated metrics to operational scorecards and dashboards.
- Monitor tracking health, track post-intervention outcomes against forecasts, and iterate when feedback arrives.
- *Reference*: [Dashboards and BI](./dashboards-and-bi.md), [Reproducibility and Governance](./reproducibility-and-governance.md).

## Non-Linear Feedback Loops
- **Data Quality Loop**: Data validation (Step 5) frequently exposes missing tracking or corrupted fields, forcing revisions to data sourcing or analytical questions.
- **EDA Hypothesis Loop**: Discoveries during EDA (Step 7) often contradict initial business assumptions, requiring new metric definitions or deeper segmentation.
- **Verification Loop**: Discrepancies during final synthesis require tracing back to SQL extraction to audit join cardinality.

## Cross-References
- For translating commercial ambiguity into analytical questions: [Problem Definition and Framing](./problem-definition.md)
- For choosing analytical types and methodologies: [Analytics Types and Selection](./analytics-types.md)
- For data quality profiling and validation: [Data Quality](./data-quality.md)
- For reproducible documentation standards: [Reproducibility and Governance](./reproducibility-and-governance.md)
