## Overview

This file defines how AI agents should use the skills in this repository when working on Alpha's projects.

- **Audience**: AI coding agents (Cursor, Claude Code, Windsurf, etc.)
- **Goal**: Apply Alpha's preferred standards consistently and transparently.

## Global Guidance for All Agents

- **Respect project-specific skills** in the `skills/` directory and `.cursor/skills-cursor/`.
- **Prefer existing patterns** in the codebase over inventing new ones.
- **Keep changes small and safe**: avoid broad refactors unless explicitly requested.
- **Explain non-obvious decisions briefly** in natural language, not in redundant code comments.
- **Run tests or linters** when you make non-trivial changes, if available and fast.

## Default Coding Agent

- **Purpose**: Day‑to‑day implementation, refactors, and bug fixes.
- **Style**:
  - Follow repository standards from `README.md` and any relevant `SKILL.md` files.
  - Use clear, modern patterns for the stack in use (TypeScript/JS, testing setup, etc.).
  - Avoid over-engineering; favor readable, pragmatic solutions.
- **Behavior**:
  - When in doubt, infer intent from existing code and skills instead of asking.
  - Keep PR-sized changes: cohesive, well-scoped, and documented in commit messages when requested.

## Testing‑Focused Agent

- **Purpose**: Design, improve, and maintain tests.
- **When to use**: When the task is primarily about tests (unit, integration, or end‑to‑end).
- **Behavior**:
  - Prefer patterns and conventions from `skills/testing/SKILL.md` and its references (e.g., Vitest docs under `skills/testing/references/`).
  - Keep tests deterministic, isolated, and fast by default.
  - Use factories and helpers instead of duplicating setup logic where appropriate.

## Adding New Agents

When a new, recurring workflow emerges (e.g., performance tuning, data migrations):

- **Define a focused purpose** for the agent.
- **Link it to one or more skills** (e.g., a new `skills/performance/SKILL.md`).
- **Describe expected behavior** in a short section like those above.

