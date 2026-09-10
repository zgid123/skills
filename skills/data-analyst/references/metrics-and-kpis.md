# Metrics and KPIs

## Overview
A metric is a quantifiable measure used to track, evaluate, and assess the status of a specific business process. A Key Performance Indicator (KPI) is a select metric tied directly to strategic organizational objectives, indicating whether a business goal is being achieved. Every metric requires an unambiguous mathematical formulation, explicit population boundaries (grain), and defined temporal windows.

## Core Metric Concepts and Anatomy

### Dimensions vs. Measures
- **Measure**: A numerical value that can be computed, aggregated, or mathematically evaluated (e.g., `revenue`, `session_duration_seconds`, `order_count`).
- **Dimension**: A qualitative attribute or categorical slice that segments, filters, or groups measures (e.g., `country`, `acquisition_channel`, `device_category`, `subscription_tier`).

### Grain and Aggregation
- **Metric Grain**: The atomic level of detail at which a metric is computed or grouped (e.g., "Daily active users per country" vs. "Monthly active users globally").
- **Aggregation Types**:
  - **Additive Metrics**: Can be meaningfully summed across all dimensions and time (e.g., `sales_volume`, `revenue_usd`, `error_count`).
  - **Semi-Additive Metrics**: Can be summed across some dimensions (such as region or department) but NOT across time (e.g., `inventory_stock_balance`, `account_balance`, `headcount`). For time aggregations, use end-of-period snapshots or time-weighted averages.
  - **Non-Additive Metrics**: Cannot be directly summed across any dimension (e.g., ratios, rates, averages, percentages, medians, unit prices). They must be computed by aggregating raw numerators and denominators independently before dividing.

### Numerators, Denominators, and Population Boundaries
- Every rate or ratio metric requires explicit definitions for its numerator, denominator, and boundary exclusions:
  - **Numerator**: The count, volume, or sum of the target event (e.g., completed checkouts).
  - **Denominator**: The eligible exposure base or opportunity pool (e.g., unique user sessions that reached the checkout step).
  - **Exclusion Criteria**: System test accounts, internal employee sessions, bot traffic, refunded orders, or unverified registrations.
- **Ratio Estimand Distinction: Ratio of Aggregates vs. Average of Ratios**:
  - $\text{AVG}(\text{revenue} / \text{users})$ and $\text{SUM}(\text{revenue}) / \text{SUM}(\text{users})$ are not "wrong" vs. "right" in the abstract; they estimate different quantities because they imply different weighting schemes:
    - **Ratio of Aggregates** ($\frac{\sum \text{revenue}}{\sum \text{users}}$): Estimates the overall population rate. Larger units (e.g., large enterprise accounts or high-traffic days) contribute proportionally to their volume.
    - **Average of Ratios** ($\text{AVG}(\frac{\text{revenue}}{\text{users}})$): Estimates the unweighted mean rate across units. Every unit (e.g., micro-account vs. enterprise) contributes equally regardless of size.
  - *Hard Rule*: Always define the intended estimand explicitly by specifying: (1) unit of analysis, (2) weighting, (3) numerator, (4) denominator, and (5) aggregation level. Mixing them up distorts business conclusions.

## Metric Classification and Hierarchy

### 1. The North Star Metric and Metric Trees
- **North Star Metric (NSM)**: The single focal metric that best captures the core customer value delivered and sustainable business growth (e.g., Spotify: "Time spent listening"; Airbnb: "Nights booked").
- **Metric Tree (Hierarchy)**: Decomposes the high-level North Star metric into operational input levers:
  ```text
  Revenue = Active Customers × Purchase Frequency × Average Order Value
     ├── Active Customers = New Customers + Retained Customers - Churned Customers
     ├── Purchase Frequency = Total Orders / Active Customers
     └── Average Order Value = Total Basket Value / Total Orders
  ```

### 2. Input vs. Output Metrics
- **Output Metrics (Lagging)**: Measure final business outcomes after activities take place (e.g., Monthly Revenue, Quarterly Churn Rate, Gross Margin). They are non-actionable in the immediate term.
- **Input Metrics (Leading)**: Operational measures that reflect early activities, user behaviors, or system performances that teams can often influence directly or indirectly to drive downstream outputs (e.g., Weekly Qualified Leads, Onboarding Activation Rate, Support Response Time).

### 3. Primary, Secondary, and Guardrail Metrics
- **Primary Metric**: The core outcome metric targeted by a specific initiative or experiment (e.g., "Increase checkout completion rate by 2 pp").
- **Secondary Metrics**: Supporting indicators that provide diagnostic context on how the primary metric moved (e.g., cart abandonment rate, average checkout latency).
- **Guardrail Metrics**: Critical operational, experience, or business metrics that must not degrade while optimizing the primary metric (e.g., page load latency, refund rate, customer support contact rate, gross margin).

## Standard Business and Product Metric Archetypes

### Engagement and Growth
- **DAU / WAU / MAU**: Daily, Weekly, and Monthly Active Users. Requires a strict definition of what constitutes an "active" user (e.g., executing a core product interaction, not merely opening a push notification).
- **DAU / MAU Stickiness Ratio**: Measures population-level activity frequency:
  $$\text{DAU} / \text{MAU} \approx \frac{\text{Average Daily Active Population}}{\text{Monthly Active Population}}$$
  *Interpretation*: It serves as a population-level stickiness or engagement-frequency proxy. Under suitable assumptions, it reflects how frequently active users return across a 30-day window, but it should not be described as a literal, individual per-user percentage of active days without inspecting user-level frequency distributions.
- **Conversion Rate (CVR)**:
  $$\text{CVR} = \frac{\text{Unique Converters}}{\text{Unique Eligible Visitors in Funnel}}$$

### Retention, Churn, and Cohort Dynamics
- **Cohort Retention Rate**: Percentage of users from an acquisition cohort who remain active in period $t$ after signup:
  $$\text{Retention Rate}(t) = \frac{\text{Active Users in Period } t \text{ from Cohort } c}{\text{Total Initial Users in Cohort } c}$$
- **User Churn Rate**: The proportion of active subscribers or users who cancel or fail to renew over a specific window:
  $$\text{User Churn Rate} = \frac{\text{Users Lost During Period}}{\text{Active Users at Start of Period}}$$
- **Net Revenue Retention (NRR)**: Tracks revenue expansion, contraction, and churn from existing customers over a timeframe:
  $$\text{NRR} = \frac{\text{Starting ARR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting ARR}} \times 100\%$$
- **Gross Revenue Retention (GRR)**: Measures recurring revenue preserved without counting expansion:
  $$\text{GRR} = \frac{\text{Starting ARR} - \text{Contraction} - \text{Churn}}{\text{Starting ARR}} \times 100\% \quad (\le 100\%)$$

### Unit Economics and Financial Metrics
- **MRR / ARR**: Monthly Recurring Revenue and Annual Recurring Revenue from active recurring subscriptions (excludes one-off fees).
- **Average Order Value (AOV)**:
  $$\text{AOV} = \frac{\text{Total Gross Revenue}}{\text{Total Order Count}}$$
- **Average Revenue Per User (ARPU)**:
  $$\text{ARPU} = \frac{\text{Total Revenue in Period}}{\text{Total Active Users in Period}}$$
- **Customer Acquisition Cost (CAC)**:
  $$\text{CAC} = \frac{\text{Total Sales and Marketing Spend}}{\text{Total New Customers Acquired}}$$
- **Customer Lifetime Value (LTV)**:
  - *Simplified Steady-State Approximation*:
    $$\text{LTV} \approx \frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Customer Churn Rate}}$$
  - *Heuristic Limitation*: This simple formula assumes a constant churn rate, constant ARPU, infinite horizon, and steady-state conditions. In practice, realistic LTV estimation depends heavily on:
    - Cohort-based retention decay curves (churn is rarely constant across tenure);
    - Discount rate / cost of capital;
    - Time horizon bounds (e.g., 1-year, 3-year, or 5-year capped LTV);
    - Contractual (subscription) vs. non-contractual (e-commerce repeat purchase) business models;
    - Revenue distribution skewness and account expansion.
- **LTV / CAC Ratio**: Benchmark heuristic for acquisition efficiency (typical target $> 3.0$ under steady-state assumptions, evaluated alongside payback period).

## Semantic Definitions, Time Windows, and Governance
- **Semantic Definition Standard**: Every metric documented in the company data catalog must specify:
  - Human-readable name and acronym.
  - Business objective and rationale.
  - Precise SQL computation logic against authoritative data warehouse tables.
  - Default aggregation time window (e.g., calendar day UTC, rolling 7-day, calendar month).
  - Metric owner and domain steward accountable for definition governance.
- **Time Windows and Normalization**:
  - Distinguish between **calendar-aligned periods** (calendar month, fiscal quarter) and **rolling windows** (trailing 7 days, trailing 28 days). Rolling windows smooth weekly seasonality.
  - Never compare an incomplete partial period directly against a completed baseline period without day-by-day normalization.

## Metric Pitfalls and Anti-Patterns
- **Percentage vs. Percentage Point Confusion**: A change from $10\%$ to $12\%$ is an increase of $+2\text{ percentage points (pp)}$, or a $+20\%$ relative increase. Mixing these confuses executives and models.
- **Denominator Shifts**: A rising conversion rate caused by collapsing top-of-funnel traffic (fewer total visitors) rather than increased conversions is an operational problem, not a success.
- **Vanity Over Value**: Prioritizing cumulative signups or raw page views over active usage, retained accounts, and unit profitability.
- **Metric Proliferation**: Tracking 50 metrics with equal priority instead of a structured hierarchy with defined primary, secondary, and guardrail metrics.

## Cross-References
- For SQL aggregation, window functions, and cohort query formulation: [SQL for Analysis](./sql-for-analysis.md)
- For testing metric movements and calculating confidence intervals: [Statistics and Statistical Inference](./statistics-and-inference.md)
- For setting primary, secondary, and guardrail metrics in A/B tests: [Experimentation and A/B Testing](./experimentation.md)
- For organizing KPIs into visual executive and operational monitoring interfaces: [Dashboards and BI](./dashboards-and-bi.md)
