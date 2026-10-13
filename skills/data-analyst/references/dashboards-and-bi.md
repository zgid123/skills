# Dashboards and Business Intelligence (BI)

## Overview
A business intelligence dashboard is a visual decision-support interface, not a dumping ground for every query and chart an analyst created. Effective dashboards provide rapid cognitive orientation, display metric status against benchmarks, enable disciplined drill-downs, and prompt timely business actions.

## Build and Delivery Contract

When the delivery contract calls for a dashboard, create one the stakeholder can open and inspect. For other substantial work, use the agreed report format. Choose the audience, question, acceptance criteria, and delivery format during Business Understanding. A written dashboard specification alone is sufficient only when requested or when data/tool access prevents implementation and that limitation is explicit.

### Tool and Artifact Selection

1. Inspect the project and accessible BI capabilities. Extend existing dashboards, metric definitions, components, and chart libraries where appropriate.
2. If no suitable tooling exists, create portable HTML with minimal dependencies. Prefer a self-contained artifact that opens locally; document any required server, network assets, or setup. Do not add an application framework solely to display a static analysis.
3. Add date or segment filters and drill-downs only when they help the stakeholder answer the analytical question. A dashboard can be a static snapshot; identify its coverage, extraction time, and manual refresh process.
4. For focused questions, use a chart, visual report, or compact result table instead. Respect explicit output constraints such as SQL-only requests.
5. If evidence is unavailable, state what is blocked and supply a clearly labeled specification or illustrative prototype when useful. Keep sample data visibly distinct from measured results and never claim that an unexecuted query or prototype is verified.

### Finding-to-Interface Coverage

For substantial visual deliverables, maintain a compact internal review map; it need not appear on the dashboard:

| Priority question | Material finding | Supporting comparison | Presentation choice and rationale | Reader-facing location |
|---|---|---|---|---|
| Question from the brief | Supported answer, including consequential follow-up | Evidence needed to assess the conclusion | Chart, table or prose suited to the comparison | Page/section, view/filter state, or linked rendered-report anchor |

Update the map when sensitivity or subgroup evidence materially changes interpretation. Flag important findings available only in supporting files, missing comparisons and uninspected locations; these are gaps to resolve or disclose as incomplete delivery. A shared view can support several findings, and one finding can need several comparisons. This is a coverage check, not a chart quota. Choose presentation using [Visualization and storytelling](./visualization-and-storytelling.md); existing components and fixed templates must not dictate the analytical comparison.

### Readable Browser Delivery

When browser delivery is required, essential findings, explanations, denominators and limitations must be readable in the dashboard or a linked rendered report. Raw Markdown, CSV, code and logs are supporting downloads; their existence or links do not establish readable delivery. Respect an explicit Markdown-only or other format request instead.

Use progressive disclosure for methods, definitions, quality checks and detailed evidence through labeled sections, expandable details or rendered-report links. Do not embed or render every supporting artifact. If both dashboard and report are required, define each artifact's role and inspect both: a strong report cannot compensate for material dashboard omissions. A dashboard may summarize a consequential result and link to its readable comparison, but cannot omit that result entirely when it belongs to its agreed role.

When sensitivity or subgroup comparisons alter a headline, expose enough of the baseline and alternative evidence to assess the change. An isolated adjusted number or dense callout is insufficient when readers need the underlying comparison. Keep changed populations, common-support exclusions and filter scope visible where they affect interpretation; label fixed reference populations when they do not follow global filters.

### Minimum Analytical Content

Include the headline metrics and relevant comparisons, trends or breakdowns, a concise interpretation, limitations, metric definitions, units, period, source, and freshness. Show uncertainty where material. Provide supporting result tables and reproducible queries or scripts alongside the artifact, with a verification ledger or a link to it. Choose content to serve the question rather than filling a fixed number of cards.

Use the same verified calculations for the dashboard and supporting analysis. Recompute rates from the correct numerator and denominator after filtering; do not average displayed percentages unless that is the defined estimand. Distinguish zero, missing, and undefined values visibly. Do not connect a line across missing periods in a way that implies observed data.

### Reader-Task Review

Alongside numerical and browser checks, use the coverage map to inspect each priority question through the documented interface. Verify that a reader can locate the answer, inspect its supporting comparison, identify the population, denominator and relevant period, understand the main limitation, and reach supporting detail. Record the actual page/section, link path and relevant view/filter state inspected, observed result, failures and corrections in the existing review ledger or coverage map; do not create a duplicate checklist.

Rendering, screenshots, functioning controls and self-reported usability do not establish analytical communication quality. Inspect what the displayed evidence lets a reader conclude. Call this a reviewer walkthrough; claim actual user testing only if users performed the tasks and their observations were recorded. Unperformed task checks remain NOT VERIFIED. Apply proportionately: one chart or table with a brief explanation can fully answer a focused question.

### Artifact Verification and Handoff

- Complete the reader-task review above and record separate numerical/functionality, analytical coverage and presentation judgments. Material presentation gaps block a fully complete delivery claim even if calculations and controls pass.
- Open the delivered artifact using an available browser or the target BI tool. Inspect labels, units, legends, readable layout at the intended screen size, and visible limitations. If render inspection is unavailable, mark it **NOT VERIFIED**.
- Reconcile displayed metrics, chart series, and supporting tables against verified calculations. Check default and representative filtered views, reset behavior, and empty selections when interactions exist.
- Confirm that filtering applies consistently across related cards and charts, preserves grain and denominator definitions, and does not turn undefined values into zero.
- Verify that required assets load and the artifact opens using the documented steps. For app or BI integrations, use the project's existing relevant checks; for local HTML, rendering and calculation/interaction checks are sufficient.
- Deliver a concrete path or link and concise opening instructions. State whether data is a snapshot or refreshes, how to rerun the analysis, and any unresolved verification failures. Hosting or scheduled refresh is part of the work only when requested and supported by available infrastructure.
- Record stakeholder feedback during Feedback. Until it is observed, label it pending rather than claiming acceptance. Distinguish dashboard correctness from any later intervention outcome.

## The Three Core Dashboard Archetypes

| Archetype | Primary Audience | Core Question | Update Cadence | Key Characteristics |
|---|---|---|---|---|
| **Executive / Strategic** | C-Suite, VPs, Board | *"Are we on track to hit our strategic goals?"* | Monthly / Weekly | High-level North Star KPIs, period-over-period targets, minimal filters, uncluttered summary scorecards. |
| **Operational** | Frontline managers, Team leads, Operations | *"Is anything broken right now that requires intervention?"* | Real-time / Hourly / Daily | Live health status, threshold alert banners, exception lists, operational bottlenecks, task-oriented. |
| **Analytical / Exploratory** | Product managers, Functional analysts, Domain leads | *"What segments, trends, or behaviors drive current performance?"* | Daily / Weekly | Interactive dimensional filters, cohort slicing, drill-downs, correlation views, deeper data tables. |

## Information Hierarchy and Visual Layout

Organize views around the questions and comparisons that support the intended use. Lead with the most material finding and its evidence, then expose relevant comparisons and supporting detail. A scorecard may help monitoring; aligned distributions, interval plots, cohort matrices or segment/period comparisons may better explain an investigation. Do not prescribe card counts or reuse a fixed layout irrespective of the data. See [worked examples](./analytical-examples.md) for alternatives.

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
- When useful, allow users to click on high-level chart elements to drill into underlying granular dimensions (e.g., clicking on a regional drop in revenue opens a sub-view filtered to that specific region's product mix).
- Keep initial views simple; hide secondary technical attributes behind click-to-expand details.

### 4. Data Freshness, Latency, and SLAs
- Explicitly display data freshness metadata in the header: *"Data updated as of: 2025-06-15 06:00 UTC (Daily batch sync)"*.
- Document the refresh schedule and underlying source table pipeline SLAs so stakeholders know when numbers are finalized.

### 5. Query Performance and BI Scalability
- **Pre-Aggregated Summary Tables**: Avoid pointing high-traffic executive dashboards directly at raw, billion-row event tables. Have analytics engineers build pre-aggregated, indexed data warehouse summary marts (e.g., via dbt).
- **Visual density**: Include only evidence needed to assess the priority questions. Review analytical value separately from working controls using [the quality rubric](./analytical-quality.md).
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
