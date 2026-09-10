# Problem Definition and Framing

## The Core Question
Before requesting data, writing queries, or generating visualizations, the analyst must answer:
> **"What decision will this analysis support?"**

If no decision depends on the outcome, the work risks becoming an unfocused data exploration without business utility. Avoid solution-first analysis where a specific tool or conclusion is presupposed before framing the problem.

## The Problem Formulation Chain
Transform vague commercial concerns into quantifiable analytical inquiries using this structured progression:
```text
Business Concern (e.g., "Retention feels weak lately")
     ↓
Decision to be Made (e.g., "Should we invest engineering resources into redesigning user onboarding?")
     ↓
Analytical Question (e.g., "What is the 30-day cohort retention curve by activation milestone, and where do drop-offs concentrate?")
     ↓
Primary Metric & Guardrails (e.g., Day-30 Retention Rate; Guardrail: Support Contact Rate)
     ↓
Required Evidence (e.g., Event telemetry from user signup to Day 30 across the last 6 monthly cohorts)
```

## Business Problem vs. Analytical Problem
- **Business Problem**: A challenge, pain point, or opportunity expressed in organizational or commercial terms (e.g., "Customer churn is increasing," "Marketing CAC feels too high," "Inventory holding costs are excessive").
- **Analytical Problem**: The business problem translated into quantifiable entities, verifiable relationships, and calculable metrics (e.g., "What is the 30-day cohort retention rate across acquisition channels, and which user behaviors correlate with churn?").
- **Translation Imperative**: An analyst never analyzes a raw business problem directly; they translate it into one or more precise analytical inquiries.

## Stakeholder Identification and Decision Alignment
- **Primary Decision-Maker**: The individual accountable for acting on the findings (e.g., VP of Growth, Product Manager, Head of Operations).
- **Influencers and Subject Matter Experts**: Domain operators whose frontline context explains data quirks (e.g., account managers, frontline support agents, software engineers).
- **Consumers of Deliverables**: Operational teams who execute recommendations or rely on scheduled monitoring dashboards.
- **Stakeholder Discovery Inquiries**:
  - What specific business action will change based on positive, negative, or inconclusive findings?
  - What is the cost of being wrong (Type I decision risk vs. Type II decision risk)?
  - What is the deadline for the decision, and what level of precision is required?

## Business Objectives vs. Analytical Objectives
- **Business Objective**: The strategic or financial outcome the organization seeks to achieve (e.g., "Reduce user churn by 2 pp in Q4 to preserve $500K in ARR").
- **Analytical Objective**: The technical, statistical, or evaluative deliverable the analysis produces (e.g., "Quantify the hazard rate of churn over tenure, identify top-k feature correlates with early cancellation, and segment churn risk by plan type").

## Scope, Constraints, and Assumptions
- **In-Scope**: Explicit populations, timeframes, geographic regions, platforms, and metrics under examination.
- **Out-of-Scope**: Explicit boundaries defining what will *not* be investigated in the current iteration to prevent scope creep.
- **Constraints**: Data availability gaps, technical infrastructure limits, latency bounds, regulatory restrictions (e.g., PII minimization), and deadlines.
- **Assumptions**: Explicit domain propositions accepted as true for the purpose of the analysis (e.g., "Historical seasonal patterns from 2024 remain valid in 2025; tracking tag implementations were error-free across all platforms").

## Formulating SMART Analytical Questions
A well-formed analytical question satisfies five SMART criteria:
- **Specific**: Identifies target populations, dimensions, and variables.
- **Measurable**: Evaluated against quantifiable, formulaic metrics.
- **Achievable**: Addressable with available data and within the project timeline.
- **Relevant**: Tied directly to an upcoming business decision or operational intervention.
- **Time-bound**: Evaluates a clearly delineated observation window with a firm completion deadline.

### Examples: Poor vs. Well-Defined Problems

| Poor Problem Definition | Flaw | Well-Defined Analytical Problem |
|---|---|---|
| "Why are sales dropping?" | Vague, undefined timeframe, unspecified product or region, no clear decision. | "Which product lines and regions experienced meaningful month-over-month revenue declines between May and July 2025, and did lower transaction volume or lower average order value drive the reduction?" |
| "Check if marketing is working." | "Working" is undefined; no baseline, attribution logic, or success threshold. | "What was the 30-day return on ad spend (ROAS) and customer acquisition cost (CAC) across Google and Meta paid campaigns for Q2 2025 compared to the organic baseline cohort?" |
| "Analyze user engagement." | Unbounded scope, vanity metric risk, lacks target decision. | "What percentage of free-tier signups in January 2025 performed key action X within 7 days, and how does 90-day conversion to paid compare between cohorts that did vs. did not perform action X?" |

## Success Criteria and Deliverables
- **Success Criteria**: Pre-agreed operational, empirical, and decision criteria that determine when the analysis is complete. Success criteria should focus on decision usefulness, magnitude of effect, uncertainty quantification, practical relevance, and reproducibility—never on achieving $p < 0.05$ alone (e.g., *"Identify the factors most strongly associated with churn, quantify effect sizes and uncertainty, assess business relevance, and clearly document limitations before recommending action to the product lead"*).
- **Deliverables**: Formally agreed artifacts suited to stakeholder needs (e.g., 1-page executive memo, reproducible analytical SQL script/notebook, or interactive BI dashboard).

## Cross-References
- For evidence-based decision frameworks and stakeholder trade-offs: [Data-Driven Business](./data-driven-business.md)
- For defining primary, secondary, and guardrail metrics: [Metrics and KPIs](./metrics-and-kpis.md)
- For situating problem framing in the project lifecycle: [The Analytics Lifecycle](./analytics-lifecycle.md)
- For classifying tasks into descriptive, diagnostic, predictive, or prescriptive types: [Analytics Types and Selection](./analytics-types.md)
