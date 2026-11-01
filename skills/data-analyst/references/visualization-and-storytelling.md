# Visualization and Analytical Storytelling

## Contents

- [Visualization and Analytical Storytelling](#visualization-and-analytical-storytelling)
  - [Contents](#contents)
  - [What the reader needs](#what-the-reader-needs)
  - [Report structure](#report-structure)
  - [Writing a finding](#writing-a-finding)
  - [Caveats without hedging](#caveats-without-hedging)
  - [Tables](#tables)
  - [Choosing a chart](#choosing-a-chart)
  - [Chart craft](#chart-craft)
  - [Before you ship](#before-you-ship)
  - [Cross-references](#cross-references)

## What the reader needs

A reader opens a report to learn three things: **what is true, how sure we are, and what it means for them.** Everything else (how the data was queried, every check that passed, every table produced) is supporting material. It should be reachable, not in the way.

Write for the stated reader. A teacher, operations manager or executive needs plain words and the consequence; a methods reviewer needs the method section and the appendix. One report can serve both by putting the answer first and the depth later.

## Report structure

Use this order for substantial reports (the [report template](../assets/report-template.html) already has it):

1. **Title as the main finding.** "Two early warning signs catch half of later withdrawals" — not "OULAD Analysis Report".
2. **Summary box (3–5 sentences).** The answer, its key number and population, what it means, and the status in plain words (e.g., "retrospective analysis; not yet tested on live students").
3. **Key numbers.** 3–4 tiles with the numbers the reader should remember, each with a one-line meaning.
4. **Findings.** One section per finding, ordered by importance to the reader, not by the order you computed them.
5. **What this means / recommendations.** Only what the evidence supports; say what would confirm it.
6. **Limitations.** The few limits that could change a conclusion, each tied to the claim it weakens.
7. **Method.** Data, population, definitions, approach — short, in plain terms.
8. **Appendix.** Wide tables, sensitivity grids, data quality detail, links to `results/` and `code/`.

This order follows the **Pyramid principle**: the answer first, then the few findings that support it, then the evidence beneath each. Keep to about **three** key messages (the Rule of Three); a reader remembers three findings, not nine. Address each stakeholder group at the level of detail it needs.

If the user or a course requires a different outline (for example an 18-section academic report), use it — and still lead each section with its answer.

## Writing a finding

Each finding section follows the same shape:

```text
## [Claim with a number]                     ← headline is the finding
[1–2 sentences: the evidence and the comparison, with population.]
[Chart or one small table.]
[1–2 sentences: what it means for the reader.]
[1 sentence: the main limit or the check that it survived.]
```

Illustrative example (the figures below are invented to demonstrate a finding; they are not a claim about a real cohort):

> **Students missing an assignment by day 60 are about 3.3 times as likely to fail or withdraw by course end**
>
> Among 5,903 students active at day 60 in the October 2014 courses, 85% of those who had missed at least one assignment due by day 60 later failed or withdrew by course end, compared with 26% of those who submitted every assignment due by day 60. That is about 3.3 times the observed risk; course-level rates are 50–96% versus 16–34%.
>
> _[chart: risk rate by submission status, small multiples by course]_
>
> For a tutor, any missed assignment by day 60 is an early signal for a supportive check-in about later failure or withdrawal.
>
> This is an association: missing work may reflect problems that started earlier, so it flags students for contact rather than explaining why they struggle. The example assumes outcomes are observed through course end and does not treat failures or withdrawals before day 60 as later outcomes.

Good finding prose:

- Uses the reader's words (students, orders, customers), not internal variable names. Introduce a field name once in the method section if needed.
- Gives the comparison every time: "26% vs 85%", not "85%".
- States magnitudes in units that matter: people, money, days, percentage points.
- Explains a technical metric once, in reader terms: "precision 60% means 6 of every 10 students on the review list really were at risk."
- Says the observation (what the data shows) separately from the interpretation (why it might be so). Label mechanisms you did not test as possibilities.

## Caveats without hedging

Over-caveating hides findings as surely as over-claiming distorts them. Rules of thumb:

- **Caveat a claim once, where it matters.** Put the single most important limit in the finding; collect the rest in Limitations.
- **Only caveats that could change a conclusion.** "Results may vary" is noise. "Scores were released with unknown delay, so day-60 score features may not be available live" is useful.
- **Prefer a test to a caveat.** If you can run a sensitivity check, run it and report the result ("the gap is unchanged when we assume a 28-day delay") instead of warning that it might matter.
- **State status once, plainly**, in the summary: complete / partial / feasibility / unverified, with scope.
- **No defensive vocabulary in every sentence.** Words like "conditional", "proxy", "not causal", "exploratory" belong where they change interpretation, not as a reflex.

## Tables

- In the body, a table must support one claim. Keep only the columns the claim needs (often 3–5) and the rows that matter. Round sensibly (percentages to whole numbers or one decimal).
- Put exhaustive tables (all cutoffs × all models × all metrics) in the appendix or `results/`, and link them.
- Prefer a chart when the reader needs to see a pattern; prefer a table when they need exact values for a few items.
- Use human column headers ("Flagged students", "Share later at risk") rather than `alert_rate`, `risk_rate`.

## Choosing a chart

Pick the chart from the comparison the reader must make. Reusing one chart type for similar comparisons is fine; there is no quota.

| Reader needs to see | Use | Avoid |
| --- | --- | --- |
| Ranking across categories | Sorted horizontal bar, highlight the focus bar | Unsorted bars, 3D |
| Change between two points for the same groups | Slope chart, paired dots (dumbbell) | Side-by-side composition bars that hide pairing |
| Trend over time | Line chart, direct labels at line ends | Spaghetti of 10+ lines (use small multiples) |
| Difference with uncertainty | Dot + interval plot, zero reference line | Bars with error whiskers for non-count measures |
| Distribution or spread | Histogram, box/strip plot | A lone mean |
| Same pattern across many groups | Small multiples with shared axes | One cluttered chart |
| Part-to-whole, few categories | Stacked or 100% bar | Pies with many slices |
| Two continuous variables | Scatter (binned or hexbin when large) | Forced linear fit on curved data |
| Two categorical dimensions | Heatmap with ordered, single-hue scale | Rainbow scales |
| Ordered stages | Funnel as horizontal bars with step conversion | Disconnected pies |
| Model trade-off (early warning) | Precision and recall vs review capacity; calibration plot | A single accuracy number |

When a sensitivity check or subgroup result changes the headline, show baseline and alternative side by side; an isolated adjusted number in a callout is not enough.

## Chart craft

`scripts/chart_style.py` applies these defaults; use it rather than raw matplotlib defaults.

- **Title states the finding**; a smaller subtitle states the measure, population and period. Axis labels carry units.
- **Bars start at zero.** Lines may use a non-zero axis when the change is the point; label it clearly.
- **One accent colour for the focus**, greys for context. Colour encodes meaning, not decoration. Use the colour-blind-safe palette in the script; never rely on red vs green alone.
- **Label directly** (bar values, line-end labels) instead of distant legends when there are few series.
- **Remove chart junk**: no top/right spines, light value-axis grid only, no shadows or 3D.
- **Annotate what matters**: a policy change, a threshold, the gap you are talking about.
- **Show uncertainty** when the claim is inferential (intervals, bands). Census totals need none.
- **Source line** under the chart: dataset, population, n.
- Export PNG for the report and SVG for reuse.

## Before you ship

Read the report as the stated reader, top to bottom, and check:

- Can I state the main finding after reading only the title and summary?
- Does every finding section have a claim, a number with its comparison, and a meaning?
- Is every chart title a sentence a reader could repeat?
- Are there more than two or three tables in the body? Move the rest to the appendix.
- Is any caveat repeated, or attached to a claim it does not affect? Remove it.
- Do the displayed numbers match `results/`?
- Are the most important findings visible in the report itself, not only in linked files?

## Cross-references

- Dashboards and interactive delivery: [Dashboards and BI](./dashboards-and-bi.md)
- Target voice: [Example report](./example-report.md)
- Ratios and percentage-point wording: [Metrics and KPIs](./metrics-and-kpis.md)
- Distribution plots during exploration: [EDA](./eda.md)
- Communicating model performance: [Predictive analysis](./predictive-analysis.md)
