# Data Sourcing and Collection

## Primary vs. Secondary Data
- **Primary Data**: Data collected directly by the organization for the specific analytical problem at hand (e.g., custom user surveys, user interviews, bespoke in-app A/B test telemetry, dedicated sensor measurements).
  - *Advantages*: Tailored precisely to the research question, high control over definitions and collection methodology.
  - *Disadvantages*: Expensive, time-consuming to gather, potentially small sample size.
- **Secondary Data**: Pre-existing data collected for operational or alternate purposes, reused for analysis (e.g., production transaction logs, ERP records, third-party industry benchmarks, government census tables).
  - *Advantages*: Immediately available, large historical volume, cost-effective.
  - *Disadvantages*: May lack ideal fields, definitions may not match analytical needs, subject to unknown historical pipeline changes.

## Data Structures and Formats
- **Structured Data**: Rigid schema organized into formal rows and columns (e.g., PostgreSQL tables, CSV/Parquet files, dimensional data warehouse marts).
- **Semi-Structured Data**: Lacks a strict relational schema but contains tags, markers, or hierarchical keys (e.g., JSON event payloads, XML feeds, MongoDB documents).
- **Unstructured Data**: Freeform information lacking predefined structural models (e.g., customer support call transcripts, survey free-text feedback, emails, PDF reports).

## Common Data Collection Channels
- **Relational & Analytical Databases**: Direct SQL querying of production replicas, analytical warehouses (Snowflake, BigQuery, Redshift), or internal datamarts.
- **APIs and Webhooks**: Programmatic HTTP requests (REST, GraphQL) extracting data from third-party platforms (Stripe, Salesforce, Google Analytics).
- **Event Tracking & Clickstreams**: Client-side and server-side event tracking capturing user actions with contextual metadata (timestamp, user_id, event_name, properties).
- **Application & Server Logs**: Unstructured or semi-structured log streams (Logstash, CloudWatch, Datadog) capturing system performance, errors, and access events.
- **Surveys and Questionnaires**: Structured forms collecting qualitative sentiment, CSAT, or NPS responses directly from target users.
- **Controlled Experiments**: Data generated through randomized A/B or multivariate testing pipelines.
- **Third-Party & Public Datasets**: Syndicated market research, open government portals, econometric benchmarks, or industry databases.

## Granularity and Time Horizon
- **Data Granularity**: The level of detail represented by an individual record in a dataset.
  - *High Granularity (Atomic)*: Individual button clicks, itemized invoice line items, millisecond sensor readings.
  - *Low Granularity (Aggregated)*: Monthly sales per store, daily active users per country.
  - *Collection Standard*: Preserve the finest granularity justified by analytical requirements while considering privacy, governance, storage, performance, and data-minimization requirements. You can always aggregate detailed data for high-level metrics, but you cannot disaggregate pre-aggregated data.
- **Time Range Considerations**:
  - Ensure the selected window captures full business cycles (e.g., day-of-week seasonality, month-end spikes, quarterly budget cycles).
  - Watch for historical structural changes (e.g., pricing model overhauls, website redesigns, tracking tag schema migrations) within the time window.

## Sampling, Bias, and Statistical Precision
- **When to Sample**: When querying or computing full-population datasets is cost-prohibitive, computationally intractable, or unnecessary for early exploratory modeling.
- **Sampling Methods**:
  - **Simple Random Sampling**: Every unit has an equal probability of selection.
  - **Stratified Sampling**: The population is divided into mutually exclusive strata (e.g., subscription tier, country), and samples are drawn from each stratum:
    - *Proportional Allocation*: Preserves the relative proportions of strata as they exist in the broader population.
    - *Disproportionate Allocation / Oversampling*: Intentionally samples a higher fraction of smaller but critical strata (e.g., enterprise accounts) to guarantee sufficient observations for subgroup estimation precision. When estimating overall population parameters from disproportionate samples, apply survey weighting ($w_i = 1 / P(\text{selection})$) to prevent systemic bias.
- **Common Sampling Biases**:
  - **Selection Bias**: The sample systematically differs from the target population due to non-random inclusion criteria.
  - **Non-Response Bias**: Individuals who choose to respond to a survey systematically differ from those who ignore it.
  - **Survivorship Bias**: Analyzing only entities that survived a selection process (e.g., surveying existing active users while ignoring churned customers).
- **Sample Size and Statistical Precision**:
  - Sample size determines statistical power and margin of error precision, but **representativeness depends primarily on sampling design and selection mechanisms**. A massive sample of millions that is systematically biased (e.g., voluntary online poll) remains unrepresentative of the broader population.
  - To achieve an intended margin of error $e$ at confidence level $z$ (e.g., $z = 1.96$ for 95%) for an estimated proportion $p$ under simple random sampling:
    $$n \approx \frac{z^2 \cdot p(1-p)}{e^2}$$
    For $p = 0.5$ (maximum variance), 95% CI, and $e = \pm 3\%$: $n \approx 1{,}068$ records.

## Data Lineage, Provenance, and Source Reliability
- **Data Lineage**: The complete recorded pathway that data travels from its original source system through pipelines, transformations, and joins to the final report or dashboard.
- **Data Provenance**: Documentation certifying origin, ownership, extraction timestamp, and transformation history.
- **Source Reliability Evaluation**:
  - Is the source an authoritative system of record (e.g., Stripe for billing, Salesforce for CRM) or an unvalidated secondary replica?
  - What is the sync cadence (streaming vs. hourly vs. daily)?
  - Are there documented service-level agreements (SLAs) regarding uptime and pipeline freshness?

## Event Tracking Schema Design
For product, system, and behavioral analytics pipelines, event telemetry is a primary data source. Because event contexts vary widely (authenticated web sessions vs. backend microservices vs. IoT pings vs. anonymous mobile sessions), schemas must distinguish structural essentials from context-specific identifiers:

### 1. Commonly Required Fields
- `event_name` / `event_type` (string): Canonical name in `object_action` format (e.g., `checkout_completed`, `order_shipped`).
- `event_timestamp` (datetime): Precise moment the event occurred. Canonical storage should use a consistent representation, commonly ISO 8601 UTC, while business/reporting queries convert to the relevant business timezone.
- `schema_version` (integer/string): Explicit schema contract version (e.g., `v1`, `v2`) to prevent silent ingestion breakage during tracking migrations.
- `entity_id`: The primary identifier for the entity undergoing the action (e.g., `order_id`, `invoice_id`, or `user_id` when present).

### 2. Context-Dependent Fields
- `user_id` / `account_id`: Stable identity for authenticated user or tenant accounts (omitted or null for pre-auth or anonymous events).
- `anonymous_id` / `device_id`: Cookie or device-level UUID used for anonymous tracking and identity stitching.
- `session_id`: Session boundary identifier (critical for web/mobile funnels, but absent in backend batch jobs or sensor telemetry).
- `request_id` / `trace_id`: Distributed tracing key for backend operations.
- `experiment_id` / `variant_id`: Active experiment assignments at the time of event generation.
- `properties` (JSON / nested map): Contextual payload attributes (e.g., `{"price": 99.00, "currency": "USD"}`).
- `platform` / `source` (enum): Environment metadata (`web`, `ios`, `android`, `backend_service`).

### 3. Schema Governance and CDPs
- **Naming Convention**: Use consistent `object_action` format (`page_viewed`, `button_clicked`, `subscription_upgraded`). Avoid vague verbs (`track`, `event_logged`).
- **Customer Data Platforms (CDPs)**: Tools like Segment, Rudderstack, or mParticle act as event routing layers: they receive events from client SDKs and fan them out to multiple destinations (data warehouse, analytics tools, marketing automation) without requiring custom integration code per destination.

## Cross-References
- For validating completeness, freshness, and accuracy of collected data: [Data Quality](./data-quality.md)
- For cleaning, transforming, and joining collected data: [Data Wrangling and Transformation](./data-wrangling.md)
- For pipeline reliability, freshness, and observability: [Data Engineering for Analysts](./data-engineering.md)
- For exploratory profiling and distribution checking on collected datasets: [Exploratory Data Analysis (EDA)](./eda.md)
- For privacy, PII minimization, and data governance: [Reproducibility and Governance](./reproducibility-and-governance.md)
