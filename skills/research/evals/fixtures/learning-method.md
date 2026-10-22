# M: A budgeted two-stage document search

Fictional extract, not a real publication or full paper. Author Cy Reed, 2025, Journal of Search Methods; peer-reviewed within this fixture. No DOI or pages supplied. Sections below can be cited by name.

## Method

Stage 1 uses L's token-overlap method to select k candidates. Stage 2 assigns each candidate a semantic relevance score s(q,d), where q is the query and d is a document, and returns the candidate with the highest score. The semantic score is supplied by an external model; its architecture and training data are not described in this extract. The paper does not claim to recover documents omitted by Stage 1.

The estimated query cost is C(k) = a + b × k, where C is time in milliseconds, a is candidate-generation time, b is scoring time per candidate, and k is the number of candidates. The budget rule is k ≤ floor((T − a) / b), with b > 0 and T the time budget in milliseconds. This is an estimate; variable document lengths and system load can violate it. It is not a rule that larger k always improves final answer quality.

## Worked example supplied by the paper

Query: “car repair.” Documents: d1 “car repair manual”; d2 “automobile maintenance guide”; d3 “car insurance prices.” There is no stemming or synonym expansion in Stage 1. Token-overlap scores are d1=2, d2=0, d3=1. With k=2, candidates are d1 and d3; the semantic scorer cannot choose d2. The paper supplies no semantic scores for these documents. It does not declare which documents are actually relevant to the user's need.

## Results

On one synthetic collection of 1,000 documents and 100 test queries, the mean top-result relevance rate was 70% for token-overlap ranking alone and 80% for two-stage search at k=20. The authors report mean query latency of 15 ms for token overlap and 55 ms for two-stage search. These are query-level benchmark summaries, not participant data. No uncertainty intervals, per-query results, significance tests, or other collections are supplied.

## Discussion

The authors claim a useful quality/cost tradeoff on this benchmark. Limitations include one synthetic collection, omitted semantic model details, candidate omissions, and variable processing cost. Generalization to real multilingual document collections is untested in the supplied extract.
