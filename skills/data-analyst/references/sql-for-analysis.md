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
    AVG(daily_revenue) OVER (ORDER BY metric_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7_observations_avg_revenue
  FROM daily_metrics;
  ```
  A `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` frame covers seven observations, not necessarily seven calendar days. Use it as a seven-day window only after verifying exactly one row exists for every calendar day. Otherwise, join to a complete date spine or use a dialect-supported interval range frame.
- **Percent of Total**:
  ```sql
  SELECT
    category,
    revenue,
    ROUND(100.0 * revenue / NULLIF(SUM(revenue) OVER (), 0), 2) AS pct_of_total
  FROM category_summary;
  ```
  When the total is zero, the percentage is undefined and remains `NULL`; if a different zero-total policy is required, state it explicitly.

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
Compare current metrics against the exact prior calendar month or year. Positional `LAG(..., 1)` means "previous observed row," which is not necessarily the previous month when periods are missing. Use exact-period joins or build a complete calendar spine:
```sql
WITH monthly_revenue AS (
  SELECT
    DATE_TRUNC('month', order_date) AS rev_month,
    SUM(order_amount) AS revenue
  FROM orders
  GROUP BY 1
)
SELECT
  current.rev_month,
  current.revenue AS current_revenue,
  previous_month.revenue AS prev_month_revenue,
  previous_year.revenue AS prev_year_revenue,
  ROUND(100.0 * (current.revenue - previous_month.revenue) / NULLIF(previous_month.revenue, 0), 2) AS mom_growth_pct,
  ROUND(100.0 * (current.revenue - previous_year.revenue) / NULLIF(previous_year.revenue, 0), 2) AS yoy_growth_pct
FROM monthly_revenue current
LEFT JOIN monthly_revenue previous_month
  ON previous_month.rev_month = current.rev_month - INTERVAL '1 month'
LEFT JOIN monthly_revenue previous_year
  ON previous_year.rev_month = current.rev_month - INTERVAL '1 year'
ORDER BY current.rev_month;
```
The interval syntax varies by SQL dialect. If a missing period should represent zero rather than unknown, make that business rule explicit and materialize the missing period with a calendar spine before calculating growth.

### 6. Funnel and Drop-Off Analysis
Sequential funnels require a defined chronological ordering rule, explicit entity/session boundaries, and conversion timeframes. Select each step only after the timestamp selected for the preceding step; independently taking the first occurrence of every event can miss a valid later sequence.

```sql
-- Ordered funnel at session grain; session_id must uniquely bound the funnel window
WITH landing AS (
  SELECT
    session_id,
    MIN(event_timestamp) AS t_landing
  FROM session_events
  WHERE event_name = 'landing_view'
  GROUP BY session_id
),
product AS (
  SELECT
    l.session_id,
    l.t_landing,
    MIN(e.event_timestamp) AS t_product
  FROM landing l
  LEFT JOIN session_events e
    ON e.session_id = l.session_id
   AND e.event_name = 'product_view'
   AND e.event_timestamp >= l.t_landing
  GROUP BY l.session_id, l.t_landing
),
cart AS (
  SELECT
    p.session_id,
    p.t_landing,
    p.t_product,
    MIN(e.event_timestamp) AS t_cart
  FROM product p
  LEFT JOIN session_events e
    ON e.session_id = p.session_id
   AND e.event_name = 'add_to_cart'
   AND e.event_timestamp >= p.t_product
  GROUP BY p.session_id, p.t_landing, p.t_product
),
checkout AS (
  SELECT
    c.session_id,
    c.t_landing,
    c.t_product,
    c.t_cart,
    MIN(e.event_timestamp) AS t_checkout
  FROM cart c
  LEFT JOIN session_events e
    ON e.session_id = c.session_id
   AND e.event_name = 'checkout_complete'
   AND e.event_timestamp >= c.t_cart
  GROUP BY c.session_id, c.t_landing, c.t_product, c.t_cart
)
SELECT
  COUNT(*) AS landing_sessions,
  COALESCE(SUM(CASE WHEN t_product IS NOT NULL THEN 1 ELSE 0 END), 0) AS product_sessions,
  COALESCE(SUM(CASE WHEN t_cart IS NOT NULL THEN 1 ELSE 0 END), 0) AS cart_sessions,
  COALESCE(SUM(CASE WHEN t_checkout IS NOT NULL THEN 1 ELSE 0 END), 0) AS completed_checkout_sessions,
  ROUND(100.0 * COALESCE(SUM(CASE WHEN t_checkout IS NOT NULL THEN 1 ELSE 0 END), 0) / NULLIF(COUNT(*), 0), 2) AS end_to_end_cvr_pct
FROM checkout;
```

This example treats `session_id` as the unique funnel entity and the session itself as the conversion window. If session IDs are not globally unique, use the actual composite session key; if sessions do not impose the required maximum duration, add an explicit upper time bound. The example allows equal timestamps with `>=`; use `>` when the event contract guarantees strict ordering and simultaneous events must not count.

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
