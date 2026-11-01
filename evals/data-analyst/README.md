# Data analyst evaluation protocol

The bundled analysis helpers and their focused regression tests require `numpy`, `pandas`, and `matplotlib`; the dashboard renderer tests also require Node.js. Install those Python packages in the evaluation environment, then run from the repository root:

```sh
python3 -m unittest discover -s evals/data-analyst -v
python3 scripts/validate_skills.py
git diff --check
```

The development suite includes the factual evaluator, helper regressions, and dashboard-template renderer checks. These deterministic tests do not establish model behavior.

IDs 1–11 are preserved regression prompts. IDs 12–23 add deterministic development inputs covering transaction composition, repeated sequential events, sparse calendars and seasonality, weighted sampling, join fanout, randomized versus observational inference, a substantial open-ended investigation, unsuitable evidence, proportional concise delivery, and stakeholder-triggered revisiting. IDs 24–30 cover analytical communication. IDs 31–34 cover the repair scenarios: separated mix and within-segment effects, early-warning leakage/capacity, weighted survey inference, and an under-specified risk definition. Paths in evals.json are relative to this evaluation directory. Fixtures are synthetic and are not real business observations. Do not feed expected_output, expectations, evaluator code, or oracle results to a model executing a task.

## Analytical communication cases

These development scenarios exercise delivery judgments and proportional presentation, not a chart-count policy:

| ID | Case | Discriminating review expectation |
| --- | --- | --- |
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

1. Preserve the pre-repair working-tree skill snapshot before editing. Freeze repaired skill files, task inputs, and grading criteria before starting runs. Use cases 18, 20, 30, and 31–34: seven scenarios, one run per version, fourteen runs total.
2. Give each runner a fresh workspace containing only its assigned skill version, prompt, and listed input fixtures. Include the same statement in every run: “The user is unavailable during this task. Complete the task autonomously within its stated scope and output-format constraints.” Runners do not receive expected answers, grading criteria, evaluator code, or the other skill version.
3. Match model/version, reasoning setting, tools, environment, and task inputs across versions. Short cases 20, 30, and 34 have a 10-minute cap and a 12,000-token output budget requested in the task prompt; record whether actual output stayed within it. Substantial cases 18, 31, 32, and 33 have a 45-minute cap with no additional output-token cap beyond the model default. Record actual limits, tokens, duration, runtime availability, and interruptions. Mark limit-hit runs TRUNCATED; report completion and resource use separately from analytical quality.
4. An independent grader receives anonymized outputs in randomized order, plus the frozen rubric and expected answers. Record criterion-level evidence. Score correctness, analytical depth, communication, and assumption handling separately. The under-specified case measures unattended assumption handling; these runs do not test interactive grilling.
5. Preserve outputs, traces, and artifacts. After Round 1, generate the review viewer, report results and total resource use, then stop for user review. Round 2 requires user authorization and consists of two additional repetitions per version for selected close or inconsistent scenarios; do not change the skill between repetitions being pooled.
6. These seven development scenarios support a controlled smoke comparison, not a reliable generalization claim. Previously exposed held-out cases are not evidence of uncontaminated performance; reserve fresh cases for generalization.

## Three separate scoring axes

Use the independent analytical-quality rubric in `../../skills/data-analyst/references/analytical-quality.md` for substantive review. Record the axes separately; no averaging away a serious failure.

- **Technical correctness and functionality (0–3):** use the rubric's grain/semantics, preparation, validity, reproducibility and functionality criteria. Recompute critical quantities and inspect actual evidence.
- **Analytical quality and completeness (0–3):** use objective alignment, question feasibility, method, depth/follow-up, uncertainty/alternatives, usefulness and honest-scope criteria. A concise calculation can be strong without a hypothesis tree; a substantial investigation cannot pass with profiling alone.
- **Communication and usability (0–3):** use visual analytical value and synthesis/accessibility criteria. Inspect actual reader-facing coverage and task evidence, including consequential follow-up. Check readable delivery in the required format; raw Markdown links do not satisfy browser delivery. Accept purposeful repeated charts, static visuals and concise answers when appropriate.

Use the rubric's shared anchors: 0 missing/misleading, 1 superficial, 2 adequate, 3 strong. Record per-criterion evidence and separate dimension decisions, with applicable minima. No material criterion below 2 or critical failure permits complete delivery. Record lifecycle compliance separately from artifact quality; a final report alone cannot establish chronological execution or predeclared criteria.

A filled ledger, exact rubric vocabulary, ten stage headings, numerous charts or correct aggregates alone cannot earn an analytical-depth pass. Review supplied scripts/results, report claims and delivered artifact together. Include negative controls: a heading-rich generic report, a shallow report with correct totals, and a ledger claiming PASS where actual violates expected. The first two may satisfy some structure/numerical checks but fail substantive review; the third must fail integrity.

## Deterministic evaluator boundary

`evaluate.py` recomputes factual oracles from development CSVs. For an optional normalized result submission, save a JSON object with `facts` and `ledger`; each ledger entry includes `fact`, `expected`, `actual`, `condition`, `status`, `method` and `evidence`. `test_evaluators.py` contains a minimal example. Run:

```sh
python3 evals/data-analyst/evaluate.py submission.json --required orders.revenue orders.aov
```

An independent grader can extract this normalized JSON from the report without forcing the analyst to produce evaluator-specific output. Preserve original output and note extraction ambiguity; do not repair missing evidence during extraction. Expected values must match independently computed oracles; actual values must match both condition and reported quantity. Check names and declared PASS are insufficient. Bounds cannot weaken exact-value requirements. Non-finite quantities, duplicate checks and absent evidence are rejected. Evidence locators and method strings are only consistency checks: the independent reviewer must open the evidence, rerun calculations and inspect artifacts before awarding verification integrity. The script always returns `overall_pass: null` and `analytical_quality: REQUIRES INDEPENDENT REVIEW`, including for a numerically correct shallow answer. It does not pretend to grade prose or infer execution from a declaration.

The unittest suite exercises known correct calculations and intentionally weak/misleading submissions. Passing these tests validates evaluator behavior, not that the revised skill improves model outputs. Record deterministic test results separately from actual baseline/revised model comparisons.

## Validation status

The deterministic checks passed: `python3 -m unittest discover -s evals/data-analyst -v` (51 tests), `python3 skills/data-analyst/scripts/stats_helpers.py --selftest`, `python3 scripts/validate_skills.py` (0 issues), and `git diff --check`.

Round 1 ran cases 18, 20, 30, and 31–34 once per version (14 runs total) with Codex `gpt-6-luna`, medium reasoning. All runs exited successfully within the 10-minute short-case or 45-minute substantial-case timeouts; none was truncated. The runs used 2,839,258 input tokens and 48,942 output tokens (2,888,200 total); summed model-run duration was 526.6 seconds. Baseline used 1,613,797 tokens in 277.5 seconds, and repaired used 1,274,403 tokens in 249.1 seconds. These durations are sums of individual runs, not end-to-end elapsed time.

Both versions passed 22 of 23 exact expectations. The repaired case 18 dashboard fixes a baseline key mismatch (`D.tierchannel` versus the embedded `tier_channel` key), and its report offers a deeper investigation. Both handoffs failed to disclose that browser rendering was unavailable. The other six cases passed every listed factual and format expectation. Pairwise preferences were mixed and graders disagreed on several cases; with one run per version, this is a smoke comparison rather than evidence of a general skill effect.

The intended 12,000-token short-case output budget was recorded as metadata but was neither sent as a model instruction nor enforced: the Codex CLI used here exposes no hard output-token cap. Actual short-case outputs stayed below 2,767 tokens, which does not establish cap compliance. Substantial cases had no additional output cap. The behavioral runs used `gpt-6-luna`, not Opus 5.5. Both blind grading passes used fresh contexts and randomized candidate order, but the graders were from the same model family as the runners. No browser executable was available; browser rendering and interaction remain unverified. The first grading packet put fixtures at a shared pair root, so those initial grades were discarded and rerun with each candidate's isolated inputs restored.

A passing deterministic suite does not establish improved model behavior. The full criterion evidence, separate 0–3 scores, and generated output review are provided with the Round 1 handoff.
