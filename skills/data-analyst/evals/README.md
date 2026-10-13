# Data analyst evaluation protocol

Run deterministic safety checks from the repository root:

```sh
python3 -m unittest discover -s skills/data-analyst/evals -v
python3 scripts/validate_skills.py
```

IDs 1–11 are preserved regression prompts. IDs 12–23 add deterministic development inputs covering transaction composition, repeated sequential events, sparse calendars and seasonality, weighted sampling, join fanout, randomized versus observational inference, a substantial open-ended investigation, unsuitable evidence, proportional concise delivery, and stakeholder-triggered revisiting. IDs 24–30 add analytical communication cases described below. Paths in evals.json are relative to the skill directory. Fixtures are synthetic fixed extracts, not real business observations. Do not feed expected_output, expectations, evaluator code or oracle results to a model executing the task.

## Analytical communication cases

These development scenarios exercise delivery judgments and proportional presentation, not a chart-count policy:

| ID | Case | Discriminating review expectation |
|---|---|---|
| 24 | Correct functional dashboard; key findings only in raw Markdown | Numerical/functionality pass does not establish readable browser delivery; flag missing reader-facing comparisons. |
| 25 | Fixed 100% bar template for different comparisons | Preserve appropriate composition bars but choose purposeful evidence for matched changes, timing and sensitivity. |
| 26 | Repeated bars for similar composition questions | Accept appropriate reuse and static delivery; no diversity or interaction quota. |
| 27 | Focused question answered by one table | Accept concise verified change with relevant population and period; no substantial-artifact checklist. |
| 28 | Dashboard plus linked rendered report | Accept sufficient readable coverage and progressive disclosure without embedding every supporting artifact. |
| 29 | Consequential sensitivity hidden in callout | Surface baseline/alternative comparison, changed populations, common-support exclusions and filter scope; a strong report cannot rescue a required dashboard role. |
| 30 | Explicit Markdown-only request | Respect the requested format; do not impose HTML requirements. |

For substantial visual outputs, the grader inspects the internal priority-question → finding → comparison → presentation → location map against the brief and actual findings. Do not accept a map that silently drops consequential follow-up. Walk each priority task through the documented interface: locate the answer, inspect the comparison, identify population/denominator/period, understand the main limitation and reach detail. Record locations, view/filter states, observed failures and corrections. Assess each required artifact against its own role and record analysis completion separately from delivery completion. Rendering, screenshots and working filters are useful functional evidence but cannot substitute for this review. A reviewer walkthrough is not actual user testing.

Cases 24, 26, 28 and 29 supply described delivery/review packets rather than executable browser fixtures. Grade the response's judgment against the supplied evidence and whether it distinguishes that evidence from direct inspection. Case 25 is a presentation-design review; cases 27 and 30 produce focused answers. These cases test review behavior and format restraint, not end-to-end dashboard construction or browser usability. For behavioral evaluation of generated substantial artifacts, also run cases 9 or 18 and inspect the actual outputs with the coverage and task protocol above.

## Comparable model runs

1. Before editing, preserve the baseline skill outside the working skill folder. Freeze the revised skill, task inputs and grading rubric before evaluation. Select the same task IDs and input bytes for each condition. Use `fixtures/development/rich-prompt.txt`, transactions.csv and its dictionary for a substantial investigation pair; this prompt deliberately does not enumerate the hidden mix effect.
2. Use a fresh agent/context per task and condition, with either the baseline skill or revised skill and the same prompt/input files. No cross-run conversation, answers, ledgers or evaluator feedback. Optional no-skill runs are an additional condition, not a substitute for the original-skill baseline.
3. Match model/version, reasoning setting, tool access, environment, timeout, maximum output tokens and total work budget. A practical initial budget is 12,000 output tokens and 10 minutes per run, identical across arms; record actual chosen settings before running. Capture total tokens, elapsed time, tool/runtime availability and any interruption. A single pair is a smoke test, never a reliable improvement estimate.
4. Prefer at least three independent repetitions per condition per selected case when resources permit. Blind condition labels and randomize review order. Preserve every output, trace, query/script and artifact under a new workspace iteration; do not overwrite existing runs. Report mean and spread per axis, paired differences, failures and resource cost rather than an overall pass-rate alone. Label any unavailable model run as NOT RUN.
5. Keep `held-out/` unopened by the skill author and model runner until the skill and rubric are frozen. Only an independent grader reads its expected results after outputs exist. Held-out prompts are separate from development evals.json, so local development does not accidentally preload their answers. Do not tune the skill on held-out failures; report them and reserve a fresh set for the next claimed generalization test. File separation is a procedural boundary, not access-control enforcement.

## Three separate scoring axes

Use the independent analytical-quality rubric in `../references/analytical-quality.md` for substantive review. Record the axes separately; no averaging away a serious failure.

- **Technical correctness and functionality (0–3):** use the rubric's grain/semantics, preparation, validity, reproducibility and functionality criteria. Recompute critical quantities and inspect actual evidence.
- **Analytical quality and completeness (0–3):** use objective alignment, question feasibility, method, depth/follow-up, uncertainty/alternatives, usefulness and honest-scope criteria. A concise calculation can be strong without a hypothesis tree; a substantial investigation cannot pass with profiling alone.
- **Communication and usability (0–3):** use visual analytical value and synthesis/accessibility criteria. Inspect actual reader-facing coverage and task evidence, including consequential follow-up. Check readable delivery in the required format; raw Markdown links do not satisfy browser delivery. Accept purposeful repeated charts, static visuals and concise answers when appropriate.

Use the rubric's shared anchors: 0 missing/misleading, 1 superficial, 2 adequate, 3 strong. Record per-criterion evidence and separate dimension decisions, with applicable minima. No material criterion below 2 or critical failure permits complete delivery. Record lifecycle compliance separately from artifact quality; a final report alone cannot establish chronological execution or predeclared criteria.

A filled ledger, exact rubric vocabulary, ten stage headings, numerous charts or correct aggregates alone cannot earn an analytical-depth pass. Review supplied scripts/results, report claims and delivered artifact together. Include negative controls: a heading-rich generic report, a shallow report with correct totals, and a ledger claiming PASS where actual violates expected. The first two may satisfy some structure/numerical checks but fail substantive review; the third must fail integrity.

## Deterministic evaluator boundary

`evaluate.py` recomputes factual oracles from development CSVs. For an optional normalized result submission, save a JSON object with `facts` and `ledger`; each ledger entry includes `fact`, `expected`, `actual`, `condition`, `status`, `method` and `evidence`. `test_evaluators.py` contains a minimal example. Run:

```sh
python3 skills/data-analyst/evals/evaluate.py submission.json --required orders.revenue orders.aov
```

An independent grader can extract this normalized JSON from the report without forcing the analyst to produce evaluator-specific output. Preserve original output and note extraction ambiguity; do not repair missing evidence during extraction. Expected values must match independently computed oracles; actual values must match both condition and reported quantity. Check names and declared PASS are insufficient. Bounds cannot weaken exact-value requirements. Non-finite quantities, duplicate checks and absent evidence are rejected. Evidence locators and method strings are only consistency checks: the independent reviewer must open the evidence, rerun calculations and inspect artifacts before awarding verification integrity. The script always returns `overall_pass: null` and `analytical_quality: REQUIRES INDEPENDENT REVIEW`, including for a numerically correct shallow answer. It does not pretend to grade prose or infer execution from a declaration.

The unittest suite exercises known correct calculations and intentionally weak/misleading submissions. Passing these tests validates evaluator behavior, not that the revised skill improves model outputs. Record deterministic test results separately from actual baseline/revised model comparisons.

## Validation status for the readable-delivery revision

Deterministic validation: `python3 scripts/validate_skills.py` reported **0 issues**, `python3 -m unittest discover -s skills/data-analyst/evals -v` passed **10 tests**, and `git diff --check` passed.

Behavioral baseline/revised comparisons: **NOT RUN**. Cases 24–30 are added evaluation scenarios, not observed agent successes. Repository validation checks their schema, IDs and file references; deterministic evaluator tests check numerical and ledger behavior. Neither establishes improved analytical communication. Direct browser walkthroughs and actual user testing of generated outputs were not performed for this revision.

The held-out case prompts were opened during repository inspection before this revision was frozen; their expected-results file was not opened. They cannot support an uncontaminated held-out claim for this authoring session. Preserve them unchanged, and reserve fresh unseen cases for any future claimed generalization test.
