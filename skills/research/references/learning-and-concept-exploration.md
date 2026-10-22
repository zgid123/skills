# Learning and concept exploration

Use this guidance for understanding research topics and papers, including follow-up questions about concepts encountered while reading. Apply [Source policy](source-policy.md), use [Discovery and screening](discovery-and-screening.md) for searches, and use [Critical analysis and synthesis](critical-analysis-and-synthesis.md) for evidence extraction and appraisal. A learning request does not automatically require manuscript work or exported notes.

## Establish an accessible starting point

Infer the user's goal, background, and preferred language from context and prior explanations. Ask only when a missing choice would substantially change the answer. If background is unknown, start with accessible language and define essential terms without assuming the user lacks all subject knowledge. Introduce prerequisites just before they are needed; avoid an encyclopedic glossary or a long questionnaire before helping.

For a broad topic, explain the central question and useful subtopics, then build a short reading path. A survey or tutorial can orient the learner; primary papers support claims about particular methods and findings. Explain what each recommended item teaches, why it comes at that point in the path, and what background it assumes. Prioritize learning value and relevance rather than citation counts or prestige. There is no fixed paper quota.

## Explain in layers

Give a quick takeaway first, then enough detail for the requested understanding. Use the following as a flexible structure rather than mandatory headings for every answer:

1. **Big picture:** what problem the paper addresses, its central idea, and why the idea matters to the user's question.
2. **Essential background:** define the key concepts and prerequisites in plain language. Distinguish established background from a contribution introduced by this paper. Verify specialized background using appropriate inspected sources; label unsupported or unresolved explanations instead of attributing them to the paper.
3. **How it works:** explain the mechanism, argument, or method step by step. Use a small worked example when helpful, labeling invented examples and numbers as illustrative. Explain necessary notation, variables, units, and assumptions before relying on an equation. An analogy should identify both the useful correspondence and where it breaks down.
4. **What the evidence supports:** summarize the findings, evaluation conditions, and important limitations using the critical-reading guidance. Separate author claims, observed results, and your interpretation. Attach source locations where available; do not let a simple explanation turn qualified findings into universal facts.
5. **Connections and next step:** identify the most useful prerequisites, alternatives, or extensions, explain their relationship to the current idea, and suggest what to read or ask next.

Scale this to the user's request: a quick clarification may need only a paragraph and example; a detailed paper explanation should cover the mechanism and evidence. Abstract-only material supports an abstract-bounded explanation, not reconstructed methods. Say which details cannot be established. General background may still be explained with separately verified support; do not imply it is the inaccessible paper's method.

## Use maps to explain relationships

Use a mind map for a broad topic overview and a concept map when understanding depends on relationships between ideas. Choose a small map focused on the current question rather than reproducing every term in a paper. Prefer labeled connections such as “requires,” “extends,” “compares with,” or “is evaluated by.” Use “causes” only when the evidence warrants it. Distinguish prerequisite relations from chronological development and citation links; a reference alone does not establish that one method extends another.

Trace paper-specific nodes and relationships to paper IDs or inspected sections, using labels or a nearby source key. Mark your organizational interpretation and tentative links explicitly. Do not place unresolved hypotheses among established findings without a visible distinction. Add cross-connections only when they clarify a supported relationship.

Use a supported diagram format when available, with a portable Markdown outline or `concept — relationship → concept` list as a fallback. Do not require an installed visualization plugin, external account, or new dependency. If the map repeats a simple explanation without adding clarity, omit it; if the user explicitly requests a map, provide one. A concept map helps organize an explanation but does not demonstrate that the user has learned it.

## Follow related concepts deliberately

When a paper introduces an unfamiliar idea, identify the relevant term, its aliases, its role in the paper, and whether it is a prerequisite, competing approach, or extension. Give a bounded explanation and useful search terms. When the user asks to find related work, search and verify actual sources rather than returning only a proposed search. Follow backward references for foundations and forward citations for later work when accessible, and explain the relationship to the original paper.

Reuse traceable prior notes and the user's established knowledge, inspecting new material only for new or unresolved claims. Recommend the next branch based on the learning goal; do not automatically explore every linked concept. Distinguish suggested follow-up queries from searches actually executed. End a focused explanation when the requested concepts and evidence are adequately covered, with remaining uncertainties visible.

## Offer active understanding checks

When useful, offer a few optional prompts such as “Explain the mechanism in your own words,” “When might it fail?” or “How would this example change under a different assumption?” Let the user attempt an answer before giving feedback if they choose practice. Do not impose a quiz, grade their ability, infer mastery from reading a summary, or claim that a map alone ensures retention. Revisit prior concepts during later related questions when it helps; do not create a spaced-review schedule or flashcard system unless requested.

## Basis for the techniques

- [Keshav, *How to Read a Paper*](https://systems.cs.columbia.edu/ds2-class/papers/keshav-paper.pdf) describes a three-pass reading method. Adapt it as an overview, a mechanism-and-evidence pass, and deeper reconstruction where needed; it is practical guidance rather than proof of a universally optimal reading procedure.
- [Novak and Cañas, *The Theory Underlying Concept Maps and How to Construct and Use Them*](https://www.cs.northwestern.edu/~paritosh/papers/sketch-to-models/Novak-Canas-TheoryUnderlyingConceptMapsHQ.pdf) explains focus questions, labeled relationships, and cross-links. This informs the map structure, not a guarantee of learning from viewing an assistant-generated diagram.
- [Karpicke and Blunt, *Retrieval practice produces more learning than elaborative studying with concept mapping*](https://pubmed.ncbi.nlm.nih.gov/21252317/) reports experimental support for retrieval practice in the studied text-learning tasks. It motivates optional recall and application prompts; it does not establish that every learner, discipline, or combined technique will have the same outcome.
