# Task-scaled analytical quality rubric

Use at contract definition and before delivery for substantial work; apply only relevant criteria to focused calculations. Record evidence locations, score, rationale and corrective work for applicable criteria. The evaluator should inspect calculations, results, visuals and available traces, not accept the generating agent's self-assessment. In comparative evaluation, use an independent reviewer blind to variants where practical.

## Scope and anchors

Scores are **0 missing or misleading**, **1 superficial**, **2 adequate**, **3 strong**. NOT APPLICABLE requires a task-based reason and is excluded from scoring, never used for unavailable evidence. A review can mark an item not verifiable without assuming it failed in the original execution; this cannot support a verified completion claim.

For a narrow calculation, adequacy can be a correct result with relevant population, formula, units and a brief independent check. Follow-up, inference, a separate visualization or stakeholder feedback may be outside scope. A substantial investigation requires objective coverage, evidence-backed interpretation, justified depth and usable delivery. A comprehensive feasibility assessment can pass its own contract, but cannot be scored as a completed broader analysis.

### 1. Technical correctness and functionality

| Criterion | 0: Missing/misleading | 1: Superficial | 2: Adequate | 3: Strong |
|---|---|---|---|---|
| Entities, grain and semantics | Materially wrong population, units, denominator or join | Lists fields without validating consequential meanings | Records/documentation support entities, keys, grain, relationships, units and time; valid populations/joins | Reconciles ambiguous or changing semantics and demonstrates their effect on conclusions |
| Quality and preparation | Silent material changes or corrupted inputs | Null/count inventory without consequences | Relevant quality/selection checks; reproducible changes with affected populations and reconciliations | Tests whether consequential preparation alternatives change findings and resolves anomalies |
| Numerical/statistical validity | Wrong calculations, leakage or invalid inference | Unchallenged calculations and nominal tests | Verified metrics; appropriate assumptions, baselines, uncertainty and study-design constraints | Independent recomputation and targeted robustness checks substantiate critical claims |
| Evidence and reproducibility | Fabricated or false verification | Code/artifact exists but claims cannot be traced | Sources, transformations, code, results and check evidence link to material claims | Another analyst can rerun critical results and reconcile the ledger to code and observed quantities |
| Artifact functionality | Required delivery inaccessible/broken or false render claim | Existence only; interactions unchecked | Agreed artifact usable; displayed values/filters reconcile, unavailable inspection disclosed | Representative and edge views inspected; access, readability and refresh behavior substantiated |

### 2. Analytical quality and completeness

| Criterion | 0: Missing/misleading | 1: Superficial | 2: Adequate | 3: Strong |
|---|---|---|---|---|
| Objective and audience alignment | Answers a different objective silently | Generic questions and inventory | Prioritized questions and acceptance criteria fit intended use; supplied/inferred requirements distinguished | Trade-offs and evolving scope explicitly preserve the intended purpose |
| Questions and feasibility | Promises unsupported answers | Lists questions without mapping evidence | Answerable/conditional/unsupported questions mapped to required data; useful revisions disclosed | Prioritization considers materiality and resolving power; unsupported aims do not prevent supported work |
| Method selection | Method cannot support claim | Default summaries/model without rationale | Simplest valid comparison/method answers each question with assumptions | Competing approaches/baselines evaluated where they can alter interpretation |
| Depth and follow-up | No investigation of material questions | Counts/means or unexecuted follow-up list only | Executes relevant comparisons and justified follow-up on material findings, or substantiates why no follow-up is needed | Resolves consequential alternatives, explains heterogeneity/mechanisms only as supported, and uses a reasoned stopping rule |
| Uncertainty, bias and alternatives | Unsupported causal claim or false precision | Generic caveats detached from findings | Material uncertainty, selection/confounding/design limits and sensitivity tied to claims | Targeted challenges show which interpretations survive and what would change them |
| Interpretation and usefulness | Unsupported conclusions/recommendations | Restates numbers without meaning | Explains magnitude, comparison and relevance; implications fit request and limits | Prioritizes what matters and distinguishes robust conclusions from unresolved alternatives |
| Honest scope and completion | Claims completed/verified without evidence | Lifecycle headings and boilerplate assurance | Material questions accounted for; failures corrected or status explicitly partial/feasibility/unverified | Evidence-backed gate review and feedback revisits explain remaining boundaries without overstatement |

### 3. Communication and usability

| Criterion | 0: Missing/misleading | 1: Superficial | 2: Adequate | 3: Strong |
|---|---|---|---|---|
| Visual analytical value | Distorts evidence, masks populations or hides a changed interpretation | Template-driven charts or dense callouts obscure materially different comparisons | Purposeful charts/tables/prose expose needed comparisons, including consequential follow-up; units, population, denominators, period, sources, exclusions, filter scope and material uncertainty clear | Inspected reader tasks show readers can assess alternatives and sensitivity with aligned evidence and clear annotations |
| Synthesis and accessibility | Essential findings absent or inaccessible in required format | Findings exist only in supporting downloads or reading paths are uninspected | Coverage map links priority questions/findings/comparisons to readable locations; reader-task walkthrough records answer, evidence, population/denominator/period, limitation and detail access | Clear prioritization and inspected reading paths support the full scoped investigation through progressive disclosure without padding |

## Decision rules

Before evaluating, declare which criteria are material and what counts as adequate for this task. Record separate dimension results and case-level weaknesses; do not combine them into a single score that hides analytical failures. Suggested reporting is each dimension's applicable scores and minimum, plus coverage and critical failures. Scores are review aids, not calibrated universal measurements.

Record numerical correctness/functionality, analytical coverage and reader-facing presentation separately, with distinct analysis and delivery completion judgments. For substantial visual work, inspect the [coverage map and reader tasks](./dashboards-and-bi.md) and record interface locations and failures. Screenshots, functioning filters or self-assessment alone do not establish communication quality; do not claim actual user testing from a reviewer walkthrough. Browser delivery requires readable essential evidence in the dashboard or linked rendered report; raw Markdown and CSV remain supporting downloads. If both report and dashboard are required, assess each against its agreed role; report quality cannot offset material dashboard omissions.

Complete delivery requires each material applicable criterion to be at least adequate (2), the task's explicit requirements met, and no unresolved critical failure. When a non-material criterion is below adequate, disclose the bounded limitation and why it does not affect the intended use. A missing required render inspection prevents a claim of fully verified artifact delivery even if the analysis itself is valid. Feedback or intervention outcomes can remain pending without blocking a correctly scoped analytical handoff.

Critical failures include fabricated data/evidence, materially incorrect populations or denominators, invalid joins that alter conclusions, material temporal/target leakage, unsupported causal claims, and false verification/completion claims. Apply them where relevant: a task without joins cannot fail a join check. Do not average critical failures away. Correct and re-evaluate affected work or remove/block the affected claim and explicitly limit delivery.

Material presentation gaps block fully complete delivery even when the underlying analysis is complete. Appropriate reuse of one chart type, a single static chart/table for a focused answer, or an explicitly requested Markdown-only report can be fully adequate; do not reward diversity or require HTML outside the delivery contract.

A technically functioning but analytically shallow substantial output fails the depth/coverage criteria even if all totals reconcile. Lifecycle terms, chart counts, page counts and model complexity earn no credit. Heading-only evidence cannot establish execution order, predeclared criteria or feedback use. Require an execution trace or contemporaneous record for such process claims; artifacts may support result quality without proving chronology.

## Minimal review record

For each material criterion: scope/reason, score or NOT APPLICABLE, specific evidence location and observed result, consequence, and correction/remaining gap. Also record question coverage (answered, partial, unsupported), critical failures, dimension decisions, separate analysis and delivery status and any pending feedback/outcomes. Use a compact equivalent for simple requests; do not append an extensive rubric to a three-number answer.
