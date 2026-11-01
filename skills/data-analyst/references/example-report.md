# Example report: the target voice

This invented example illustrates structure and tone; its arithmetic is internally consistent. A real substantial report uses [the HTML template](../assets/report-template.html) with the same structure. Notes in *[brackets]* explain choices and are not part of a report.

---

# Weekly orders fell 9%; Android checkout conversion fell after version 5.2 shipped

*Operations review · 1 Sep–12 Oct 2026 · seven-day average · completed orders across four channels · prepared 14 Oct 2026*

> **Summary.** Completed orders fell from 41,200 to 37,500 per seven days (−9%) after 22 September. Android accounted for 3,400 of the 3,700-order decline (92%). Android product-view sessions stayed near 283,333 per week while conversion fell from 3.1% to 1.9%; at that traffic level, the 1.2-point decline corresponds to about 3,400 fewer orders per week. The timing makes version 5.2 a leading hypothesis, not a proven cause; a rollback or controlled test would help confirm it. **Status:** complete descriptive analysis for this period; release causality remains unverified.

*[The title states observed changes, not a proven mechanism. The summary gives the population, comparison, implication and status.]*

| Weekly orders lost | Share of decline from Android | Android product-view conversion | Revenue represented by lost orders |
| --- | --- | --- | --- |
| **3,700** (−9%) | **92%** | **3.1% → 1.9%** | **$207,400** at $61 per order |

## 1. Android accounts for most of the order decline

Android orders fell by about 3,400 per seven days; the other three channels together fell by about 300. The Android share is 3,400 ÷ 3,700, or 92%.

*[Chart — Weekly orders by channel, before and after 22 Sep: Android −3,400; web −180; iOS −90; partner −30.]*

The decline is concentrated in Android. That comparison locates the change but does not by itself establish its cause.

## 2. Android conversion fell after version 5.2 shipped

Android product-view sessions stayed near 283,000 per week. Conversion fell from 3.1% (about 8,773 orders) to 1.9% (about 5,377 orders), a difference of approximately 3,400 orders per week. Version 5.2 shipped on 22 September, near the observed change.

*[Chart — Daily Android conversion by app version, with the 22 Sep release marked.]*

Compare version 5.2 with version 5.1 on the same days and check tracking and campaign changes before assigning cause. Users who updated early may differ from those who did not, so a same-day comparison alone does not remove selection bias.

## 3. Other channels and average order value changed little

The other channels together account for about 300 fewer orders per week. Average order value remained around $61, so 3,400 fewer Android orders corresponds to approximately $207,400 in weekly revenue at that value.

| Channel | Conversion before | Conversion after | AOV before | AOV after |
| --- | --- | --- | --- | --- |
| Web | 2.4% | 2.4% | $62 | $62 |
| iOS | 3.3% | 3.2% | $61 | $61 |
| Android | 3.1% | 1.9% | $61 | $61 |

## What to investigate next

1. Check tracking, product-view session counts, and the checkout funnel by app version around 22 September.
2. If operationally safe, run a limited rollback or controlled test and compare conversion before expanding the change.
3. Track Android conversion for two weeks after a fix; define the expected recovery and guardrails before the test.

## Limitations

- Traffic and order values are rounded, so derived counts and revenue are approximate.
- The data is observational. Timing and version comparisons identify a useful hypothesis, not a causal effect.
- Completed orders do not show where unsuccessful sessions left checkout.

## Method

Weekly figures are seven-day averages over 1 Sep–12 Oct 2026. Conversion = completed Android orders ÷ Android sessions with a product view. AOV = completed-order revenue ÷ completed orders. The before and after periods are 1–21 Sep and 22 Sep–12 Oct, equal 21-day windows. Channel totals sum to 41,200 before and 37,500 after; all displayed figures are rounded. Reproducible code and result tables belong in `code/` and `results/`.

## Appendix

- A1. Weekly orders by channel (`results/weekly_channel.csv`)
- A2. Daily conversion by platform and app version (`results/daily_conversion_version.csv`)
- A3. Verification checks (`NOTES.md`)
