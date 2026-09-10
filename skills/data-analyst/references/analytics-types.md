# Analytics Types and Selection

## The Four Core Types of Analytics

Data analytics is categorized into four primary types based on the nature of the inquiry and the decision objective. A comprehensive real-world business investigation often traverses multiple types sequentially:

```text
Descriptive ("What happened?")
       ↓
Diagnostic ("Why did it happen?")
       ↓
Predictive ("What is likely to happen next?")
       ↓
Prescriptive ("What action should we take?")
```

### 1. Descriptive Analytics
- **Core Question**: *"What happened? What is our current operational state?"*
- **Purpose**: Quantify, categorize, and summarize historical and present facts to establish baselines, track performance trends, and provide operational visibility.
- **Typical Business Questions**:
  - What was our total gross merchandise value (GMV) by product category last month?
  - How many daily active users (DAU) logged into the platform across regions this week?
  - What is the current inventory stock level across regional fulfillment centers?
- **Common Methods**:
  - Summary statistics (mean, median, quantiles, variance, IQR).
  - Frequency distributions and cross-tabulations.
  - Grouped relational aggregations (SUM, COUNT, AVG in SQL).
  - Time-series plots, categorical bar charts, and operational summary scorecards.
- **Outputs**: Weekly KPI reports, executive dashboards, historical performance summaries.
- **Limitations**: Solely retrospective; provides zero explanation of underlying mechanisms or drivers.

### 2. Diagnostic Analytics
- **Core Question**: *"Why did it happen? What components, segments, or historical factors drove this shift?"*
- **Purpose**: Investigate root drivers, isolate anomalies, decompose metrics into mathematical sub-components, and determine structural contributors to observed changes.
- **Typical Business Questions**:
  - Why did checkout conversion drop by 14% following the latest mobile app release?
  - Which customer segment drove the sudden spike in subscription cancellations?
  - Did the revenue decline result from lower active buyer volume, fewer orders, or smaller basket sizes?
- **Common Methods**:
  - Mathematical metric tree decomposition ($Revenue = Volume \times Price \times Mix$).
  - Slice-and-dice dimensional contribution analysis (absolute volume vs. relative percentage shift).
  - Hypothesis issue trees and falsification testing.
  - Cohort retention decay curves and funnel drop-off analysis.
- **Outputs**: Root cause diagnostic memos, issue tree validations, metric decomposition waterfalls.
- **Limitations**: Identifies empirical drivers and historical segment contributions; answering causal questions (*"Would changing X change Y?"*) requires randomized experimentation or formal causal identification strategies.

### 3. Predictive Analytics (at Analyst Depth)
- **Core Question**: *"What is likely to happen next?"*
- **Purpose**: Estimate future metric trajectories, project probabilities of specific events, and score future outcomes based on historical patterns and relationships.
- **Typical Business Questions**:
  - What is our expected recurring revenue for the next two quarters?
  - Which active customer accounts have a high probability of churn over the next 60 days?
  - What will warehouse order demand be across regions next month?
- **Common Methods**:
  - Baseline heuristic projections (naive, seasonal naive, moving average).
  - Classical time-series forecasting (Holt-Winters, ARIMA).
  - Supervised regression (OLS linear regression) for continuous outcomes.
  - Supervised classification (logistic regression) for binary probabilities.
- **Outputs**: Estimated event probabilities and risk scores, demand forecasts with prediction intervals, churn risk tiers.
- **Limitations**: Predictions are probabilistic estimates carrying uncertainty; models assume historical relationships hold and are vulnerable to sudden regime shifts, black swan events, and data leakage. Advanced deep learning and complex MLOps remain out of scope for general analytics.

### 4. Prescriptive Analytics
- **Core Question**: *"What specific action should we take?"*
- **Purpose**: Evaluate alternative decisions, quantify trade-offs, model scenario outcomes, and recommend optimal operational actions subject to real-world constraints.
- **Typical Business Questions**:
  - How should marketing budget be allocated across 6 channels to maximize acquisition subject to target CAC?
  - What price adjustment maximizes contribution margin given estimated price elasticity?
  - How should customer support staffing be scheduled across shifts to meet SLA response targets?
- **Common Methods**:
  - Scenario simulation and sensitivity analysis (best-case, base-case, worst-case).
  - Decision payoff matrices and expected value calculations.
  - Trade-off optimization models (linear programming).
  - Controlled A/B testing and policy rollouts.
- **Outputs**: Strategic recommendations, scenario comparison tables, budget allocation models, action plans.
- **Limitations**: Highly sensitive to underlying assumptions, model formulation errors, and unmodeled real-world externalities.

## Multi-Type Analytical Problem Solving
Most significant business problems require combining analytical types. For example, investigating a revenue slump:
1. **Descriptive**: Establish that total revenue fell 8% MoM in June.
2. **Diagnostic**: Decompose the drop to reveal a 25% drop in enterprise renewals, driven by a new competitor pricing tier.
3. **Predictive**: Forecast ARR trajectory over the next 3 quarters if enterprise renewal rates remain depressed.
4. **Prescriptive**: Model three retention pricing interventions and recommend offering a multi-year discount to protect key accounts.

## Guidance for Methodology Selection
- **Distinguish Prediction, Diagnosis, and Causation**:
  - *Predictive question*: What is likely to happen?
  - *Diagnostic question*: Why did it happen?
  - *Causal question*: Would changing X change Y?
  Do not conflate them. Prediction and explanation are different analytical goals: a model can provide accurate predictive scores without establishing why the outcome occurs causally, and identifying historical drivers does not prove that an operational intervention on those drivers will produce the desired change.
- **Establish Descriptive Baseline First**: Always verify data quality, definitions, and descriptive baseline distributions before building predictive or prescriptive models.
- **Favor Simplicity**: The simplest method that defensibly answers the business question is the preferred method. Do not deploy machine learning when relational SQL aggregation or cohort slicing solves the stakeholder problem.

## Cross-References
- For end-to-end analytical workflow stages: [The Analytics Lifecycle](./analytics-lifecycle.md)
- For framing analytical questions and business decisions: [Problem Definition and Framing](./problem-definition.md)
- For metric decomposition and KPI structures: [Metrics and KPIs](./metrics-and-kpis.md)
- For analyst-level forecasting and regression: [Time-Series Analysis](./time-series-analysis.md), [Predictive Analysis](./predictive-analysis.md)
- For randomized experiment design and treatment effect estimation: [Experimentation and A/B Testing](./experimentation.md)
