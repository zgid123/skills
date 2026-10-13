# Examples of analytical judgment

All numbers below are illustrative synthetic examples, not empirical findings. They teach reasoning choices, not mandatory output templates. Use the actual project's definitions, units, population and evidence.

## From a shallow summary to a supported finding

Shallow: “Average service time rose from 10 to 12 minutes. Investigate efficiency.” This omits population, composition, dispersion and evidence for the implication.

Evidence-backed: “Among completed visits in the two supplied monthly extracts, mean duration rose from 10 to 12 minutes. Within routine and complex visits, duration was unchanged at 8 and 18 minutes; complex visits grew from 20% to 40% of visits. Holding the earlier mix fixed gives 10 minutes in both months. The aggregate increase is consistent with the measured case-mix shift, not observed within-type slowdown. These extracts exclude unfinished visits; their durations and the reason for the mix shift remain unknown.” Link the group counts, weighted calculation and completion rule. This supports a bounded interpretation without claiming a causal mechanism.

## Initial observation → justified follow-up → stopping

An exploratory report finds higher refund rates for one fulfillment center. Before recommending changes, check product mix and return-window maturity because either could alter that comparison. Calculate rates within comparable product groups for orders with a complete return window. If the apparent center difference largely disappears, revise the finding to reflect composition and immature exposure; preserve the original observation and correction. If sparse comparable groups prevent resolution, report that blocker. Stop once the scoped comparison is adequately answered; unrelated customer clustering does not improve this answer.

## Substantial report led by questions

For an illustrative inventory investigation, organize the report around “Where did availability change?”, “Is the change concentrated in particular item classes?”, and “Does incomplete recording explain the pattern?”. Each answer includes magnitude, population/period, a suitable comparison and a link to calculations. A compact synthesis distinguishes supported changes from unresolved recording explanations and their implications. Put schemas, preparation details and the verification ledger in supporting material. Ten lifecycle headings and a claim that all stages passed cannot substitute for those answers.

## Narrow request

User supplies three eligible orders of USD 20, 40 and 60 and asks for average order value. Adequate answer: “AOV is USD 40 per order: USD 120 / 3 eligible orders. Cross-check: (20 + 40 + 60) / 3 = 40.” No dashboard, model, recommendation or outcome plan is needed; apply only relevant gates.

## Dashboard around comparisons

To explain a changing overall outcome rate, show the aggregate change alongside within-segment rates and segment shares using aligned period views. Label eligible counts and rate definitions; annotate whether a fixed-composition comparison alters interpretation. A scorecard can orient the reader but cannot reveal the composition effect alone. Filters recompute eligible numerators and denominators and clearly distinguish unknown from zero. A separate distribution view is useful only if heterogeneity changes the answer. Chart count is not an acceptance criterion.

## Insufficient evidence without abandoning supported work

A delivery extract contains dates and service zones but no promised arrival, actual arrival or outcome label. It cannot establish lateness or train a valid lateness predictor. State that feasibility limit, seek the definitions and missing timestamps, and propose descriptive volume/coverage questions as a revised scope. If the user accepts or the task permits provisional alternatives, execute supported comparisons and label the deliverable partial against the original aim. Do not invent late deliveries or present a volume profile as a completed prediction study.

## Failed gate leads to corrective work

A revenue join duplicates orders because an order can contain multiple items. The source total is USD 300; the joined sum is USD 500. Mark reconciliation FAIL, return to preparation, aggregate the item table to the intended order grain (or analyze item revenue with its own correct definition), rerun the join and verify the USD 300 control total. Update affected findings and charts. A limitation note does not make the USD 500 order-revenue claim valid.

A separate ledger checks unique respondents equal 80 but logs 120 response rows. Even if the code correctly checked 80 users, that ledger entry is invalid evidence. Log the actual unique-respondent value, unit, population and condition, retain response rows as a separately named quantity, then rerun or inspect the corrected check. Do not erase the recorded failure.

## Appropriate stopping and feedback

A focused descriptive comparison has reconciled eligible counts, explained its material composition effect, and shown that a documented alternative exclusion does not change interpretation. No causal question was requested and the extract has no intervention design. Stop with the supported descriptive answer rather than adding a model. If feedback later changes the intended population to first-time visitors, revisit the contract and requirements, establish whether prior visit history exists, and recompute eligible comparisons if feasible; changing a title alone does not incorporate that feedback.
