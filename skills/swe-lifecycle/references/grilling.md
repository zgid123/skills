# Grilling

Use this reference when the user asks to be grilled ("grill me", "grill this plan", "stress-test this design"). It is also mandatory, without being asked, before writing a requirement, change proposal, or design that is missing context: any decision that the request, existing documents, and code do not settle and only the user can make. Grill on `plan` too when consequential decisions block it. Grilling is an interview that ends in a shared understanding; it does not write documents or code by itself.

Adapted from Matt Pocock's [`grill-me` and `grilling` skills](https://github.com/mattpocock/skills/tree/main/skills/productivity). The main difference: the original asks every open question in one round, while this version asks exactly one question per message.

## Map the design tree

Treat the plan as a **design tree**: every decision branches into the decisions that depend on it. The **frontier** is every decision whose prerequisites are already settled, so it can be asked now without guessing at answers you have not heard yet.

Start from the existing context. Read the relevant requirements, proposals, designs, ADRs, knowledge, and source before asking anything, and treat approved documents and accepted decisions as settled unless the user reopens them.

## Ask one question at a time

1. Pick the single frontier question that unblocks the most other decisions or carries the most risk.
2. Ask only that question, with your recommended answer, then stop and wait for the reply. Do not bundle sub-questions, list upcoming questions, or ask a second question in the same message.
3. When the answer arrives, update the tree: settled decisions move the frontier outward, and some branches may disappear. Briefly acknowledge what is now settled, then ask the next question.

Format each question like this:

```
❓ **<question title>**: <question body, which may span several paragraphs and list the options>

➡️ <your recommended answer and the main reason for it>
```

Word the question so "yes" accepts your recommended answer. Prefer concrete options and trade-offs over open-ended prompts.

## Facts versus decisions

Finding facts is your job, never the user's. When a question depends on something you can look up in the repository, documentation, tools, or GitHub, look it up first (dispatch a sub-agent when that is available and the lookup is broad) instead of asking. Decisions about behavior, scope, priorities, risk tolerance, and trade-offs belong to the user: put each one to them and wait.

## Finish

The interview is done when the frontier is empty: every branch visited and nothing silently assumed. The user may also stop early; record the remaining branches as open questions.

Summarize the settled decisions and any open questions, then ask the user to confirm the shared understanding. Do not act on the outcome until they confirm. After confirmation, continue the lifecycle operation that needed it, for example recording decisions in a requirement, change proposal, design, or ADR following [specifications](specifications.md). A decision made during grilling is the user's explicit input, but formal document approval still follows [conventions](conventions.md).
