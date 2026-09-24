# The Five-Phase Analytics Lifecycle

## Operational Overview

Use this lifecycle to move from an ambiguous business concern to a verified analytical result and an evaluated decision outcome. The five phases provide the workflow; the other reference modules provide techniques and safeguards used within that workflow.

```text
Define the Problem
        ↓
Collect & Preprocess Data
        ↓
Analyze Data & Identify Insights
        ↓
Share Results
        ↓
Evaluate Outcomes
        ↺
   Iterate as needed
```

Treat the workflow as iterative rather than as a one-way pipeline. Scale its depth to the task and decision risk. Execute every applicable phase; when a focused request legitimately does not involve an intervention or outcome assessment, mark that phase **NOT APPLICABLE** with a brief reason. A failed gate sends the work back to the earliest phase that can correct the problem.

## Phase 1: Define the Problem

### Purpose

Narrow the decision space or informational purpose and establish the evidence needed for a useful answer.

### Activities

1. Identify the business concern, stakeholder, decision or informational purpose, relevant deadline, and cost of being wrong.
2. Translate the concern into one or more precise analytical questions.
3. Classify each question as descriptive, diagnostic, predictive, prescriptive, causal, funnel, cohort, or temporal.
4. Define the target population, observation window, unit of analysis, and output grain.
5. Define the primary metric and its formula, grain, and interpretation when a metric is needed; specify a numerator and denominator for rates or ratios. Define guardrails and success thresholds when an intervention or decision requires them.
6. Record scope, constraints, assumptions, required evidence, and expected deliverable.

### References

- [Problem Definition and Framing](./problem-definition.md)
- [Data-Driven Business and Decision-Making](./data-driven-business.md)
- [Analytics Types and Selection](./analytics-types.md)
- [Metrics and KPIs](./metrics-and-kpis.md)

### Expected Output

Produce an analysis brief containing the decision or informational purpose, analytical question, stakeholders, relevant metric definitions, scope, required data, and intended deliverable. Include success criteria when the analysis supports a decision or intervention.

### Verification Gate

- The analytical question is answerable and its decision or informational purpose is explicit.
- When a metric is needed, its formula, eligible population, time window, and grain are unambiguous.
- When the analysis supports a decision or intervention, success and failure can be evaluated with observable evidence.
- Assumptions, constraints, and out-of-scope areas are recorded.

## Phase 2: Collect and Preprocess Data

### Purpose

Create a trustworthy, analysis-ready dataset while preserving provenance and transformation transparency.

### Activities

1. Identify the minimum authoritative internal and external sources needed to answer the question.
2. Record source ownership, extraction time, table or file version, permissions, and PII constraints.
3. Profile schemas, row counts, keys, cardinality, nulls, ranges, categories, duplicates, and freshness.
4. Define the grain of every source and intended analytical output before joining data.
5. Clean, typecast, filter, deduplicate, join, reshape, and derive variables without silently altering observations.
6. Reconcile row counts and key metrics before and after every material transformation.
7. Preserve the extraction query or code and document all exclusions, imputations, and unresolved quality issues.

### References

- [Data Sourcing and Collection](./data-collection.md)
- [Data Quality](./data-quality.md)
- [Data Wrangling and Transformation](./data-wrangling.md)
- [SQL for Analysis](./sql-for-analysis.md)
- [Data Engineering for Analysts](./data-engineering.md)
- [Reproducibility and Data Governance](./reproducibility-and-governance.md)

### Expected Output

Produce an analysis-ready dataset or reproducible query together with a data-quality summary and transformation record.

### Verification Gate

- Every source and transformation is traceable.
- Grain and keys are explicit, and joins do not introduce unintended fanout.
- Row counts and control totals reconcile within documented expectations.
- Required fields meet acceptable completeness, validity, uniqueness, consistency, accuracy, and freshness thresholds.
- Unresolved quality problems and their consequences are disclosed.

## Phase 3: Analyze Data and Identify Insights

### Purpose

Answer the analytical question with the simplest method that produces defensible evidence.

### Activities

1. Establish descriptive baselines and inspect distributions before relying on averages or models.
2. Compare relevant segments, cohorts, time periods, and reference groups.
3. Select specialized methods only when required by the analytical question.
4. Quantify uncertainty and practical effect size where sampling or estimation is involved.
5. Test alternative explanations, inspect confounding, and avoid converting correlation into causation.
6. Separate facts, observations, insights, hypotheses, conclusions, recommendations, and limitations.
7. Reproduce material calculations and reconcile headline results against source totals or an independent formulation.

### References

- [Exploratory Data Analysis](./eda.md)
- [Statistics and Statistical Inference](./statistics-and-inference.md)
- [Experimentation and A/B Testing](./experimentation.md)
- [Causal Reasoning](./causal-reasoning.md)
- [Time-Series Analysis](./time-series-analysis.md)
- [Predictive Analysis](./predictive-analysis.md)
- [SQL for Analysis](./sql-for-analysis.md)

### Expected Output

Produce reproducible findings with supporting calculations, uncertainty, tested alternatives, and limitations. If the available evidence cannot answer the question reliably, report **INSUFFICIENT EVIDENCE**, explain why, and specify the evidence needed to proceed.

### Verification Gate

- The selected technique matches the question, data, assumptions, and decision stakes.
- Material calculations reproduce and reconcile.
- Uncertainty and effect size are reported where they affect the decision.
- Alternative explanations and contradictory evidence were considered.
- Conclusions do not exceed the evidence, and causal language has a defensible identification strategy.

## Phase 4: Share Results

### Purpose

Translate verified analysis into a clear, decision-ready explanation for the intended stakeholders.

### Activities

1. Lead with the answer, or state that the evidence is insufficient to answer reliably.
2. Present only the evidence needed to understand and assess the conclusion.
3. Choose visualizations that accurately encode the relevant comparison, trend, distribution, or relationship.
4. State assumptions, uncertainty, limitations, trade-offs, and unresolved questions visibly.
5. When supported and within scope, specify recommended actions, owners, expected impact, guardrails, and the conditions that would change the recommendation.
6. Preserve links to the queries, code, definitions, and source data needed for auditability.

### References

- [Visualization and Analytical Storytelling](./visualization-and-storytelling.md)
- [Dashboards and BI](./dashboards-and-bi.md)
- [Data-Driven Business and Decision-Making](./data-driven-business.md)
- [Reproducibility and Data Governance](./reproducibility-and-governance.md)

### Expected Output

Produce a stakeholder-appropriate report, memo, dashboard, or presentation containing the answer or insufficient-evidence finding, supporting evidence, limitations, and any warranted recommendation or next action.

### Verification Gate

- The deliverable directly answers the original analytical question.
- Every material claim and recommendation is traceable to verified evidence.
- Charts preserve visual integrity and do not conceal uncertainty or scale.
- Facts, hypotheses, and recommendations remain distinguishable.
- Limitations are visible, and any next decision or action is explicit when one is relevant. For an informational request, state that no action was requested when appropriate.

## Phase 5: Evaluate Outcomes

### Purpose

When a decision or intervention exists, determine whether its outcome met the predeclared success criteria and convert the result into learning for the next cycle.

### Activities

1. Restate the implemented decision, implementation date, affected population, baseline, target, guardrails, and evaluation window.
2. Confirm implementation fidelity and post-decision data quality before interpreting movement.
3. Compare observed results with the predeclared success criteria and relevant counterfactual or baseline.
4. Use randomized or quasi-experimental methods when the question is whether the decision caused the outcome.
5. Inspect unintended effects, distributional impacts, operational trade-offs, and stakeholder feedback.
6. Decide whether to continue, scale, modify, reverse, or investigate the intervention.
7. Feed new evidence into the phase that needs revision.

### References

- [Metrics and KPIs](./metrics-and-kpis.md)
- [Experimentation and A/B Testing](./experimentation.md)
- [Causal Reasoning](./causal-reasoning.md)
- [Time-Series Analysis](./time-series-analysis.md)
- [Dashboards and BI](./dashboards-and-bi.md)
- [Reproducibility and Data Governance](./reproducibility-and-governance.md)

### Expected Output

When post-decision evidence exists, produce an outcome assessment with a continue, scale, modify, reverse, or investigate decision. When a decision is planned but evidence does not yet exist, produce an evaluation plan specifying the baseline, target, guardrails, evaluation window, attribution method, owner, and review date, and label outcome verification **PENDING**. When the work supports no intervention, mark the phase **NOT APPLICABLE**.

### Verification Gate

- A completed outcome is compared against predeclared success criteria rather than a convenient post-hoc target.
- Implementation and measurement integrity are checked before attributing effects.
- Causal claims use an appropriate identification strategy.
- Unintended effects and guardrail movements are included.
- A future evaluation remains **PENDING** until evidence is observed; its next action, owner, and timing are explicit.
- A **NOT APPLICABLE** status explains why the analytical request has no decision outcome to evaluate.

## Verification Model

Use three complementary levels of verification:

1. **Phase verification**: Apply each phase gate before moving forward.
2. **Result verification**: Before delivery, confirm that the complete analysis answers the original question, reproduces, reconciles, states uncertainty and limitations, and supports its recommendations.
3. **Outcome verification**: After the decision is implemented, evaluate real-world impact against the baseline, target, guardrails, and attribution plan. If the outcome cannot yet be observed, record **PENDING** and deliver the evaluation plan rather than claiming success. If no intervention exists, record **NOT APPLICABLE**.

### Evidence Standard

Verification requires recorded evidence, not an unchecked assertion that a review occurred.

1. Define the expected condition or tolerance for each material check before assigning a status.
2. Implement mechanically testable checks with task-specific SQL, Python/R, spreadsheet formulas, or equivalent executable tooling whenever the data and environment permit it.
3. Encode the actual analytical contract: source and output grain, key uniqueness, join cardinality, exclusions, metric formulas, denominator population, time windows, reconciliation totals, statistical assumptions, and metric-specific domain invariants.
4. Independently recompute decision-critical metrics when practical and investigate discrepancies before reporting the result.
5. Preserve each material check's method and observed output with the analysis artifacts.
6. Record each material check as **PASS**, **FAIL**, **NOT VERIFIED**, or **NOT APPLICABLE**. A check passes only when its expected condition was explicitly evaluated and satisfied. Reserve **NOT APPLICABLE** for a check outside the justified scope, not for missing evidence. **PENDING** is a separate outcome-evaluation state, not a verification-check status: an evaluation-plan completeness check may pass while the future outcome remains pending.
7. A failed or unavailable check must either send the analysis back to an earlier phase or appear as a visible limitation that blocks or reduces confidence in the affected conclusion.

For every non-trivial deliverable, include a verification ledger with these fields:

| Check | Expected Condition / Tolerance | Method | Evidence | Status | Effect on Confidence |
|---|---|---|---|---|---|
| Material invariant or claim being verified | Explicit condition that constitutes success | Executed query, calculation, formula, or review method | Observed result and location of saved details | PASS, FAIL, NOT VERIFIED, or NOT APPLICABLE | None, bounded caveat, or conclusion blocked |

Use task-specific verification code by default. Add a bundled reusable script only after repeated analyses demonstrate the same stable, domain-independent validation pattern.

## Non-Linear Feedback Loops

- **Question loop**: Missing or unsuitable evidence requires narrowing or revising the analytical question.
- **Data-quality loop**: Missing tracking, corrupted fields, schema drift, or unresolvable fanout requires revisiting collection and preprocessing.
- **Analysis loop**: Contradictory findings or failed assumptions require a different comparison, method, or metric definition.
- **Communication loop**: Stakeholder questions that expose unsupported claims require returning to analysis rather than polishing the narrative.
- **Outcome loop**: Unexpected post-decision results become evidence for a new problem definition and another lifecycle iteration.

## Cross-References

- For translating commercial ambiguity into analytical questions: [Problem Definition and Framing](./problem-definition.md)
- For choosing analytical types and techniques: [Analytics Types and Selection](./analytics-types.md)
- For data quality profiling and validation: [Data Quality](./data-quality.md)
- For reproducible documentation standards: [Reproducibility and Data Governance](./reproducibility-and-governance.md)
