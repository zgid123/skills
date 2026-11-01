# Playbook: diagnose a change

Use when a metric moved and someone asks why: revenue fell, conversion rose, churn spiked, pass rates dropped, tickets doubled.

The goal is to locate the change (where and when), size each contributor, and test the explanation against the most plausible alternatives — then say plainly what is known and what needs confirmation.

## Frame it

- **Exact metric and definition**: numerator, denominator, population, unit. Ratios need both parts examined.
- **Periods**: complete and comparable (same weekdays, season, length). Flag partial periods.
- **Size of the move vs normal noise**: compare with typical period-to-period variation before calling it a change.
- **Known events**: releases, price changes, campaigns, policy or tracking changes, holidays.

## Analysis sequence

1. **Rule out measurement first.** Tracking changes, pipeline gaps, definition changes, late-arriving data, duplicates. Check row counts and freshness around the change date. Many "drops" are data problems.
2. **Decompose the metric.** Split into its drivers (e.g., revenue = traffic × conversion × order value; overall pass rate = completion rate × pass-given-completion rate; pass count = enrolments × both rates). Which driver moved?
3. **Locate it.** Break down by the main dimensions (channel, platform, region, product, cohort, course). Rank segments by contribution to the change, not by their own % change.
4. **Separate mix from rate.** If segment shares shifted, the overall rate can move even when no segment changed (Simpson's paradox). Report both the within-segment rate change and the mix effect.
5. **Pin the timing.** Daily or event-level series around the change. A step on a specific date points to an event; a slow drift points to something gradual.
6. **Test the explanation.** Find a comparison that the explanation predicts and the alternatives do not: affected vs unaffected versions, regions or cohorts on the same days; before vs after within the same entities. Report what survived.
7. **Size the impact** in units the reader cares about (orders, money, students) and what recovery would look like.

## Charts that work

- Driver tree or waterfall: contribution of each driver or segment to the total change.
- Dumbbell / slope chart: each segment before vs after.
- Daily line with the event annotated; split lines for affected vs unaffected groups.
- Small multiples by segment when the pattern differs.

## Report shape

Title states the observed change and size. State a cause only when the design identifies it; otherwise describe the best-supported explanation as a hypothesis and say what would confirm it. Summary: how big, where, when, why (with confidence), what to do. Findings: where the change is → when it started → what explains it and what was ruled out → impact. See the [example report](../references/example-report.md).

## Traps checklist

- Explaining noise: the change is within normal variation.
- Ranking segments by % change instead of contribution (tiny segments dominate).
- Averaging rates across segments instead of recomputing from totals.
- Ignoring mix shift.
- Comparing incomplete or non-equivalent periods.
- Stopping at the first plausible story without testing an alternative.
- Stating a cause as proven when only timing coincides; say what would confirm it.
