# Playbook: survey analysis

Use for questionnaire or sampled survey data: international assessments (PISA, TALIS), employee or customer surveys, polls, institutional surveys.

The goal is to describe what a defined population reports, with honest precision, and compare groups fairly — without treating opinions as behaviour or associations as effects.

## Frame it

- **Target population and estimand**: who does the estimate describe (all lower-secondary teachers in Australia; all customers who bought in Q3)? Respondents are not the population.
- **Design**: weights, strata, clusters, replicate weights (BRR, Fay, jackknife), plausible values. Read the technical documentation; the method for standard errors comes from there.
- **Unit**: respondent, school, country. Do not mix levels silently (e.g., school-level answers weighted as if they were teachers).
- **Item meaning**: read the exact question wording and response options in the codebook. Item codes are not meanings.

## Analysis sequence

1. **Inventory items** relevant to the questions; record wording, scale, valid codes, missing codes (not applicable, not reached, invalid).
2. **Valid denominators**: percentages over valid responses for that item; report the valid n and how much is missing. Check whether missingness differs across groups.
3. **Weighted estimates** with the documented weight. Show unweighted n alongside.
4. **Precision** with the documented method (replicate weights or design-based variance). If design information is missing, give point estimates and state that precision cannot be computed correctly — do not substitute a naive standard error.
5. **Comparisons**: between groups or countries, compute the difference and its interval with the same replicate method (covariance matters for paired items on the same respondents).
6. **Likert items**: report the distribution or a clearly defined top-box share ("agree or strongly agree"), not a mean of codes unless the scale justifies it.
7. **Multiple comparisons**: with many items or countries, highlight a few pre-chosen comparisons and treat the rest as exploratory.

## Charts that work

- Dot + interval plot of weighted shares across groups or countries, sorted.
- Diverging stacked bars for Likert distributions, centred on the neutral point.
- Paired dot (dumbbell) for two related items on the same respondents.
- Small multiples by domain or country group.

## Report shape

Summary: the main pattern in population terms, with weighted share, interval and population ("84% of Australian mathematics teachers report giving immediate feedback in most lessons; only 32% give written feedback beyond marks"). Findings: biggest contrasts → whether they hold across groups → what they suggest for the reader's decision. Keep the design explanation in Method.

## Traps checklist

- Unweighted percentages presented as population estimates.
- Naive standard errors that ignore the design.
- Averaging plausible values before computing statistics.
- Pooling countries or domains with different sampling frames.
- Treating self-reported practice as observed behaviour.
- Treating cross-sectional associations as effects.
- Linking survey answers to individuals' outcomes when the data does not contain that linkage.
