## Overview

This file is the **canonical template** for all of Alpha's projects. Copy it into a project's root `AGENTS.md` and adjust the skills path (`skills/` → `.agents/skills/`) as needed.

- **Audience**: AI coding agents (Cursor, Claude Code, Windsurf, Gemini, etc.)
- **Goal**: Apply Alpha's preferred standards consistently and transparently across every project.

---

## Mandatory Skill-Reading Protocol

**Before writing or modifying any code, you MUST read the relevant skills. This is not optional.**

### Step 1 — Always Read First

Read these two skills at the start of every coding or skill-maintenance task:

1. `skills/principles/SKILL.md` — engineering principles (YAGNI, pragmatic DRY, small safe changes)
2. `skills/testing/SKILL.md` — testing conventions

### Step 2 — Trigger-Based Skills

Read the following skills when the task matches their trigger. Do not skip them.

| Trigger | Skill to Read |
| --- | --- |
| Creating, refactoring, or reviewing any domain model, aggregate, entity, value object, repository contract, domain service, command, query, or bounded context | `skills/domain-driven-design/SKILL.md`, then the references relevant to the task |
| Creating, refactoring, or reviewing CQRS commands, command handlers, queries, query handlers, buses, application use cases, read/write separation, or `@cqrsx/core` wiring in TypeScript | `skills/cqrs/SKILL.md`, `skills/domain-driven-design/SKILL.md`, `skills/typescript/SKILL.md`, then the relevant references from each |
| Creating, editing, refactoring, or reviewing any TypeScript (`.ts`) file, type (`T` prefix), interface (`I` prefix), function parameter object, path alias (`#/` imports), `#private` class member, tsconfig extending `@alphacifer/tsconfig`, or Biome lint/format configuration | `skills/typescript/SKILL.md`, then the references relevant to the task |
| Deciding a filename, directory name, class name, function name, variable name, or import style — in any language | Read the skill for that language (e.g., `skills/typescript/SKILL.md` for `.ts` files). If no skill exists for the language, follow the closest existing convention in the codebase. |
| Writing or modifying a React component, hook, or JSX file (`.tsx`, `.jsx`) | `skills/react/SKILL.md` and `skills/typescript/SKILL.md`, then the references relevant to the task |
| Creating, scaffolding, editing, or reorganizing a Slidev presentation, `slides.md`, Slidev section pages, or a Slidev deck inside a monorepo | `skills/slidevjs/SKILL.md` |
| Analyzing datasets (.csv, .xlsx, SQL tables, dataframes), performing data analysis, exploratory data analysis (EDA), metric/KPI design, cohort/retention/funnel queries, A/B test analysis, building analytical dashboards or visual reports, or framing business recommendations from data | `skills/data-analyst/SKILL.md`, then only the reference files routed by that skill for the current task |
| Writing or modifying tests, Vitest suites, test data factories (fishery, faker), mocks, or fakes | `skills/testing/SKILL.md`, then the references relevant to the test type and framework |
| Writing, structuring, creating, revising, or formatting academic or personal documents in DOCX or LaTeX | `skills/documents/SKILL.md`, then only the references relevant to the requested content and output format |
| Exploring unfamiliar research topics, searching for scholarly papers, explaining paper concepts or prerequisites, creating concept maps grounded in papers, following related ideas, summarizing or critically analyzing studies, synthesizing literature, identifying research gaps, designing research, or substantively drafting or revising a research paper or thesis | `skills/research/SKILL.md`, including its source policy, then only the references relevant to the current learning or research stage; use `skills/documents/SKILL.md` for manuscript production and formatting-only work |
| Creating, modifying, improving, evaluating, or benchmarking skills, or optimizing skill descriptions | `.agents/skills/skill-creator/SKILL.md` |

### Step 3 — Confirm Before Acting

After reading the relevant skills, verify:

- Your planned names, structure, and patterns match what the skill prescribes.
- You are not introducing abstractions, dependencies, or layers that the skill says to avoid.
- If the skill and the existing codebase conflict, follow the existing codebase and note the discrepancy briefly.

Read additional references when the work reaches their subject. The skill's reference guide determines which files apply; a task does not require every reference in a directory.

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

- Apply the mandatory skill-reading protocol above, with emphasis on `skills/testing/SKILL.md` and its references.
- Keep tests deterministic, isolated, and fast.
- Use factories and helpers instead of duplicating setup logic.

### Data Analyst

**Purpose**: Apply the ten-stage data analytics methodology from business understanding through deployment and feedback, including metric design, data quality validation, analysis, and usable visual delivery.

**When to use**: When the task is primarily analytical, exploratory, metric-oriented, or inspecting analytical data pipelines.

**Behavior**:

- Apply the mandatory skill-reading protocol above. For end-to-end dataset analysis, read `skills/data-analyst/workflows/analytics-lifecycle.md`; load only the supporting `skills/data-analyst/references/` files routed by the skill for the current question and stage. For focused requests, apply the relevant stages proportionately and read the full workflow only when needed.
- Clarify the commercial decision or informational purpose, primary metric, and grain before writing queries or code.
- Deliver a usable report or dashboard suited to substantial analyses and a chart, visual report, or compact result table for focused questions; use existing project/BI tooling or portable HTML by default, respecting explicit format constraints.
- Verify the analysis before deployment, inspect the delivered artifact, and distinguish stakeholder feedback and future outcomes from verified results.
- Never silently alter, drop, or impute data without transparent documentation.
- Distinguish between correlation and causation; report distributions and uncertainty intervals over naked averages.

---

## Adding Skills

When a new recurring pattern emerges (e.g., performance, migrations):

- Use `.agents/skills/skill-creator/SKILL.md` to guide the creation, refinement, or benchmarking of the new skill.
- Add a `skills/<topic>/SKILL.md`.
- Add a trigger row to the **Trigger-Based Skills** table above.
- Describe the expected agent behavior in a new Agent Role section if needed.
