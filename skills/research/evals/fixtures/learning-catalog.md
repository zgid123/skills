# Fictional learning catalog

These papers, authors, venues, and results are invented evaluation material, not real publications. Do not browse for them. Supplied publication fields are authoritative within this closed fixture. Use paper IDs as local source identities; no DOI, publication URL, or page numbers are supplied. Linked extracts are all the available text, not full papers. This catalog is a supplied index export, not a live search performed by the assistant.

## Records

| ID | Title | Author | Year | Venue and status | Available text and relation |
| --- | --- | --- | --- | --- | --- |
| K | A tutorial on searching a document collection | Ada Lin | 2024 | Journal of Search Education; peer-reviewed tutorial | Tutorial extract below. Introduces retrieval and ranking. |
| L | Token-overlap candidate retrieval | Bo Minh | 2022 | Proceedings of Practical Search; peer-reviewed conference paper | Method extract below. Cited by M as its candidate generator. |
| M | A budgeted two-stage document search | Cy Reed | 2025 | Journal of Search Methods; peer-reviewed paper | [Method, results, and discussion extract](learning-method.md). Builds on L. |
| N | Adaptive candidate budgets | Di Chen | 2026 | Open repository; preprint, not peer reviewed | Abstract: We extend M by choosing a candidate budget per query. On an unspecified search benchmark, the authors report a 12% relative latency reduction against a fixed budget. No candidate selection rule, dataset size, quality result, uncertainty, or code is available. |
| X | An alternative semantic search pipeline | Eli Park | 2025 | IEEE Access; peer-reviewed paper | Abstract claims improved ranking. No extract supplied. |
| W | Search across languages | Flo Diaz | 2026 | Venue and review status unknown | Abstract discusses multilingual retrieval. Metadata unresolved. |

## K: tutorial extract

**Concepts:** A query describes an information need. Retrieval selects candidate documents; ranking orders candidates by a relevance score. A candidate generator trades coverage against computation. Reranking reorders the supplied candidates and cannot recover a relevant document that the generator omitted. A lexical score uses token overlap; a semantic scorer can compare meaning, including synonyms, but has a computational cost.

**Metrics:** Recall@k = relevant documents in the k candidates / all relevant documents in the evaluation collection. Precision@k = relevant documents in the k candidates / k. These metrics require relevance judgments. A larger candidate set can contain more relevant documents, but adding irrelevant candidates can lower its precision. No claim is made that recall or latency changes linearly with k.

## L: method extract

**Method:** Split the query and each document into tokens. Score each document by the count of distinct query tokens it contains. Return the k highest-scoring documents. Ties use a fixed document-ID order.

**Limitation:** Exact token matching can miss a synonym if no query token matches. This extract supplies no benchmark results. M explicitly cites this method as its first stage; this establishes a method dependency, not a historical first-invention claim.
