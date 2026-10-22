# Alpha Agent Skills

This repository contains reusable instructions for AI coding and document agents. The skills encode Alpha's working preferences for engineering, testing, analysis, presentations, and document creation.

## How to use this repository

Start with [AGENTS.md](AGENTS.md). It maps common tasks to the skill or skills to read. Each skill lives in `skills/<name>/SKILL.md`; follow links in that file only when the current task needs those references.

When adding or updating a skill, include its trigger in `AGENTS.md` and keep an evaluation file at `skills/<name>/evals/evals.json`. Run `python3 scripts/validate_skills.py` to check skill metadata, local links, triggers, evaluation cases, and fixture paths.

## Skill catalog

### Engineering foundations

- [Principles](skills/principles/SKILL.md) - Apply YAGNI, pragmatic reuse, dependency discipline, readable code, and small cohesive changes across engineering tasks.
- [Testing](skills/testing/SKILL.md) - Write focused, deterministic tests. Controllers, adapters, and route handlers use end-to-end tests.

### Languages and application design

- [TypeScript](skills/typescript/SKILL.md) - Write type-safe TypeScript and follow Alpha's naming, module, import, and lint conventions.
- [React](skills/react/SKILL.md) - Build React components and hooks using Alpha's component, typing, and export patterns.
- [Domain-Driven Design](skills/domain-driven-design/SKILL.md) - Model domains, bounded contexts, entities, value objects, repositories, and domain services.
- [CQRS](skills/cqrs/SKILL.md) - Structure TypeScript use cases, commands, queries, handlers, events, and buses using Alpha's CQRS conventions.

### Analysis and reporting

- [Data Analyst](skills/data-analyst/SKILL.md) - Investigate data, define metrics, analyze experiments and trends, and report findings with transparent evidence and limitations.
- [Research](skills/research/SKILL.md) - Learn unfamiliar research topics, find and screen papers, understand their core concepts through layered explanations and examples, map relationships, and follow related ideas through a reading path. Defaults to chat and Markdown; literature synthesis, study design, and manuscript work remain available when requested. Excludes IEEE Access and labels preprints and evidence access. Documents and Research each work independently. See [evaluation instructions](skills/research/evals/README.md).

The data analyst skill includes [evaluation instructions](skills/data-analyst/evals/README.md) and deterministic checks. Run `python3 -m unittest discover -s skills/data-analyst/evals -v` when changing its evaluator. Comparative evaluation notes are in [the data analyst workspace](skills/data-analyst-workspace/README.md).

### Documents and presentations

- [Documents](skills/documents/SKILL.md) - Route [academic writing](skills/documents/references/academic-writing.md) to DOCX reports and coursework, [paper writing](skills/documents/references/paper-writing.md) to research papers and theses, and [personal writing](skills/documents/references/personal-writing.md) to either format. Papers and theses share ICIS by default, with ACM or IEEE when requested, independently of output format; LaTeX source plus PDF is the default. Thesis structure retains chapters and front matter. University and publication templates take priority. The course-report example uses neutral identity placeholders, Word's native automatic TOC field, and a matching PDF preview.
- [SlidevJS](skills/slidevjs/SKILL.md) - Create or update Slidev seminar decks using Alpha's academic theme, addon, project structure, and component guidance.

### Skill development

- [Skill Creator](.agents/skills/skill-creator/SKILL.md) - Create, revise, evaluate, and package reusable skills.

## Evaluations

Evaluation prompts describe realistic tasks and expected outcomes. They are scenarios for evaluating skill behavior, not proof that a skill has passed those scenarios. Some skills also include deterministic checks for specific outputs; those checks do not replace reviewing the resulting work.
