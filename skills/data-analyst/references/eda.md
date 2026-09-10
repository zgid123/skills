# Exploratory Data Analysis (EDA)

## Purpose and Mindset
Exploratory Data Analysis (EDA) is an iterative, structured investigation of data to discover underlying patterns, inspect distributions, verify assumptions, detect candidate anomalies, and formulate testable hypotheses before committing to formal statistical testing, predictive modeling, or business recommendations. EDA should generate hypotheses, not automatically prove them.

### Crucial Distinction: Exploratory Analysis vs. Diagnostic Analysis
- **Exploratory Analysis (EDA)** asks: *"What patterns, distributions, correlations, and anomalies exist in this dataset?"* It maps the analytical landscape and generates candidate hypotheses without presuming a specific failure mode.
- **Diagnostic Analysis** asks: *"Why did a specific business metric movement, anomaly, or failure occur?"* It is focused, hypothesis-driven, and designed to isolate root causes through metric decomposition.
- *Guidance*: Use EDA to profile distributions, uncover data quality issues, and map segment patterns. When diagnosing why a metric moved, transition to focused diagnostic root-cause analysis.

## The Comparative Mindset: "Compared to What?"
An isolated number or trend has no analytical meaning without a comparative baseline. Always evaluate observations against:
- **Previous Period**: Prior day, week, month, or year (MoM, YoY).
- **Target / Plan**: Budgeted goals or forecasted milestones.
- **Benchmark**: Industry standard, category average, or platform norm.
- **Control Cohort**: An unexposed or untreated group.
- **Peer Segment**: Other product tiers, geographies, or operating categories.
- **Historical Baseline**: Pre-intervention run rate.

## Cognitive Layers of Analytical Output
To maintain analytical integrity and prevent premature conclusions, categorize analytical statements into seven distinct cognitive layers:

| Layer | Definition | Example |
|---|---|---|
| **FACT** | A validated directly measured or derived value whose source, definition, transformation, and data quality are sufficiently known. | "Validated `orders` table contains 14,200 records with 0 unhandled nulls in primary key `order_id`." |
| **OBSERVATION** | A pattern or property observed in the analyzed data. | "Mobile checkout conversion declined from 4.8% to 3.2% between Q1 and Q2." |
| **INSIGHT** | An interpretation explaining why an observation matters in context. | "The conversion decline is concentrated entirely among Android users following the v3.2 release, indicating checkout interface friction." |
| **HYPOTHESIS** | A testable explanation that has not yet been sufficiently validated. | "Network timeouts during third-party payment gateway handoffs on Android v3.2 may be causing drop-offs." |
| **CONCLUSION** | A statement supported by the available evidence and methodology, with appropriate uncertainty. | "Android app release v3.2 is associated with increased checkout failures, while web and iOS cohorts remained stable." |
| **RECOMMENDATION** | An action proposed based on the evidence, conclusion, business context, constraints, and trade-offs. | "Revert Android app release v3.2 immediately while investigating payment gateway client logs." |
| **LIMITATION** | A condition that restricts the reliability, interpretation, generalizability, or causal meaning of the analysis. | "Payment gateway error logs for the initial 48 hours were truncated due to server log rotation." |

> **Cardinal Rules**: (1) Never present a hypothesis as a proven conclusion. (2) Never assert a causal claim from observational data alone without a defensible identification strategy. (3) Distinguish validated facts from raw uninspected data.

## Systematic Step-by-Step EDA Workflow

### Step 1: Shape and Structural Inspection
- Inspect dataset dimensions (row count, column count).
- Verify data types of each column (numeric, categorical, datetime, boolean).
- Assess primary key uniqueness and overall record completeness.

### Step 2: Missingness and Cardinality Profiling
- Compute fill rates and null counts per column.
- Check cardinality (count of unique values) for categorical dimensions.
- Identify single-value (zero-variance) columns that provide zero analytical signal.

### Step 3: Univariate Analysis (Numerical Variables)
- Compute 5-number summary (Min, $Q_1$, Median, $Q_3$, Max) alongside Mean and Standard Deviation.
- Check distribution shape: symmetrical, right-skewed, left-skewed, bimodal, or uniform.
- Compare Mean vs. Median: if Mean $\gg$ Median, substantial positive skew is present; use median for typical values.
- Visualize distributions using histograms with appropriate bin widths and box plots.
- Detect candidate unusual observations using the IQR rule ($1.5 \times \text{IQR}$) or Z-scores ($|z| > 3$). Treat them as signals requiring investigation, not automatic deletion.

### Step 4: Univariate Analysis (Categorical Variables)
- Generate frequency tables and percentage shares of total for each category.
- Plot sorted bar charts with a zero baseline.
- Identify high-cardinality columns, rare tail categories, or unstandardized casing.

### Step 5: Bivariate Analysis (Relationships and Interactions)
- **Numerical vs. Numerical**:
  - Generate scatter plots to inspect linearity, curvature, heteroscedasticity, and clustering.
  - Calculate correlation coefficients (Pearson for linear, Spearman for monotonic rank relationships). Note that correlation does not imply causation.
- **Categorical vs. Numerical**:
  - Compare metric distributions across categories using grouped box plots, violin plots, or faceted histograms.
  - Evaluate within-group variance vs. between-group variance.
- **Categorical vs. Categorical**:
  - Construct contingency tables (cross-tabulations) with row and column percentage distributions.
  - Plot stacked or grouped bar charts.

### Step 6: Temporal Patterns and Time Slicing
- Plot primary metrics over time using continuous line charts.
- Inspect for:
  - **Trends**: Long-term directional movement.
  - **Seasonality**: Repeating cyclical patterns (day-of-week, hour-of-day, annual holidays).
  - **Structural Breaks**: Sudden level shifts or trend changes coinciding with product releases, pricing changes, or macro events.

### Step 7: Confounding and Simpson's Paradox Checks
- Check whether aggregate trends reverse or disappear when partitioned by major subgroups (Simpson's Paradox).
- Identify confounding variables that correlate simultaneously with both predictor and outcome.

### Step 8: Synthesis and Hypothesis Formulation
- Summarize confirmed empirical facts and observations.
- Document unexpected anomalies, data quality gaps, and unmeasured variables.
- Formulate explicit, testable hypotheses to guide subsequent diagnostic analysis, inferential testing, or experimental design.

## Cross-References
- For data quality profiling, sanity checks, and validation rules: [Data Quality](./data-quality.md)
- For data cleaning, missing value handling, and reshaping: [Data Wrangling and Transformation](./data-wrangling.md)
- For SQL aggregation, window functions, and deduplication: [SQL for Analysis](./sql-for-analysis.md)
- For quantifying uncertainty, hypothesis testing, and confidence intervals: [Statistics and Statistical Inference](./statistics-and-inference.md)
- For chart selection, formatting, and storytelling principles: [Visualization and Storytelling](./visualization-and-storytelling.md)
