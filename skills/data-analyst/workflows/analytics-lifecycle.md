# Ten-Stage Data Analytics Methodology

## Contents

- [Operational Overview](#operational-overview)
- [Stage 1: Business Understanding](#stage-1-business-understanding)
- [Stage 2: Analytic Approach](#stage-2-analytic-approach)
- [Stage 3: Data Requirements](#stage-3-data-requirements)
- [Stage 4: Data Collection](#stage-4-data-collection)
- [Stage 5: Data Understanding](#stage-5-data-understanding)
- [Stage 6: Data Preparation](#stage-6-data-preparation)
- [Stage 7: Modeling](#stage-7-modeling)
- [Stage 8: Evaluation](#stage-8-evaluation)
- [Stage 9: Deployment](#stage-9-deployment)
- [Stage 10: Feedback](#stage-10-feedback)
- [Verification Model](#verification-model)
- [Non-Linear Feedback Loops](#non-linear-feedback-loops)

## Operational Overview

Follow the ten stages of the John Rollins data analytics methodology: **Business Understanding → Analytic Approach → Data Requirements → Data Collection → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment → Feedback**. The workflow is iterative; the technique references provide methods and the safeguards protect integrity throughout.

Keep reusable skill guidance, the domain-specific project brief, and dataset-specific evidence separate. Preliminary inspection may refine the contract; record revisions rather than implying all criteria existed before inspection.

Scale the work and documentation to the question and decision risk. A focused calculation can address applicable stages briefly and deliver a compact table. Choose a usable report or dashboard for substantial analyses according to the task; default to a dashboard for substantial visual analysis when no format is specified. Mark genuinely unnecessary stages or activities **NOT APPLICABLE** with a reason; missing data or unexecuted checks must remain visible limitations.

Evaluation validates the analysis before delivery. Feedback concerns stakeholder use and real-world outcomes afterward. Modeling includes ordinary analytical queries and statistics; it does not mandate machine learning or expand the skill into production MLOps.

## Stage 1: Business Understanding

### Purpose

Establish the business or informational purpose before selecting tools.

### Activities

1. Identify the stakeholder, intended use, analytical question, deadline, and cost of being wrong.
2. Define scope, population, time window, grain, relevant metrics and formulas, and success criteria. Define guardrails when an intervention is involved.
3. Establish audience and delivery acceptance criteria from the request; label inferred criteria as proposed rather than agreed. Substantial analyses need a useful report/dashboard; focused questions can use a compact result. Respect explicit format constraints.
4. Prioritize evidence-supported questions for open-ended requests. Define what constitutes an adequate answer, including comparison, interpretation and material validation, rather than artifact or chart counts.

### Expected Output

An analysis brief containing the question, purpose, scope, relevant metrics, constraints, and intended artifact.

### Verification Gate

The question and intended use are explicit; relevant metric definitions, grain, period, and acceptance criteria are unambiguous.

### References

- [Problem Definition and Framing](../references/problem-definition.md)
- [Data-Driven Business and Decision-Making](../references/data-driven-business.md)
- [Metrics and KPIs](../references/metrics-and-kpis.md)

## Stage 2: Analytic Approach

### Purpose

Translate the business question into the simplest defensible analytical method.

### Activities

1. Classify the question and select descriptive, diagnostic, predictive, prescriptive, causal, funnel, cohort, or temporal techniques as needed.
2. State the comparisons, assumptions, evidence, and validation needed to distinguish a useful answer from an unsupported claim.
3. Choose methods proportionate to the task. A relational aggregation can be the entire model; do not require machine learning. State a stopping rule tied to question coverage and material uncertainty, not endless exploration.

### Expected Output

A method and evaluation plan, including material assumptions and success criteria.

### Verification Gate

The approach can answer the question with feasible evidence and appropriate analytical validity.

### References

- [Analytics Types and Selection](../references/analytics-types.md)
- [Statistics and Statistical Inference](../references/statistics-and-inference.md)
- [Causal Reasoning](../references/causal-reasoning.md)

## Stage 3: Data Requirements

### Purpose

Specify what evidence is needed before acquiring data.

### Activities

1. Define required fields, units, source grain, keys, join relationships, population, historical coverage, sampling needs, and freshness.
2. Identify authoritative sources, owners, access and privacy constraints, and quality conditions required by the approach.
3. Map each priority question to required and available evidence: answerable, conditionally answerable, or unsupported. Record missing evidence and decide whether collection or a narrower question can resolve the gap.
4. Preserve the original objective when revising scope. Explain supported alternatives and resulting delivery status; an unsupported prediction target need not block useful descriptive work.

### Expected Output

Minimum data requirements and a source/access plan.

### Verification Gate

Required evidence is specified and sourcing is feasible, or gaps explicitly trigger a revised question or approach.

### References

- [Data Sourcing and Collection](../references/data-collection.md)
- [Data Quality](../references/data-quality.md)
- [Data Engineering for Analysts](../references/data-engineering.md)
- [Reproducibility and Data Governance](../references/reproducibility-and-governance.md)

## Stage 4: Data Collection

### Purpose

Acquire traceable inputs that meet the data requirements.

### Activities

1. Extract the minimum relevant data from accessible authoritative sources; an existing supplied dataset may satisfy collection.
2. Preserve raw inputs or point-in-time references and extraction queries; record source versions, timestamps, filters, row counts, and coverage.
3. Compare actual coverage with requirements and document inaccessible sources or unavailable periods. Never fabricate records to fill a gap.

### Expected Output

Traceable raw data or reproducible extraction queries with a provenance and coverage record.

### Verification Gate

Inputs can be traced to their source and requirements; missing coverage is resolved or disclosed before claims depend on it.

### References

- [Data Sourcing and Collection](../references/data-collection.md)
- [Reproducibility and Data Governance](../references/reproducibility-and-governance.md)

## Stage 5: Data Understanding

### Purpose

Assess what the collected data means and whether it supports the approach.

### Activities

1. Inspect schemas, actual records and relevant documentation to establish entities, field meanings, units, keys, cardinality, nulls, categories, ranges, distributions, duplicates, time semantics and freshness. Column names alone do not establish consequential meanings.
2. Investigate unusual values, measurement changes, missingness, sampling constraints, and potential join fanout.
3. Assess fitness for the analytical approach. Return to requirements or collection when evidence is insufficient.

### Expected Output

A data profile, quality assessment, and documented analytical limitations.

### Verification Gate

Data semantics, grain, quality, and limitations are understood well enough to prepare and analyze responsibly.

### References

- [Exploratory Data Analysis (EDA)](../references/eda.md)
- [Data Quality](../references/data-quality.md)
- [SQL for Analysis](../references/sql-for-analysis.md)

## Stage 6: Data Preparation

### Purpose

Produce analysis-ready inputs while preserving transformation transparency.

### Activities

1. Clean, typecast, filter, deduplicate, join, reshape, and derive variables only as needed; preserve the original input.
2. Document exclusions, imputations, and other material changes with affected row counts and justification.
3. Reconcile row counts, key uniqueness, join cardinality, control totals, and relevant denominators; prevent leakage for predictive tasks.

### Expected Output

An analysis-ready dataset or query with its transformation and quality record.

### Verification Gate

Grain, keys, row counts, and control totals reconcile; changes and unresolved quality constraints are explicit.

### References

- [Data Wrangling and Transformation](../references/data-wrangling.md)
- [SQL for Analysis](../references/sql-for-analysis.md)
- [Data Quality](../references/data-quality.md)
- [Reproducibility and Data Governance](../references/reproducibility-and-governance.md)

## Stage 7: Modeling

### Purpose

Execute the chosen analytical approach to answer the question.

### Activities

1. Build descriptive aggregations, metric decompositions, cohort/funnel analyses, statistical comparisons, scenario calculations, or appropriate predictive models.
2. Compare relevant segments and time periods; quantify uncertainty and practical effect size when material; inspect alternative explanations.
3. Preserve calculations and result tables. Create candidate visuals and separate facts, observations, insights, hypotheses, conclusions, recommendations, and limitations.
4. For material initial findings, execute justified follow-up to discriminate plausible alternatives or quantify heterogeneity; record observation → reason for follow-up → executed result → changed interpretation. Distinguish planned analyses from exploratory discoveries and account for multiplicity where material. A proposed follow-up list is not executed investigation.
5. For substantial visual artifacts, read [Dashboards and BI](../references/dashboards-and-bi.md) and [Visualization and storytelling](../references/visualization-and-storytelling.md). Map priority questions → material findings → supporting comparisons → presentation choices → reader-facing locations, retaining consequential follow-up. Maintain this internal review evidence through delivery.
6. Follow [investigation and synthesis](../references/investigation-and-synthesis.md): stop when priority questions are answered or concretely blocked and additional feasible work is unlikely to change the scoped answer. Explain exceptions and blockers.

### Expected Output

Reproducible analytical results, supporting tables, and candidate visuals.

### Verification Gate

The method follows the approach, calculations reproduce, and interpretations remain within the available evidence. Major findings trace question, population/comparison, method, magnitude, limits, interpretation and relevant implication. A substantial investigation cannot pass with profiling alone; justified follow-up is executed or its absence is substantiated. State INSUFFICIENT EVIDENCE for specific unsupported claims, not as a blanket substitute for supported analysis.

### References

- [SQL for Analysis](../references/sql-for-analysis.md)
- [Statistics and Statistical Inference](../references/statistics-and-inference.md)
- [Experimentation and A/B Testing](../references/experimentation.md)
- [Causal Reasoning](../references/causal-reasoning.md)
- [Time-Series Analysis](../references/time-series-analysis.md)
- [Predictive Analysis](../references/predictive-analysis.md)
- [Visualization and Analytical Storytelling](../references/visualization-and-storytelling.md)

## Stage 8: Evaluation

### Purpose

Validate analytical correctness and usefulness before delivery.

### Activities

1. Compare results with the original question, intended use, and predeclared analytical success criteria. Check assumptions, leakage, alternative explanations, and causal language as relevant.
2. Independently recompute decision-critical metrics when practical; reconcile displayed values and candidate visual encodings with verified results.
3. Apply [the analytical quality rubric](../references/analytical-quality.md) separately to technical correctness, analytical adequacy and communication/usability. Check each material question and criterion against specific evidence. Use the coverage map and dashboard reader-task review to inspect answer, comparison, population/denominator/period, limitation and supporting-detail access; record locations and failures. Numerical reconciliation, screenshots and working controls cannot establish communication quality.
4. Return failed checks to the earliest corrective stage and record the correction and rerun evidence. If blocked, limit affected conclusions and explicitly deliver partial analysis, feasibility assessment or unverified work. Do not mark missing work complete by adding caveats.

### Expected Output

A verification ledger and coverage review, limitations, separate numerical/functionality, analytical coverage and presentation judgments, and distinct analysis and delivery readiness decisions.

### Verification Gate

Material claims are supported, calculations reconcile, and all material applicable rubric criteria are adequate or stronger. Critical failures block affected claims. Unresolved material gaps block complete status against the original contract; identify the revised scope and status.

### References

- [Data Quality](../references/data-quality.md)
- [Statistics and Statistical Inference](../references/statistics-and-inference.md)
- [Visualization and Analytical Storytelling](../references/visualization-and-storytelling.md)
- [Reproducibility and Data Governance](../references/reproducibility-and-governance.md)

## Stage 9: Deployment

### Purpose

Make the validated analysis accessible in a usable visual artifact.

### Activities

1. Build the agreed report, dashboard or smaller visual result. Use accessible existing BI/project tooling; otherwise deliver portable HTML for a dashboard.
2. Organize substantial delivery around priority questions and findings supported by relevant comparisons, distributions or trends, definitions and limitations. Keep extended methodology available without letting it replace findings. Choose encodings for the actual analytical relationship; add interactions only when they serve the question.
3. Open and inspect each required artifact; reconcile visible values, exercise applicable filters and empty states, and complete the reader-task walkthrough through the documented interface. For browser delivery, essential evidence must be readable in the dashboard or linked rendered report; raw Markdown/CSV/code downloads do not suffice. Respect explicit alternative formats. Record locations inspected, failures and checks that could not be executed; do not call a reviewer walkthrough actual user testing.
4. Provide the artifact link or path, supporting result tables, queries/scripts, and opening and refresh instructions. Local delivery is sufficient unless hosting is requested. Label snapshots and illustrative prototypes accurately.

### Expected Output

An accessible visual artifact and reproducible analytical handoff.

### Verification Gate

Each required artifact meets its agreed role, renders where applicable, and exposes essential findings and consequential follow-up through inspected reading paths. Applicable interactions work, displayed values reconcile, and access/refresh instructions are clear. Material presentation gaps block complete delivery even when analysis is complete; a strong report cannot offset material dashboard omissions. Unperformed checks remain NOT VERIFIED.

### References

- [Dashboards and Business Intelligence (BI)](../references/dashboards-and-bi.md)
- [Visualization and Analytical Storytelling](../references/visualization-and-storytelling.md)
- [Reproducibility and Data Governance](../references/reproducibility-and-governance.md)

## Stage 10: Feedback

### Purpose

Learn from stakeholder use and assess real-world outcomes when applicable.

### Activities

1. Request or record stakeholder feedback on clarity, usefulness, and missing questions. Do not invent stakeholder acceptance; when feedback is unavailable, record it as pending.
2. For an intervention, compare observed outcomes with the predeclared baseline, target, guardrails, evaluation window, and attribution method. Check implementation fidelity, data integrity, unintended effects, and uncertainty.
3. When outcome data does not yet exist, provide an evaluation plan with baseline, target, guardrails, window, attribution method, owner, and review date; label the outcome PENDING. When no intervention exists, mark outcome evaluation NOT APPLICABLE.
4. Use available evidence to continue, modify, reverse, or investigate the intervention, and route learning to the appropriate earlier stage. Record which feedback changed the question, data requirements, method, analysis or presentation and verify affected work again. A pending plan supports handoff but does not verify an outcome.

### Expected Output

A feedback record and, where relevant, an outcome assessment or pending evaluation plan.

### Verification Gate

Observed outcomes and stakeholder feedback are distinguished from future plans; any pending follow-up has a next step and owner/timing when known.

### References

- [Data-Driven Business and Decision-Making](../references/data-driven-business.md)
- [Metrics and KPIs](../references/metrics-and-kpis.md)
- [Experimentation and A/B Testing](../references/experimentation.md)
- [Causal Reasoning](../references/causal-reasoning.md)
- [Time-Series Analysis](../references/time-series-analysis.md)
- [Dashboards and Business Intelligence (BI)](../references/dashboards-and-bi.md)

## Verification Model

Use three complementary levels of verification:

1. **Stage verification**: Apply each stage gate before moving forward.
2. **Result verification**: Before delivery, confirm that the complete analysis answers the original question, reproduces, reconciles, states uncertainty and limitations, and supports its recommendations.
3. **Outcome verification**: After the decision is implemented, evaluate real-world impact against the baseline, target, guardrails, and attribution plan. If the outcome cannot yet be observed, record **PENDING** and deliver the evaluation plan rather than claiming success. If no intervention exists, record **NOT APPLICABLE**.

### Evidence Standard

Verification requires recorded evidence, not an unchecked assertion that a review occurred.

1. Define the expected condition or tolerance for each material check before assigning a status.
2. Implement mechanically testable checks with task-specific SQL, Python/R, spreadsheet formulas, or equivalent executable tooling whenever the data and environment permit it.
3. Encode the actual analytical contract: source and output grain, key uniqueness, join cardinality, exclusions, metric formulas, denominator population, time windows, reconciliation totals, statistical assumptions, and metric-specific domain invariants.
4. Independently recompute decision-critical metrics when practical and investigate discrepancies before reporting the result.
5. Preserve each material check's method and observed output with the analysis artifacts. Record the actual tested quantity, population, unit and condition; compare ledger entries with code. Derive logged values from checked variables where practical: a response count cannot evidence a unique-user-count condition even when the latter passed.
6. Record each material check as **PASS**, **FAIL**, **NOT VERIFIED**, or **NOT APPLICABLE**. A check passes only when its expected condition was explicitly evaluated and satisfied. Reserve **NOT APPLICABLE** for a check outside the justified scope, not for missing evidence. **PENDING** is a separate outcome-evaluation state, not a verification-check status: an evaluation-plan completeness check may pass while the future outcome remains pending.
7. A failed or unavailable check must either send the analysis back to an earlier stage or appear as a visible limitation that blocks or reduces confidence in the affected conclusion.

For every non-trivial deliverable, include a verification ledger with these fields:

| Check / quantity and population | Expected Condition / Tolerance | Method | Observed value, unit and evidence location | Status | Effect on Confidence |
|---|---|---|---|---|---|
| Material invariant or claim being verified | Explicit condition that constitutes success | Executed query, calculation, formula, or review method | Observed result and location of saved details | PASS, FAIL, NOT VERIFIED, or NOT APPLICABLE | None, bounded caveat, or conclusion blocked |

Preserve contemporaneous gate decisions and corrections when process compliance matters. Headings, boilerplate and artifact existence do not prove stage execution, predeclared criteria or chronological order.

Use task-specific verification code by default. Add a bundled reusable script only after repeated analyses demonstrate the same stable, domain-independent validation pattern.

## Non-Linear Feedback Loops

- **Question and approach**: An unanswerable question or failed assumption requires revisiting Business Understanding or Analytic Approach.
- **Requirements and collection**: Missing fields, coverage, or access require revising requirements, recollecting data, or narrowing scope.
- **Understanding and preparation**: Profiling and transformation checks can reveal new data-quality problems and require rework.
- **Modeling and evaluation**: Contradictory findings, unreconciled calculations, or unsupported claims return the work to the method or data that needs correction.
- **Deployment and feedback**: Rendering defects return to artifact creation; stakeholder questions and observed outcomes can initiate a new analytical cycle.
