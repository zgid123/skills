# Data Quality

## Overview
Data quality is the measure of data fitness for operational, decision-making, and analytical purposes. Raw data cannot be treated as indisputable truth; instrumentation failures, network drops, schema migrations, and ETL bugs frequently introduce corruptions. A data fact is only established after source, definition, transformation, and data quality have been validated.

## The Six Core Dimensions of Data Quality

| Dimension | Definition | Practical Test | Example Failure |
|---|---|---|---|
| **Accuracy** | Data represents the real-world entity or event correctly without distortion. | Cross-source reconciliation against trusted physical receipts or financial ledgers. | Billing table records $150 transaction when Stripe charged $15. |
| **Completeness** | Expected data is present without unintended missing records or null fields. | Null count/rate on mandatory fields; missing temporal partitions. | 25% of checkout events have null `payment_method`. |
| **Consistency** | Data values do not conflict across different tables, systems, or time periods. | Cross-table referential integrity and dimensional parity checks. | User status is `active` in CRM but `cancelled` in subscription warehouse mart. |
| **Validity** | Data conforms to domain syntax, formatting rules, allowed ranges, and schemas. | Regex format validation, enum set checks, schema contract verification. | `user_age` is recorded as -5 or 999; email is "john.doe". |
| **Uniqueness** | Records representing an entity or event appear exactly once without duplicate rows. | Primary key uniqueness tests (`COUNT(*) = COUNT(DISTINCT id)`). | Webhook retry inserts duplicate `order_id` records. |
| **Freshness / Timeliness** | Data reflects the latest operational state within acceptable latency SLAs. | `MAX(event_timestamp)` inspection vs. current system clock. | Daily dashboard shows data from 3 days ago due to stalled pipeline. |

## Practical Validation Checks and Invariants

### 1. Structural and Primary Key Invariants
- **Primary Key Integrity**: Every analytical entity table must have a verified unique primary key.
  ```sql
  SELECT primary_key_col, COUNT(*) AS cnt
  FROM table_name
  GROUP BY primary_key_col
  HAVING COUNT(*) > 1;
  ```
- **Foreign Key Referential Integrity**: Child entity foreign keys must resolve to valid parent table entries.
  ```sql
  SELECT COUNT(*) AS orphaned_orders
  FROM orders o
  LEFT JOIN customers c ON o.customer_id = c.customer_id
  WHERE c.customer_id IS NULL;
  ```

### 2. Nullity and Completeness Profiling
- Measure missingness proportions per column.
- Distinguish between expected structural nulls (e.g., `cancellation_reason` for active users) and anomalous nulls (e.g., `user_id` missing from an authentication log).
- Flag columns with fill rates dropping below baseline thresholds.

### 3. Range, Boundary, and Category Checks
- **Numerical Ranges**: Verify that values satisfy physical constraints ($price \ge 0$, $0 \le percentage \le 100$, $duration \ge 0$).
- **Allowed Categories**: Verify that categorical values belong to the approved domain enum list (e.g., `order_status` in `('pending', 'paid', 'shipped', 'cancelled', 'refunded')`).
- **Temporal Boundaries**: Verify that event timestamps are within physically valid intervals ($created\_at \le updated\_at$, $event\_time \le current\_timestamp$).

### 4. Reconciliation and Aggregation Sanity Checks
- **Source-to-Target Reconciliation**: Sum of line items must equal order totals; sum of daily revenue across marts must match the core financial ledger.
  ```sql
  -- Total line items vs order header
  SELECT o.order_id, o.total_amount, SUM(li.item_amount) AS calculated_amount
  FROM orders o
  JOIN order_line_items li ON o.order_id = li.order_id
  GROUP BY o.order_id, o.total_amount
  HAVING ABS(o.total_amount - SUM(li.item_amount)) > 0.01;
  ```
- **Row Count Multiplier Audit**: Track `COUNT(*)` immediately before and after joins to detect Cartesian products or fanout.

### 5. Distribution Shifts and Anomaly Detection
- **Volume and Metric Deviations**: Do not apply rigid universal percentage thresholds (such as an arbitrary $>30\%$ cutoff) to declare anomalies across all metrics. Anomaly thresholds depend heavily on historical variability, baseline volatility, seasonality, expected business events, and data volume.
- **Investigation Sequence**:
  ```text
  Unexpected deviation detected
       ↓
  Compare with historical variation and baseline dispersion
       ↓
  Check pipeline health, ingestion logs, and instrumentation
       ↓
  Check known business events, marketing campaigns, and external factors
       ↓
  Investigate thoroughly before interpreting as business shift
  ```
- **Categorical Drift**: Unannounced spikes in "Unknown", "Other", or default fallback values signal upstream tracking changes, mobile app version migrations, or frontend schema drift.

## Outlier and Unusual Observation Protocol
Unusual observations (such as values exceeding $1.5 \times \text{IQR}$ or $|z| > 3$) must NEVER be treated as automatically invalid or deleted silently. Follow this investigation protocol:

```text
Unusual observation detected
     ↓
Investigate source, context, and logging
     ↓
Determine nature:
├── Technical Data Error (e.g., sensor glitch, test user, 99999 sentinel value) → Correct or filter with documentation
├── Valid Business Extreme (e.g., Black Friday whale customer, enterprise deal) → Retain; use robust statistics (median, IQR)
├── Distinct Subpopulation (e.g., wholesale buyer mixed with retail) → Segment into separate cohorts
└── Fraud / Security Anomaly → Retain and route to risk/security investigation
     ↓
Document remediation decision and business rationale transparently
```

## Data Quality Triage Workflow
When data quality fails during an analysis:
1. **Quarantine the Issue**: Isolate corrupted records using filtering flags (`is_valid_record = false`) rather than dropping them silently.
2. **Determine Scope and Blast Radius**: Identify which downstream tables, metrics, and dashboards are affected.
3. **Trace Provenance**: Identify whether the error occurred at collection (SDK bug), ingestion (ETL transformation), or query logic (bad join).
4. **Notify Stakeholders**: Communicate the quality gap, impacted metrics, and estimated time to resolve.

## Cross-References
- For understanding pipeline freshness, schema drift, and data engineering triage: [Data Engineering for Analysts](./data-engineering.md)
- For cleaning, deduplicating, and reshaping problematic data: [Data Wrangling and Transformation](./data-wrangling.md)
- For identifying anomalies and inspecting distributions during EDA: [Exploratory Data Analysis (EDA)](./eda.md)
- For maintaining data provenance, lineage, and audit trails: [Reproducibility and Governance](./reproducibility-and-governance.md)
