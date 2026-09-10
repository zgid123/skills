# SQL for Analysis

## Overview
SQL is the foundational query language for data analysis. Relational querying requires strict mental discipline around data grain, join cardinality, and aggregation boundaries. Before writing any analytical SQL query, establish the golden rule: **Define explicitly what one row of the output table represents.**

## The Analytical Grain
The grain is the level of atomic detail represented by a single row in a dataset. Changing the grain through aggregation or joins alters how measures must be interpreted:
- Customer grain: One row per customer (`customer_id`).
- Order grain: One row per order (`order_id`).
- Order item grain: One row per line item in an order (`order_id`, `item_id`).
- Daily user grain: One row per user per calendar date (`user_id`, `date`).

## Common Join Cardinality Pitfalls and Fanout
Joining tables with differing grains without proper aggregation causes **fanout (duplicate amplification)**:
- Joining `orders` (grain: `order_id`) to `order_line_items` (grain: `order_id`, `item_id`) multiplies order-level fields (e.g., shipping fee, order total) across every line item.
- Summing `orders.order_total` after an unaggregated line-item join silently overstates total revenue by $2\times, 5\times$, or $10\times$.
- **Mitigation Protocol**: Always aggregate the child table to the parent grain before joining, or use CTEs with validated unique primary keys.

```sql
-- DANGEROUS: Fanout multiplies shipping_fee
SELECT SUM(o.shipping_fee) AS total_shipping
FROM orders o
JOIN order_line_items li ON o.order_id = li.order_id;

-- CORRECT: Pre-aggregate line items or query orders directly
SELECT SUM(shipping_fee) AS total_shipping
FROM orders;
```

## Core Analytical SQL Techniques

### 1. Conditional Aggregation
Execute multi-segment aggregations in a single scan using `CASE WHEN`:
```sql
SELECT
  DATE_TRUNC('month', order_date) AS order_month,
  COUNT(DISTINCT order_id) AS total_orders,
  COUNT(DISTINCT CASE WHEN status = 'completed' THEN order_id END) AS completed_orders,
  SUM(CASE WHEN payment_method = 'credit_card' THEN amount ELSE 0 END) AS credit_card_volume,
  ROUND(100.0 * COUNT(DISTINCT CASE WHEN status = 'completed' THEN order_id END) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS completion_rate_pct
FROM orders
GROUP BY 1
ORDER BY 1;
```

### 2. Analytical Window Functions
Window functions calculate metrics across a set of rows related to the current row without collapsing rows into a single summary:
- **`ROW_NUMBER()` vs. `RANK()` vs. `DENSE_RANK()`**:
  - `ROW_NUMBER()` assigns sequential integers ($1, 2, 3, 4$) deterministically (ideal for deduplication).
  - `RANK()` leaves gaps on ties ($1, 2, 2, 4$).
  - `DENSE_RANK()` leaves no gaps on ties ($1, 2, 2, 3$).
- **`LAG()` and `LEAD()`**: Access values from preceding or subsequent rows without self-joins.
- **Running Totals and Moving Averages**:
  ```sql
  SELECT
    metric_date,
    daily_revenue,
    SUM(daily_revenue) OVER (ORDER BY metric_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue,
    AVG(daily_revenue) OVER (ORDER BY metric_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d_avg_revenue
  FROM daily_metrics;
  ```
- **Percent of Total**:
  ```sql
  SELECT
    category,
    revenue,
    ROUND(100.0 * revenue / SUM(revenue) OVER (), 2) AS pct_of_total
  FROM category_summary;
  ```

### 3. Deterministic Deduplication
Use `ROW_NUMBER()` inside a CTE to resolve duplicate updates or webhook retries. Always include a deterministic tie-breaker (such as an auto-incrementing ID or hash) so that identical timestamps do not produce non-deterministic results across runs:
```sql
WITH ranked_records AS (
  SELECT
    order_id,
    customer_id,
    order_status,
    updated_at,
    event_id,
    ROW_NUMBER() OVER (
      PARTITION BY order_id 
      ORDER BY updated_at DESC, event_id DESC
    ) AS ranking
  FROM raw_orders
)
SELECT order_id, customer_id, order_status, updated_at, event_id
FROM ranked_records
WHERE ranking = 1;
```

### 4. Cohort Retention Analysis
Compute triangular cohort retention matrices by joining user signup cohorts to activity events:
```sql
WITH user_cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('month', created_at) AS cohort_month
  FROM users
),
monthly_activity AS (
  SELECT
    user_id,
    DATE_TRUNC('month', event_timestamp) AS activity_month
  FROM user_events
  GROUP BY 1, 2
)
SELECT
  c.cohort_month,
  -- Calculate month offset: 0, 1, 2, ...
  EXTRACT(YEAR FROM a.activity_month) * 12 + EXTRACT(MONTH FROM a.activity_month) -
  (EXTRACT(YEAR FROM c.cohort_month) * 12 + EXTRACT(MONTH FROM c.cohort_month)) AS period_offset,
  COUNT(DISTINCT c.user_id) AS active_users
FROM user_cohorts c
JOIN monthly_activity a ON c.user_id = a.user_id
GROUP BY 1, 2
ORDER BY 1, 2;
```

### 5. Period-Over-Period (PoP) Comparisons
Compare current metrics against prior month (MoM) or prior year (YoY) with proper date truncation:
```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC('month', order_date) AS rev_month,
    SUM(order_amount) AS revenue
  FROM orders
  GROUP BY 1
)
SELECT
  rev_month,
  revenue AS current_revenue,
  LAG(revenue, 1) OVER (ORDER BY rev_month) AS prev_month_revenue,
  LAG(revenue, 12) OVER (ORDER BY rev_month) AS prev_year_revenue,
  ROUND(100.0 * (revenue - LAG(revenue, 1) OVER (ORDER BY rev_month)) / NULLIF(LAG(revenue, 1) OVER (ORDER BY rev_month), 0), 2) AS mom_growth_pct,
  ROUND(100.0 * (revenue - LAG(revenue, 12) OVER (ORDER BY rev_month)) / NULLIF(LAG(revenue, 12) OVER (ORDER BY rev_month), 0), 2) AS yoy_growth_pct
FROM monthly_revenue
ORDER BY rev_month;
```

### 6. Funnel and Drop-Off Analysis
Sequential funnels require strict chronological ordering, explicit entity/session boundaries, and conversion timeframes. Do not count mere independent event presence as an ordered funnel completion:

```sql
-- Ordered session funnel requiring step_1 <= step_2 <= step_3 <= step_4 within the session
WITH step_events AS (
  SELECT
    session_id,
    user_id,
    MIN(CASE WHEN event_name = 'landing_view' THEN event_timestamp END) AS t_landing,
    MIN(CASE WHEN event_name = 'product_view' THEN event_timestamp END) AS t_product,
    MIN(CASE WHEN event_name = 'add_to_cart' THEN event_timestamp END) AS t_cart,
    MIN(CASE WHEN event_name = 'checkout_complete' THEN event_timestamp END) AS t_checkout
  FROM session_events
  GROUP BY session_id, user_id
),
ordered_funnel AS (
  SELECT
    session_id,
    CASE WHEN t_landing IS NOT NULL THEN 1 ELSE 0 END AS s1_landing,
    CASE WHEN t_landing IS NOT NULL AND t_product >= t_landing THEN 1 ELSE 0 END AS s2_product,
    CASE WHEN t_landing IS NOT NULL AND t_product >= t_landing AND t_cart >= t_product THEN 1 ELSE 0 END AS s3_cart,
    CASE WHEN t_landing IS NOT NULL AND t_product >= t_landing AND t_cart >= t_product AND t_checkout >= t_cart THEN 1 ELSE 0 END AS s4_checkout
  FROM step_events
)
SELECT
  SUM(s1_landing) AS landing_sessions,
  SUM(s2_product) AS product_sessions,
  SUM(s3_cart) AS cart_sessions,
  SUM(s4_checkout) AS completed_checkout_sessions,
  ROUND(100.0 * SUM(s4_checkout) / NULLIF(SUM(s1_landing), 0), 2) AS end_to_end_cvr_pct
FROM ordered_funnel;
```

## Common SQL Analytical Anti-Patterns and Mistakes
1. **The Unweighted Ratio Confusion**: Mixing up ratio-of-aggregates (`SUM(conv) / SUM(visitors)`) with unweighted average-of-ratios (`AVG(cvr)`), failing to match the intended business estimand.
2. **Silent NULL Propagation**: Forgetting that `COUNT(column)` ignores `NULL`s while `COUNT(*)` counts all rows, and `1 + NULL = NULL`.
3. **Division by Zero**: Failing to wrap denominators in `NULLIF(denominator, 0)`, which causes catastrophic runtime query failure.
4. **Non-SARGable Queries**: Using functions on indexed columns in `WHERE` clauses (e.g., `WHERE DATE(order_timestamp) = '2025-01-01'`) preventing database index utilization; use explicit ranges instead (`WHERE order_timestamp >= '2025-01-01' AND order_timestamp < '2025-01-02'`).
5. **Accidental Cross Joins**: Omitting join conditions or joining on non-unique keys, generating massive unintended Cartesian row explosions.
6. **Timezone Discrepancies**: Storing timestamps in UTC while reporting daily metrics in an undefined or mixed timezone. Canonical storage should use a consistent representation (commonly UTC), but business reporting days must align with explicitly defined business/local reporting boundaries.

## Query Validation Checklist
Before sharing or visualizing the results of any analytical SQL query:
- [ ] What does one row of the output represent?
- [ ] Did `COUNT(*)` change unexpectedly after any `JOIN` operation?
- [ ] Are all division operations protected against division by zero with `NULLIF`?
- [ ] Do grouped sums reconcile with the total unaggregated source table?
- [ ] Are timestamps canonically stored and aligned with the designated business reporting timezone?

## Cross-References
- For metric definitions, ratio pitfalls, and unit economics: [Metrics and KPIs](./metrics-and-kpis.md)
- For data quality profiling and schema invariants: [Data Quality](./data-quality.md)
- For downstream exploratory data analysis on SQL extracts: [Exploratory Data Analysis (EDA)](./eda.md)
- For dimensional warehouse concepts (star schema, fact/dim tables): [Data Engineering for Analysts](./data-engineering.md)
