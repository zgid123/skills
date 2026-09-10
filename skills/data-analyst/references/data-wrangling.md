# Data Wrangling and Transformation

## Data States: Raw vs. Clean vs. Analysis-Ready
- **Raw Data**: Data exactly as extracted from the source system. Contains structural artifacts, mixed formatting, nulls, unparsed JSON strings, and system-specific quirks. Treat raw data as read-only and immutable. Note that raw data is NOT indisputable fact; it may contain instrumentation, transmission, or logging errors.
- **Clean Data**: Data where mechanical and formatting defects are resolved: consistent schema, normalized column names, validated primitive types, deduplicated records, and parsed timestamps.
- **Analysis-Ready Data**: Data shaped, filtered, aggregated, and enriched specifically for the analytical inquiry: appropriate unit of observation (one row per entity/event), required joined dimensions, engineered business metrics, and proper encoding.

## Core Wrangling Operations

### 1. Type Conversion and Standardization
- Explicitly cast string numbers to integer/float types (`CAST(val AS NUMERIC)` or `pd.to_numeric()`).
- Parse timestamps into ISO 8601 compliant datetime objects with explicit UTC or local timezone awareness.
- Convert low-cardinality string columns to categorical or enum types to optimize memory and enforce valid sets.
- Standardize column identifiers to `snake_case` without spaces, special characters, or leading digits.

### 2. Missing Value Treatment
- **Assess Missingness Mechanism**:
  - *MCAR (Missing Completely at Random)*: Missingness is unrelated to both observed and unobserved data; listwise deletion introduces no systematic bias into estimates, though it reduces sample size and estimation precision.
  - *MAR (Missing at Random)*: Missingness is explained by observed variables; conditional modeling or subgroup-aware imputation may be viable.
  - *MNAR (Missing Not at Random)*: Missingness depends on the unobserved value itself (e.g., high-income earners refusing to disclose income); naive deletion or simple imputation creates severe structural bias.
- **Evaluation Workflow**:
  ```text
  Missing values detected
       ↓
  Why are they missing? (Data pipeline drop vs. structural business condition)
       ↓
  How much is missing and which specific variables are affected?
       ↓
  Assess missingness mechanism (MCAR / MAR / MNAR awareness)
       ↓
  What downstream analysis or model will use the variable?
       ↓
  Would deletion alter the effective population or create selection bias?
       ↓
  Would imputation distort feature variance, distributions, or correlations?
       ↓
  Could imputation introduce future leakage (e.g., in time series)?
       ↓
  Choose appropriate treatment (deletion, indicator, domain fallback, imputation)
       ↓
  Perform sensitivity checks where missingness has material decision impact
       ↓
  Document treatment, rationale, and volume affected transparently
  ```
- **Treatment Nuance & Caveats**:
  - *Listwise Deletion*: Do not apply arbitrary percentage cutoffs (e.g., "<3%"). Consider whether dropping rows alters the target population, distorts segment representation, or creates survivorship bias.
  - *Mean / Median / Mode Imputation*: Simple baseline techniques, but analysts must recognize their distortions: they artificially reduce feature variance, alter distribution shapes, attenuate correlations with other features, and underestimate downstream statistical uncertainty.
  - *Time-Series Forward vs. Backward Fill*:
    - *Forward Fill*: Appropriate only when a value is domain-verified to persist unchanged until the next event.
    - *Backward Fill*: Carries severe risk of lookahead data leakage in predictive or time-series contexts by pulling future values into historical rows.
  - *Missingness Indicator*: Adding an indicator column (`feature_is_null`) alongside imputation preserves the informative signal that data was missing.
  - *Hard Rule*: Never silently drop rows or impute missing data without documenting the volume affected, method used, and business justification.

### 3. Deduplication
- **Distinguish Duplicate Types**:
  - *Exact Duplicates*: Drop identical rows resulting from ingestion retries or repeated logging.
  - *Semantic / Key Duplicates*: Multiple records sharing the same business entity key with divergent timestamps or values.
- **Resolution Strategy**: Establish deterministic deduplication rules using window functions with deterministic tie-breakers (e.g., `ROW_NUMBER() OVER (PARTITION BY entity_id ORDER BY updated_at DESC, event_id DESC)`) to ensure repeatable results when timestamps match.

### 4. Reshaping and Tidying Data
- **Tidy Data Principles (Hadley Wickham)**:
  1. Each variable forms a column.
  2. Each observation forms a row.
  3. Each type of observational unit forms a table.
- **Pivot (Long to Wide)**: Converting row values into distinct columns (e.g., transposing quarterly revenue metrics into Q1, Q2, Q3 columns for side-by-side comparative modeling).
- **Melt / Unpivot (Wide to Long)**: Consolidating multiple metric columns into key-value pairs; essential for tidy plotting and grouped aggregations.

### 5. Joining and Blending Datasets
- **Join Cardinality Discipline**:
  - Understand relationship cardinality before joining: 1-to-1, 1-to-many, many-to-many.
  - Always verify row count before and after joins to detect unintended Cartesian products (many-to-many fanout).
  - Use `LEFT JOIN` when preserving all primary cohort observations; use `INNER JOIN` only when non-matching rows are intentionally excluded.

### 6. Aggregation and Feature Derivation
- Group atomic records to the required analytical grain (e.g., daily transactions aggregated to monthly customer summaries).
- Create derived features reflecting business logic:
  - Ratios: Click-Through Rate ($Clicks / Impressions$).
  - Elapsed Durations: Days between account creation and first purchase.
  - Cohort Buckets: Tenure in months, spending tiers.

### 7. Normalization and Feature Scaling
- **Min-Max Scaling**: Rescales values to $[0, 1]$; useful when features must share identical bounded ranges:
  $$x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$$
- **Z-Score Standardization**: Centers feature at mean 0 and standard deviation 1:
  $$z = \frac{x - \mu}{\sigma}$$
- **When Scaling Is and Is Not Required**:
  - *Ordinary Least Squares (OLS) Linear Regression*: Does NOT inherently require standardized features for mathematical estimation or fit; unstandardized coefficients directly reflect the original physical units.
  - *When Scaling Is Critical*: Distance-based methods (k-NN, k-Means, SVM), regularized regression (Ridge, Lasso), gradient-descent optimization, and when directly comparing relative coefficient magnitudes across variables with disparate scales.
  - *Tree-Based Algorithms*: Decision trees, random forests, and gradient boosting are scale-invariant and do not benefit from feature scaling.

### 8. Categorical Transformation
- **Ordinal Encoding**: Convert ranked categories to ordered integers ($1, 2, 3, \dots$) when natural hierarchy exists.
- **One-Hot Encoding**: Create binary dummy columns for nominal categories. Drop one dummy category ($k-1$ columns) in unregularized linear models to prevent perfect multicollinearity (the Dummy Variable Trap).

### 9. Dates, Times, and Timezones
- Convert raw date strings to native datetime objects early in the pipeline.
- Normalize all transactional timestamps to a common timezone (UTC) before comparing or joining across global servers.
- Extract analytical temporal components: `day_of_week`, `hour_of_day`, `is_weekend`, `fiscal_quarter`.

### 10. Outlier and Anomaly Investigation
- Candidate unusual observations flagged by statistical thresholds (such as $|z| > 3$ or $1.5 \times \text{IQR}$) are NOT automatically invalid errors.
- Investigate whether an unusual point is a logging/instrumentation defect, a valid high-value business event (e.g., enterprise deal), a distinct subpopulation, or a fraud signal.
- Never delete unusual points silently; choose appropriate treatments (capping, winsorization, segmentation, robust modeling) and document the rationale.

## Validation After Transformation
Never assume a transformation succeeded as intended. Execute post-transformation validation:
1. Compare input row counts vs. output row counts.
2. Confirm no unexpected `NULL` values were introduced by failed joins or failed type parsing.
3. Validate that derived ratios lie within theoretically permissible bounds (e.g., percentages between 0% and 100%).
4. Verify sum reconciliations: the sum of an aggregated metric across groups must match the total sum of the unaggregated source table.

## Cross-References
- For data quality profiling, integrity checks, and validation rules: [Data Quality](./data-quality.md)
- For SQL aggregation, window functions, and deduplication: [SQL for Analysis](./sql-for-analysis.md)
- For distribution checks, outlier profiling, and correlation analysis: [Exploratory Data Analysis (EDA)](./eda.md)
- For predictive model feature preparation and leakage prevention: [Predictive Analysis](./predictive-analysis.md)
