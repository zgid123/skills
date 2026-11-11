---
name: grill-me
description: Explicitly start a one-question-at-a-time interview to sharpen a plan or design.
disable-model-invocation: true
---

# Grill me

Invoke the installed `grilling` skill and follow its interview procedure. If the environment has no skill invocation tool, locate and read its `SKILL.md` directly; when installed side by side, it is at `../grilling/SKILL.md`.

Ask one question at a time, include a recommendation, and wait for the answer before asking the next. Keep the full interview procedure in `grilling` rather than duplicating it here. If that skill is missing, tell the user to install it; do not silently substitute another interview procedure.

Copy both the `grill-me` and `grilling` folders into a repository's skill directory when installing this alias.

## Credit

Adapted from [Matt Pocock](https://github.com/mattpocock)'s [grill-me skill](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me), under the [MIT license](LICENSE). Alpha's adaptation uses the one-question-at-a-time `grilling` skill and adds a fallback for agents without a skill invocation tool.
