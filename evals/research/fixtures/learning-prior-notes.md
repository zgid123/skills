# Prior-session learning notes

All papers and observations here are fictional. These notes are traceable prior reading, not newly inspected full text. The user has already learned M's two stages and the idea of a latency budget. They now ask about recall versus precision, so do not repeat the full M explanation.

## Reusable M notes

Identity: M, Cy Reed (2025), A budgeted two-stage document search, Journal of Search Methods; peer-reviewed within the fixture. Source: [previously inspected extract](learning-method.md), Method and Results.

L generates k token-overlap candidates, then M applies a semantic reranker. The reranker can only return a supplied candidate. In the one synthetic benchmark, top-result relevance was 70% versus 80% and latency 15 ms versus 55 ms. No uncertainty intervals are available. These checks were performed in the prior session. No new correction is known.

## New material for the current question

Source K, Tutorial metrics supplement, supplied here for the first time: K is Ada Lin (2024), A tutorial on searching a document collection, Journal of Search Education, peer-reviewed tutorial within this fixture. Recall@k is relevant candidates divided by all relevant documents; precision@k is relevant candidates divided by k. These definitions require relevance judgments.

Suppose an illustrative collection has 10 relevant documents. A nested candidate set of 5 contains 4 relevant documents. Expanding it to 10 adds 1 relevant and 4 irrelevant documents. This is a teaching example, not M's experimental data. K states that candidate recall constrains what a reranker can recover but does not guarantee top-result relevance. No live search or new publication-metadata check occurred.
