# Experimentation and A/B Testing

## Overview
Randomized controlled experiments (A/B tests) are the gold standard for establishing causal relationships between product or business interventions and measurable outcomes. By randomly assigning eligible units to control and treatment variations, experimentation balances both observed and unobserved confounding variables across groups.

## Core Experiment Concepts and Architecture

### 1. The Scientific Hypothesis
A valid experiment hypothesis states the expected intervention, the primary outcome, the proposed causal mechanism, and the target audience:
> *"By [introducing 1-click checkout] to [returning mobile customers], we will increase [completed checkout conversion] because [checkout friction and form entry fatigue are reduced]."*

### 2. Unit of Randomization
- The entity upon which randomization is performed (e.g., `user_id`, `cookie_id`, `cluster_id`, `store_id`, `geographic_market`).
- **Dependence Structure Principle**: The randomization unit determines the dependence structure of the experiment. The unit of randomization does NOT have to equal the unit of analysis, but the analysis must account for the actual randomization and clustering structure:
  - *Randomize by user* $\rightarrow$ Analyze user-level outcomes directly under independent observation assumptions.
  - *Randomize by store or cluster* $\rightarrow$ Customer observations within the same store are correlated; standard errors must be clustered or analyzed at the store aggregate level to prevent severely deflated variance and inflated false positives.
  - *Randomize by region / market* $\rightarrow$ Account for regional dependencies, market-level spillovers, or use synthetic control / market-level aggregations.
- *Default Practice*: Use stable, persistent identifiers (`user_id` when authenticated, persistent device UUID otherwise) to avoid variant contamination across user sessions.

### 3. Metric Architecture for Experiments
- **Primary Metric (OEC - Overall Evaluation Criterion)**: The single metric deciding success (e.g., checkout completion rate). Must be directly sensitive to the treatment.
- **Secondary Metrics**: Diagnostic metrics explaining why the primary moved (e.g., add-to-cart rate, payment error rate).
- **Guardrail Metrics**: Critical business health indicators that must not be degraded (e.g., page latency, refund rates, customer support tickets, gross revenue).

## Pre-Experiment Sizing and Power Analysis
Before launching an experiment, determine the sample size and duration required to detect the expected business impact with statistical reliability.

### Key Sizing Parameters
- **Significance Level ($\alpha$)**: Type I error rate, standardly set to $0.05$ ($5\%$).
- **Statistical Power ($1 - \beta$)**: Probability of detecting a true effect if present, standardly set to $0.80$ ($80\%$) or $0.90$ ($90\%$).
- **Baseline Rate / Variance ($\sigma^2$)**: Historical conversion rate or standard deviation of the metric.
- **Minimum Detectable Effect (MDE)**: The smallest relative or absolute lift that matters practically to the business. Sizing for an unrealistically tiny MDE requires massive sample sizes; sizing for a large MDE leaves real, smaller improvements undetected.
- **Duration Estimation**:
  $$\text{Days Required} = \frac{\text{Required Total Sample Size}}{\text{Daily Eligible Unique Traffic}}$$
- **Duration Heuristics and Constraints**: Experiment duration is context-dependent and cannot be dictated by a universal fixed rule (such as an unconditional "7 to 14 days"). Duration depends on:
  - Required statistical sample size and exposure rates;
  - Outcome maturity and conversion delay (e.g., 30-day repeat purchase vs. immediate click);
  - Day-of-week and intra-month seasonality (covering at least one full weekly cycle is a common heuristic for daily consumer traffic);
  - Novelty and primacy effects requiring time to stabilize;
  - Business cycle volatility and operational risk constraints.

## Threats to Experimental Validity

### 1. Sample Ratio Mismatch (SRM)
- Occurs when the observed ratio of visitors between control and treatment deviates significantly from the planned allocation (e.g., planned 50/50, observed 48/52 across 100,000 visitors).
- **Diagnostic Test**: Always perform a Chi-Square goodness-of-fit test on assignment counts before analyzing outcomes:
  $$\chi^2 = \sum \frac{(\text{Observed} - \text{Expected})^2}{\text{Expected}}$$
- **Diagnostic Signal**: A very small $p$-value (e.g., $p < 0.001$) is a strong diagnostic signal requiring immediate investigation, rather than absolute proof that the underlying treatment effect is invalid. It signals potential flaws such as:
  - Variant redirection latency differences causing dropped sessions;
  - Asymmetric bot filtering or bot detection triggers;
  - Client crashes or runtime exceptions on variant loading;
  - Tracking/instrumentation pipeline failures or dropped exposure logs;
  - Upstream user segmentation or targeting discrepancies.
  *Rule*: Investigate root causes and verify data integrity before trusting downstream metric movements.

### 2. The Peeking Problem and Repeated Testing
- Continuously checking results and stopping the test as soon as nominal $p < 0.05$ inflates Type I decision error. The extent of false positive inflation depends on the number of interim looks, the stopping rule, and the correlation between successive test statistics.
- *Default Practice*: Stick to pre-determined sample sizes and scheduled evaluation dates. If interim monitoring is necessary for early stopping on safety guardrails or high efficacy, employ formal sequential testing methods (e.g., Group Sequential designs or alpha-spending functions) at an awareness level.

### 3. Novelty and Primacy Effects
- **Novelty Effect**: Users interact with a feature simply because it is new, creating an artificial initial spike that decays over time.
- **Primacy Effect**: Users initially resist or perform worse on a redesigned interface due to muscle memory, even if the new design is superior long-term.
- **Mitigation**: Observe metric trends over time; check if effect sizes attenuate or stabilize in week 2 vs. week 1.

### 4. Contamination and Network Interference
- **Contamination**: Users in the control group inadvertently receive treatment exposure (e.g., cross-device usage without unified ID).
- **Network Effects / Interference (SUTVA Violation)**: In two-sided marketplaces (e.g., Uber, Airbnb, DoorDash), treatment drivers or sellers compete with control units for the same shared pool of demand. Use cluster-based randomization, synthetic controls, or switchback (time-based) experiments instead of simple user-level randomization.

## Experiment Decision Framework
Do not reduce ship/no-ship decisions to a simplistic binary rule ($p < 0.05 \rightarrow \text{ship}$, $p \ge 0.05 \rightarrow \text{reject}$). Instead, evaluate decisions through a multi-factor framework:

```text
Estimated Treatment Effect & Point Lift
     ↓
Uncertainty Quantification (Confidence Intervals)
     ↓
Practical & Business Value (Commercial magnitude vs. cost)
     ↓
Implementation, Maintenance, and Technical Costs
     ↓
Guardrail Health & Secondary System Trade-offs
     ↓
Decision Risk & Reversibility (One-Way vs. Two-Way Door)
     ↓
Evidence Quality & SRM Diagnostics
     ↓
Decision: Ship / Iterate / Reject / Gather More Evidence
```

### Action Archetypes
- **Ship**: Clear positive effect estimate with confidence interval bounds exceeding minimum business utility thresholds, neutral/healthy guardrails, acceptable ongoing costs, and verified test integrity.
- **Do Not Ship / Reject**: Clear negative impact on primary outcome, material degradation of guardrail metrics, or ongoing operational costs far exceeding plausible upside.
- **Iterate**: Point estimate is promising but confidence intervals are wide or include negative outcomes; or user feedback reveals interface friction; formulate refined hypotheses.
- **Gather More Evidence**: Sample size was prematurely constrained, high conversion latency remains incomplete, or diagnostic anomalies (such as SRM) must be resolved first.

## Cross-References
- For confidence intervals, hypothesis testing, and statistical power: [Statistics and Statistical Inference](./statistics-and-inference.md)
- For evaluating causal assumptions and quasi-experiments when A/B tests are impossible: [Causal Reasoning](./causal-reasoning.md)
- For metric design, primary vs. guardrail indicators, and ratio definitions: [Metrics and KPIs](./metrics-and-kpis.md)
- For event tracking and telemetry requirements: [Data Sourcing and Collection](./data-collection.md)
