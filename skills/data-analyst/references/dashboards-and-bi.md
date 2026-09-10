# Dashboards and Business Intelligence (BI)

## Overview
A business intelligence dashboard is a visual decision-support interface, not a dumping ground for every query and chart an analyst created. Effective dashboards provide rapid cognitive orientation, display metric status against benchmarks, enable disciplined drill-downs, and prompt timely business actions.

## The Three Core Dashboard Archetypes

| Archetype | Primary Audience | Core Question | Update Cadence | Key Characteristics |
|---|---|---|---|---|
| **Executive / Strategic** | C-Suite, VPs, Board | *"Are we on track to hit our strategic goals?"* | Monthly / Weekly | High-level North Star KPIs, period-over-period targets, minimal filters, uncluttered summary scorecards. |
| **Operational** | Frontline managers, Team leads, Operations | *"Is anything broken right now that requires intervention?"* | Real-time / Hourly / Daily | Live health status, threshold alert banners, exception lists, operational bottlenecks, task-oriented. |
| **Analytical / Exploratory** | Product managers, Functional analysts, Domain leads | *"What segments, trends, or behaviors drive current performance?"* | Daily / Weekly | Interactive dimensional filters, cohort slicing, drill-downs, correlation views, deeper data tables. |

## Information Hierarchy and Visual Layout

Follow the **F-Pattern** or **Z-Pattern** reading flow to establish visual hierarchy:
- **Top Row (Executive Headline Scorecard)**: 3 to 5 single-value metric cards displaying the primary KPIs, current period values, historical baseline comparisons (e.g., vs. prior month or budget), and directional trend arrows.
- **Middle Section (Core Trends & Drivers)**: 1 or 2 focal time-series or category charts decomposing the primary KPIs over time and across major business dimensions.
- **Bottom Section (Granular Breakdown & Exceptions)**: Segmented breakdowns, geographic heatmaps, top/bottom performance tables, or exception lists for operational follow-up.

## Dashboard Design Best Practices

### 1. Contextual Reference Points (Heuristic)
- A naked number (e.g., *"Revenue: $4.2M"*) provides zero actionable context. Include only the contextual information required to support the dashboard's intended decisions:
  - **Temporal Baselines**: Prior period comparison (MoM, YoY, vs. trailing 7-day average).
  - **Plan / Target**: Budgeted milestones or forecasted expectations.
  - **Benchmarked Health / Thresholds**: Color-coded status indicators (on-track, at-risk, breached) when actionable thresholds exist.
- *Guidance*: The appropriate contextual references depend on the audience, decision stakes, and update cadence.

### 2. Disciplined Filter Design
- Establish intuitive global filters at the top of the canvas (e.g., Date Range, Region, Product Line, Customer Tier).
- Set sensible, standardized default filter states (e.g., "Trailing 30 Days", "All Active Regions").
- Avoid creating dozens of granular multi-select dropdowns that confuse non-technical users and trigger massive unindexed database queries.

### 3. Drill-Down and Progressive Disclosure
- Allow users to click on high-level chart elements to drill into underlying granular dimensions (e.g., clicking on a regional drop in revenue opens a sub-view filtered to that specific region's product mix).
- Keep initial views simple; hide secondary technical attributes behind click-to-expand details.

### 4. Data Freshness, Latency, and SLAs
- Explicitly display data freshness metadata in the header: *"Data updated as of: 2025-06-15 06:00 UTC (Daily batch sync)"*.
- Document the refresh schedule and underlying source table pipeline SLAs so stakeholders know when numbers are finalized.

### 5. Query Performance and BI Scalability
- **Pre-Aggregated Summary Tables**: Avoid pointing high-traffic executive dashboards directly at raw, billion-row event tables. Have analytics engineers build pre-aggregated, indexed data warehouse summary marts (e.g., via dbt).
- **Visual Card Count (Heuristic)**: Aim for a focused set of visual elements (a common starting heuristic is 6 to 9 cards per view). Dashboard density should depend on the target audience, decision urgency, screen size, information hierarchy, and metric complexity: include only the cards necessary to support the target decision.
- **Cache Strategy**: Leverage BI query caching layers to serve frequent dashboard views without hitting underlying cloud warehouse compute repeatedly.

## Dashboard Governance and Lifecycle
- **Metric Definitions Standard**: Every metric card should include an info tooltip (`ℹ️`) providing the canonical semantic definition, numerator, denominator, and business owner.
- **Sunset Deprecated Dashboards**: Track dashboard view logs periodically. Archive and deprecate abandoned reports to prevent metric drift and conflicting sources of truth.
- **Tool-Agnostic Application**: While implementations vary across platforms (e.g., Tableau, Looker, Power BI, Metabase, Apache Superset), the architectural principles of grain, layout hierarchy, and decision utility remain identical.

## Common Dashboard Anti-Patterns
- **The "Kitchen Sink" Dashboard**: Cramming 25 unrelated charts into a single endless page with no visual hierarchy or unified theme.
- **The Unvalidated Query**: Publishing dashboard tiles with unverified joins that silently produce duplicate rows or mismatched totals.
- **The Abandoned Orphan**: Building custom one-off dashboards for a single ad-hoc meeting and leaving them running indefinitely.
- **Alert Fatigue**: Flooding operational teams with dozens of non-actionable yellow and red status banners.

## Cross-References
- For KPI architecture, metric trees, and ratio definitions: [Metrics and KPIs](./metrics-and-kpis.md)
- For chart selection, color usage, and data-to-ink ratio: [Visualization and Storytelling](./visualization-and-storytelling.md)
- For data warehouse dimensional modeling (fact/dim tables): [Data Engineering for Analysts](./data-engineering.md)
- For data quality profiling and freshness validation: [Data Quality](./data-quality.md)
