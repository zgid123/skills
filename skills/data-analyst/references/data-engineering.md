# Data Engineering for Analysts

## Purpose and Scope
Data analysts consume data pipelines, storage systems, and dimensional models built and maintained by data engineers. This reference provides the architectural awareness, storage vocabulary, and pipeline concepts necessary for analysts to collaborate effectively, understand data latency, query high-volume warehouses efficiently, and triage pipeline incidents without attempting to act as full-time data engineers.

## Division of Responsibilities: Analyst vs. Engineer

| Dimension | Data Engineer (DE) | Data Analyst (DA) |
|---|---|---|
| **Core Focus** | Pipeline reliability, data infrastructure, ingestion scalability, data modeling architecture | Business problem solving, exploratory analysis, metrics definition, visualization, storytelling |
| **Primary Artifacts** | Production ETL/ELT pipelines, warehouse schemas, orchestration DAGs, streaming infrastructure | Analytical SQL queries, exploratory notebooks, KPI dashboards, business memos, executive reports |
| **Key Metrics** | Pipeline uptime, data freshness (latency), query performance, infrastructure cost, data availability | Decision velocity, business revenue impact, metric adoption, forecasting accuracy |
| **Tooling Ecosystem** | Airflow, Kafka, Spark, dbt, Snowflake, Terraform, Python, Docker | SQL, BI platforms (Tableau, Looker, Power BI), Pandas, Spreadsheets |

## Core Data Architecture Concepts

### 1. Operational (OLTP) vs. Analytical (OLAP) Systems
- **OLTP (Online Transaction Processing)**: Row-oriented relational databases (e.g., PostgreSQL, MySQL) optimized for high-throughput, low-latency individual transactions (reads/writes of single customer records). Normalized to 3NF to avoid update anomalies. Poor performance for analytical aggregations across millions of rows.
- **OLAP (Online Analytical Processing)**: Column-oriented analytical data warehouses (e.g., Snowflake, BigQuery, Redshift, ClickHouse) designed for large-scale scans, aggregations, and analytical workloads across millions or billions of records, whereas transactional systems prioritize low-latency inserts, updates, and point lookups. Columnar storage and compression allow queries to read only the columns requested, greatly improving aggregation speed.

### 2. Modern Storage Architectures
- **Data Warehouse**: Centrally structured, column-oriented analytical database curated for fast aggregations, dimensional modeling, and BI reporting.
- **Data Lake**: Central repository storing structured, semi-structured, and unstructured raw data in low-cost object storage (e.g., Amazon S3, Google Cloud Storage) without upfront schema enforcement.
- **Data Lakehouse**: Modern hybrid architecture combining the low-cost open storage of a data lake (Parquet files, Delta Lake, Apache Iceberg) with the ACID transactions, governance, and SQL query speed of a data warehouse.
- **Data Mart**: A specialized, curated subset of a data warehouse structured for the specific reporting needs of a single business unit (e.g., Marketing Mart, Finance Mart).

### 3. Ingestion and Processing Paradigms
- **ETL (Extract, Transform, Load)**: Data is transformed on an external compute cluster prior to loading into storage. Common in legacy on-premise stacks.
- **ELT (Extract, Load, Transform)**: Modern cloud standard. Raw data is ingested directly into the analytical warehouse; transformations are executed inside the warehouse using SQL models (e.g., dbt). Raw data remains preserved for auditability.
- **Batch Processing**: Ingesting and transforming scheduled blocks of data (hourly, daily, weekly). High throughput, cost-efficient, latency-tolerant.
- **Streaming Processing**: Ingesting and transforming individual events continuously in real-time (sub-second latency) using distributed event brokers (e.g., Apache Kafka, AWS Kinesis).

### 4. Dimensional Modeling (Ralph Kimball Framework)
- **Fact Tables**: Central tables containing numerical business measurements, transaction events, and additive metrics (e.g., `fact_orders`, `fact_ad_clicks`). Typically tall (millions/billions of rows) and narrow.
- **Dimension Tables**: Contextual tables containing descriptive business attributes describing who, what, where, and when (e.g., `dim_customers`, `dim_products`, `dim_date`).
- **Star Schema**: Single central fact table joined directly to denormalized dimension tables. Highly optimized for fast analytical SQL joins and BI tools.
- **Slowly Changing Dimensions (SCD)**:
  - *Type 1*: Overwrite old attribute value with new value. Historical context is lost.
  - *Type 2*: Retain historical context by creating a new record with effective date ranges (`valid_from`, `valid_to`, `is_current`). When querying, filter on dates to match the historical state.

### 5. Orchestration, Transformation, and the Semantic Layer
- **Orchestration**: Workflow engines that schedule, execute, and monitor dependency-driven data pipelines (DAGs) with automated retries and alerting (e.g., Apache Airflow, Dagster, Prefect).
- **Transformation Frameworks (dbt - Data Build Tool)**: Enables analysts and analytics engineers to build modular, version-controlled, tested, and documented SQL transformation models directly inside the warehouse.
- **Semantic Layer**: A centralized definition layer (e.g., Cube, dbt Metrics, LookML) where metrics and business dimensions are coded once in code, ensuring identical metric calculations across all BI tools and notebooks.

## Data Observability and Incident Triage

Before interpreting an anomalous metric movement as a genuine commercial change, follow a structured investigation sequence rather than assuming either an engineering failure or a business event prematurely:

```text
Unexpected large metric change
     ↓
Validate pipeline health and instrumentation logs
     ↓
Check source data completeness and partition counts
     ↓
Check upstream schema, ETL transformation, or query definition changes
     ↓
Check known business events, marketing launches, or external outages
     ↓
Only then interpret the change and report findings
```

1. **Freshness & Latency**: Has an upstream ingestion cron job stalled or failed? Verify `MAX(event_timestamp)` or table load metadata.
2. **Volume & Ingestion Anomalies**: Investigate whether ingestion retries, expired API tokens, pipeline backpressure, or tracking drops occurred before concluding real-world behavior shifted.
3. **Schema Drift**: Unannounced column renames, type mutations, or missing payload fields break downstream transformation views silently.
4. **Distribution Shifts**: Sudden spikes in column null percentages or unexpected default enum values indicate upstream frontend or instrumentation bugs.

### The Analyst's Triage Checklist for Data Engineering
When metric anomalies appear, confirm with engineering:
- *"When was the underlying pipeline for this table last refreshed, and did it exit with SUCCESS?"*
- *"Were there any upstream orchestration failures, retries, or backpressure delays in the last 24 hours?"*
- *"Has there been any recent frontend deployment, schema migration, or tracking SDK release affecting source events?"*

## Cross-References
- For SQL query optimization, joins, and grain definitions: [SQL for Analysis](./sql-for-analysis.md)
- For data quality profiling, null checks, and freshness validation: [Data Quality](./data-quality.md)
- For data provenance, lineage, and audit trails: [Reproducibility and Governance](./reproducibility-and-governance.md)
- For cleaning and reshaping ingested data: [Data Wrangling and Transformation](./data-wrangling.md)
