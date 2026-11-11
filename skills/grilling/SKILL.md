---
name: grilling
description: Stress-test a plan, decision, or idea through an interview, asking one question at a time. Use when the user asks to be grilled or needs to resolve consequential decisions before proceeding.
---

# Grilling

Interview the user until you reach a shared understanding. Map the plan as a **design tree**: each decision branches into decisions that depend on it. The **frontier** contains questions whose prerequisites are settled.

## Ask one question at a time

Read the available context and preserve decisions already made. Choose the single frontier question that unblocks the most work or carries the greatest risk. Ask only that question, give your recommended answer and a short reason, then wait for the reply. Do not bundle independent decisions, list upcoming questions, or ask another question before the user answers.

Use this format:

```text
❓ **<question title>**: <One decision, with concise options when helpful.>

➡️ <Recommended answer and reason.>
```

Word the question so “yes” accepts your recommendation. After the answer, update the tree and ask the next ready question. Questions that depend on unresolved decisions must wait. Keep questions within the agreed scope; defer future work explicitly.

## Investigate facts

Finding facts is your job. Inspect the repository, documents, and available tools before asking the user for information you can retrieve. When useful and permitted, delegate independent investigation to a sub-agent with focused context; otherwise investigate directly. A pending investigation blocks its dependent question, but another ready question can proceed. Ask only one question at a time even when several investigations finish together.

User decisions about scope, behavior, priorities, and trade-offs require their answer. Do not treat silence or elapsed time as agreement. Reopen a settled decision only when new evidence or a user correction warrants it.

## Confirm understanding

When no in-scope questions remain, summarize the settled decisions and any explicitly deferred questions. Ask the user to confirm the shared understanding before acting on the outcome. If the user ends the interview early, identify unresolved decisions without inventing answers.

## Credit

Adapted from [Matt Pocock](https://github.com/mattpocock)'s [grilling skill](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling), under the [MIT license](LICENSE). Alpha's adaptation asks one question per turn instead of the entire frontier, preserves settled decisions, and supports environments without delegation.
