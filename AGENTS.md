## Overview

This file is the **canonical template** for all of Alpha's projects. Copy it into a project's root `AGENTS.md` and adjust the skills path (`skills/` → `.agents/skills/`) as needed.

- **Audience**: AI coding agents (Cursor, Claude Code, Windsurf, Gemini, etc.)
- **Goal**: Apply Alpha's preferred standards consistently and transparently across every project.

---

## Mandatory Skill-Reading Protocol

**Before writing or modifying any code, you MUST read the relevant skills. This is not optional.**

### Step 1 — Always Read First

Read these two skills at the start of every task, no exceptions:

1. `skills/principles/SKILL.md` — engineering principles (YAGNI, pragmatic DRY, small safe changes)
2. `skills/testing/SKILL.md` — testing conventions

### Step 2 — Trigger-Based Skills

Read the following skills when the task matches their trigger. Do not skip them.

| Trigger | Skill to Read |
|---|---|
| Creating, refactoring, or reviewing any domain model, aggregate, entity, value object, repository contract, domain service, command, query, or bounded context | `skills/domain-driven-design/SKILL.md` and all files under `skills/domain-driven-design/references/` |
| Deciding a filename, directory name, class name, function name, variable name, or import style — in any language | Read the skill for that language (e.g., `skills/typescript/SKILL.md` for `.ts` files). If no skill exists for the language, follow the closest existing convention in the codebase. |
| Writing or modifying a React component, hook, or JSX file (`.tsx`, `.jsx`) | `skills/react/SKILL.md` and all files under `skills/react/references/` — read these in addition to `skills/typescript/SKILL.md`. |
| Writing or modifying tests | `skills/testing/SKILL.md` |

### Step 3 — Confirm Before Acting

After reading the relevant skills, verify:

- Your planned names, structure, and patterns match what the skill prescribes.
- You are not introducing abstractions, dependencies, or layers that the skill says to avoid.
- If the skill and the existing codebase conflict, follow the existing codebase and note the discrepancy briefly.

---

## Global Rules

- **Prefer existing patterns** over inventing new ones.
- **Apply YAGNI**: do not add features, abstractions, configuration, or dependencies that are not required right now.
- **Apply pragmatic DRY**: reuse existing helpers and conventions; do not create premature abstractions just to remove harmless duplication.
- **Keep changes small and safe**: avoid broad refactors unless explicitly requested.
- **Explain non-obvious decisions briefly** in natural language — not redundant inline comments.
- **Do not hard-wrap prose**: keep Markdown paragraphs and bullet text on a single line unless the format requires line breaks.
- **Run tests or linters** after non-trivial changes, if available and fast.

---

## Agent Roles

### Default Coding Agent

**Purpose**: Day-to-day implementation, refactors, and bug fixes.

**Behavior**:
- Apply the mandatory skill-reading protocol above before every task.
- Follow `README.md` and any `SKILL.md` relevant to the files being changed.
- When in doubt, infer intent from existing code and skills rather than asking.
- Keep changes cohesive and well-scoped.

### Testing-Focused Agent

**Purpose**: Design, improve, and maintain tests.

**When to use**: When the task is primarily about tests (unit, integration, or end-to-end).

**Behavior**:
- Apply the mandatory skill-reading protocol above, with emphasis on `skills/testing/SKILL.md`.
- Keep tests deterministic, isolated, and fast.
- Use factories and helpers instead of duplicating setup logic.

---

## Adding Skills

When a new recurring pattern emerges (e.g., performance, migrations):

- Add a `skills/<topic>/SKILL.md`.
- Add a trigger row to the **Trigger-Based Skills** table above.
- Describe the expected agent behavior in a new Agent Role section if needed.
