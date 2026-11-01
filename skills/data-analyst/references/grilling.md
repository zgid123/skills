# Grilling

Use this reference when the user asks to be grilled on an analysis ("grill me", "stress-test this analysis plan", "challenge my metric"). It is also mandatory, without being asked, before committing to a substantial analysis that is missing context: any decision that the request, the data, its documentation and existing project files do not settle, that only the user can make, and that would change the answer. Grilling is an interview that ends in a shared understanding of the analysis brief; it does not run the analysis by itself.

Adapted from Matt Pocock's [`grill-me` and `grilling` skills](https://github.com/mattpocock/skills/tree/main/skills/productivity) and this repository's swe-lifecycle grilling. Like the latter, it asks exactly one question per message.

## When to grill, and when not to

Grill when a consequential decision is open, for example:

- the decision or reader the analysis serves, when it changes what to measure;
- the outcome or KPI definition (e.g., whether "at risk" means fail, withdraw, or both);
- the population, unit of analysis, period or comparison;
- the prediction cutoff, lead time or review capacity for an early-warning analysis;
- what counts as success, or how wrong the answer can afford to be;
- the deliverable when format matters (inline answer, report, dashboard, required outline);
- a pivot, when the main question turns out to be unsupported and several substitutes are plausible.

Do not grill for:

- **Facts you can find yourself.** Field meanings, row counts, date ranges, codes, keys and coverage come from profiling the data and reading its documentation. Run `scripts/profile_data.py`, read the dictionary, dispatch a sub-agent for broad lookups — then ask only what remains.
- **Focused requests.** A single calculation with a clear definition needs an answer, not an interview. If one detail is ambiguous, state the assumption in the answer.
- **Choices with a sensible default** that would not change the conclusion. Pick the default and record it as *proposed* in `NOTES.md`.
- **Settled context.** Treat explicit instructions, a provided brief or course requirements, and approved metric definitions as settled unless the user reopens them.

If the user is not available to answer (a batch or background run, or they said "don't ask, just do it"), do not block: record each open decision with your recommended answer as a *proposed* assumption in `NOTES.md`, make the analysis robust to it where cheap (e.g., report both definitions), and disclose material assumptions in the requested deliverable's limitations. Keep notes and limitations proportionate to the requested format; a focused inline answer does not require extra files. After the last answer, summarize the settled brief and proceed on that basis. Ask again only when the summary introduces a new consequential assumption or scope change. This intentionally differs from swe-lifecycle, which waits for explicit confirmation of the summarized brief.

## Map the decision tree

Treat the analysis plan as a **decision tree**: each decision branches into decisions that depend on it. The reader and decision come first; they shape the questions; the questions shape the outcome definition and population; those shape the method, cutoffs and deliverable. The **frontier** is every decision whose prerequisites are already settled, so it can be asked now without guessing at answers you have not heard yet.

Start from the existing context: the request, any brief or requirements, the data and its documentation. Inspecting the schema and a few records first usually removes half the questions and sharpens the rest.

## Ask one question at a time

1. Pick the single frontier question that unblocks the most other decisions or carries the most risk of a wrong answer.
2. Ask only that question, with your recommended answer, then stop and wait for the reply. Do not bundle sub-questions, list upcoming questions, or ask a second question in the same message.
3. When the answer arrives, update the tree: settled decisions move the frontier outward, and some branches disappear. Briefly acknowledge what is now settled, then ask the next question.

Format each question like this:

```
❓ **<question title>**: <question body: what is undecided, why it changes the answer, the concrete options, and any fact from the data that bears on it>

➡️ <your recommended answer and the main reason for it>
```

Word the question so "yes" accepts your recommendation. Prefer concrete options grounded in the data ("Withdrawals are 31% of enrollments and fails 22%; treat them as separate outcomes or combine them?") over open prompts ("How should I define risk?"). When a structured question tool is available, you may use it for the same one-question exchange.

While waiting for an answer, you may continue independent work that no open decision affects, such as profiling or quality checks.

## Finish

The interview is done when the frontier is empty: every consequential branch visited and nothing silently assumed. The user may also stop early; record the remaining branches as proposed assumptions.

Summarize the settled decisions (the brief: reader, decision, questions, KPI and outcome definitions, population, period, method choices, deliverable) and any open questions. Proceed using settled decisions and explicitly proposed assumptions; ask again only if the summary reveals a consequential decision that was not discussed or changes scope. Record the brief in `NOTES.md` as stage 1 output when the task warrants a notes file, distinguishing user decisions from proposed assumptions.
