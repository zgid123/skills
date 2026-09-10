# Causal Reasoning

## Overview
Causal reasoning addresses the fundamental question: *"Did intervention $X$ cause outcome $Y$?"* In observational business data, correlation is ubiquitous, but establishing causality requires a defensible identification strategy, transparent assumptions, and supporting evidence. The analyst must recognize when causal claims are warranted and guard stakeholders against attributing business shifts to coincidental correlations.

## Core Causal Concepts and Terminology

### The Potential Outcomes Framework (Rubin Causal Model)
- **Counterfactual**: What would have happened to the exact same subject if they had received the opposite treatment?
  - For user $i$, let $Y_i(1)$ be the outcome if treated, and $Y_i(0)$ be the outcome if untreated.
  - **Fundamental Problem of Causal Inference**: For any individual user, we can only observe one outcome: $Y_i(1)$ or $Y_i(0)$, never both simultaneously.
- **Average Treatment Effect (ATE)**:
  $$\text{ATE} = \mathbb{E}[Y(1) - Y(0)]$$

### Directed Acyclic Graphs (DAGs) and Causal Structures
DAGs visually map causal assumptions using nodes (variables) and directed edges (causal arrows):
- **Confounder (Common Cause)**: Variable $Z$ causes both Treatment $X$ and Outcome $Y$ ($X \leftarrow Z \rightarrow Y$). If unadjusted, $Z$ introduces spurious correlation. *Example: Marketing budget ($Z$) causes both higher ad impressions ($X$) and higher organic customer acquisition ($Y$).*
- **Collider**: Variable $C$ is caused by both $X$ and $Y$ ($X \rightarrow C \leftarrow Y$). Conditioning or filtering on a collider creates artificial, non-causal association between $X$ and $Y$. *Example: Conditioning only on users who contacted customer support.*
- **Mediator**: Variable $M$ lies along the causal chain ($X \rightarrow M \rightarrow Y$). Controlling for a mediator blocks part of the causal mechanism you intend to measure.

### Key Threats to Causal Identification
- **Selection Bias**: Systematic differences in baseline characteristics between individuals who choose to use a feature and those who do not (e.g., highly engaged power users voluntarily adopt a new dashboard feature; comparing their retention to non-adopters measures user motivation, not feature impact).
- **Reverse Causality**: The outcome actually causes the treatment, rather than vice-versa (e.g., do high-spending customers join the loyalty program, or does the loyalty program cause customers to spend more?).
- **Omitted Variable Bias**: Failure to control for an unobserved common driver distorting the relationship.

## Causal Identification Strategies at Analyst Depth

When randomized experiments are impossible, unethical, or prohibitively expensive, analysts leverage quasi-experimental identification strategies. Each strategy relies on specific, falsifiable assumptions:

### 1. Randomized Controlled Trials (RCTs)
- **Identification Mechanism**: Random assignment guarantees that treatment and control groups have identical distributions of both observed and unobserved characteristics in expectation.
- **Assumptions**: Proper random allocation, no non-compliance, no sample ratio mismatch, stable unit treatment value assumption (SUTVA / no spillover interference).

### 2. Difference-in-Differences (DiD)
- **Concept**: Compares the change in outcomes over time between a treated group and an untreated comparison group:
  $$\text{DiD} = (\bar{Y}_{\text{treat, post}} - \bar{Y}_{\text{treat, pre}}) - (\bar{Y}_{\text{control, post}} - \bar{Y}_{\text{control, pre}})$$
- **Core Assumption: Parallel Trends**: In the absence of treatment, the average outcome of the treatment group would have followed the same trajectory as the control group.
- **Plausibility Check**: Pre-treatment trends can provide evidence about the plausibility of the parallel-trends assumption, but cannot prove it for the unobserved post-treatment counterfactual. Always inspect pre-period alignment while checking for concurrent events that might have affected only one group.

### 3. Regression Adjustment (Multivariate Conditioning)
- **Concept**: Statistically controlling for observed confounders in a regression model to estimate the partial effect of treatment holding other factors constant.
- **Core Assumption: Conditional Independence (Selection on Observables)**: All confounding variables influencing both treatment and outcome are accurately measured and included in the model. If key drivers (e.g., user intent, brand affinity) are unmeasured, estimates remain biased.

### 4. Matching Methods (Propensity Score Matching)
- **Concept**: Pairs each treated unit with one or more untreated units having nearly identical observable characteristics or estimated treatment probabilities (propensity scores).
- **Application**: Balances observable covariates across cohorts; subject to the same omitted variable bias as regression adjustment if unmeasured confounders exist.

### 5. Regression Discontinuity Design (RDD)
- **Concept**: Exploits an arbitrary, strict numerical threshold determining treatment assignment (e.g., credit approved only if credit score $\ge 680$; VIP status granted at exactly 10 orders).
- **Intuition**: Units immediately above and immediately below the threshold are virtually identical except for receiving the treatment.
- **Core Assumption**: Units cannot precisely manipulate their score to cross the threshold.

### 6. Instrumental Variables (IV)
- **Concept**: Uses an exogenous source of variation (an instrument $Z$) that influences treatment assignment $X$ but affects outcome $Y$ solely through its impact on $X$.
- **Core Assumptions (Analyst-Level Awareness)**:
  1. **Relevance**: The instrument $Z$ is strongly correlated with treatment take-up $X$ (not a weak instrument).
  2. **Exogeneity / Independence**: The instrument $Z$ is as good as randomly assigned, independent of all unobserved confounders.
  3. **Exclusion Restriction**: $Z$ affects outcome $Y$ *only* through $X$ and through no direct alternative pathway.
  4. **Monotonicity**: The instrument affects treatment uptake in a single direction (there are no "defiers" who do the opposite of assignment); under monotonicity, IV estimates the Local Average Treatment Effect (LATE) on compliers.
- **Application**: Useful in product rollouts with imperfect compliance (e.g., randomized discount coupon acts as an instrument for purchase behavior).

## Causal Decision Rules for Analysts
- **Avoid Over-Claiming**: Never use causal verbs ("drives", "causes", "boosts", "increases") in reporting unless backed by randomized experiments or validated quasi-experimental identification. Use associational language ("is associated with", "correlates with", "higher among") for observational patterns.
- **Formulate Alternative Explanations**: When observing a strong correlation between a feature and positive retention, actively brainstorm plausible confounding explanations before reporting.
- **Validate Counterfactual Plausibility**: Always ask: *"What comparison, counterfactual, or identification strategy supports the causal claim?"* Evidence supports claims; it rarely "proves" them unconditionally.

## Cross-References
- For designing and analyzing randomized experiments: [Experimentation and A/B Testing](./experimentation.md)
- For inferential statistical tests, confidence intervals, and effect sizes: [Statistics and Statistical Inference](./statistics-and-inference.md)
- For root cause investigation protocols and hypothesis trees: [Exploratory Data Analysis (EDA)](./eda.md)
- For framing decision stakes and business context: [Problem Definition and Framing](./problem-definition.md)
