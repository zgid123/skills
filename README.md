# Alpha Agent Skills

This repository contains reusable instructions for AI coding and document agents. The skills encode Alpha's working preferences for engineering, testing, analysis, presentations, and document creation.

## How to use this repository

Start with [AGENTS.md](AGENTS.md). It maps common tasks to the skill or skills to read. Each skill lives in `skills/<name>/SKILL.md`; follow links in that file only when the current task needs those references.

When adding or updating a skill, include its trigger in `AGENTS.md` and keep an evaluation file at `evals/<name>/evals.json`. Run `python3 scripts/validate_skills.py` to check skill metadata, local links in skills, evaluations, and root README/AGENTS documentation, triggers, evaluation cases, and fixture paths. Run `python3 -m unittest discover -s scripts -p 'test_*.py' -v` when changing this validator.

## Skill catalog

### Engineering foundations

- [Principles](skills/principles/SKILL.md) - Apply YAGNI, pragmatic reuse, dependency discipline, readable code, and small cohesive changes across engineering tasks.
- [Testing](skills/testing/SKILL.md) - Write focused, deterministic tests. Controllers, adapters, and route handlers use end-to-end tests.
- [SWE Lifecycle](skills/swe-lifecycle/SKILL.md) - Coordinate requirements, design, GitHub delivery, implementation, verified knowledge, and durable history. Uses the standalone [Grilling](skills/grilling/SKILL.md) skill when user decisions need clarification. See the [usage guide and limitations](skills/swe-lifecycle/README.md) and [local evaluations](evals/swe-lifecycle/README.md).

### Planning interviews

- [Grilling](skills/grilling/SKILL.md) - Stress-test a plan one question at a time, with a recommendation for each decision.
- [Grill Me](skills/grill-me/SKILL.md) - Explicit invocation alias for Grilling. Copy both folders into your repository’s skill directory; retain each folder’s license. Grilling can also be installed alone.

### Languages and application design

- [TypeScript](skills/typescript/SKILL.md) - Write type-safe TypeScript and follow Alpha's naming, module, import, and lint conventions.
- [React](skills/react/SKILL.md) - Build React components and hooks using Alpha's component, typing, and export patterns.
- [CSS](skills/css/SKILL.md) - Use token-based colors, Tailwind-style palettes, background/border/text theme roles, and cascade-first overrides alongside canonical Tailwind classes, BEM, and CSS Modules. BEM and CSS Modules can be used independently or combined.
- [Domain-Driven Design](skills/domain-driven-design/SKILL.md) - Model domains, bounded contexts, entities, value objects, repositories, and domain services.
- [CQRS](skills/cqrs/SKILL.md) - Structure TypeScript use cases, commands, queries, handlers, events, and buses using Alpha's CQRS conventions.

### Analysis and reporting

- [Data Analyst](skills/data-analyst/SKILL.md) - Investigate data through the ten-stage lifecycle and deliver finding-led reports and dashboards, with templates, chart styling, statistics helpers and playbooks for early warning, change diagnosis and surveys.
- [Research](skills/research/SKILL.md) - Learn unfamiliar research topics, find and screen papers, understand their core concepts through layered explanations and examples, map relationships, and follow related ideas through a reading path. Defaults to chat and Markdown; literature synthesis, study design, and manuscript work remain available when requested. Excludes IEEE Access and labels preprints and evidence access. Documents and Research each work independently. See [evaluation instructions](evals/research/README.md).

The data analyst skill includes [evaluation instructions](evals/data-analyst/README.md) and deterministic checks. Run `python3 -m unittest discover -s evals/data-analyst -v` when changing its evaluator.

### Documents and presentations

- [Documents](skills/documents/SKILL.md) - Route [academic writing](skills/documents/references/academic-writing.md) to DOCX reports and coursework, [paper writing](skills/documents/references/paper-writing.md) to research papers and theses, and [personal writing](skills/documents/references/personal-writing.md) to either format. Papers and theses share ICIS by default, with ACM or IEEE when requested, independently of output format; LaTeX source plus PDF is the default. Thesis structure retains chapters and front matter. University and publication templates take priority. The course-report example uses neutral identity placeholders, Word's native automatic TOC field, and a matching PDF preview.
- [SlidevJS](skills/slidevjs/SKILL.md) - Create or update Slidev seminar decks using Alpha's academic theme, addon, project structure, and component guidance.

### Skill development

- [Skill Creator](.agents/skills/skill-creator/SKILL.md) - Create, revise, evaluate, and package reusable skills.

## Credits

- [Grilling](skills/grilling/SKILL.md) and [Grill Me](skills/grill-me/SKILL.md) are adapted from [Matt Pocock’s skills](https://github.com/mattpocock/skills/tree/main/skills/productivity), under MIT. These versions ask one question per turn; each skill includes attribution and the original license.

## Evaluations

Evaluation prompts describe realistic tasks and expected outcomes. They are scenarios for evaluating skill behavior, not proof that a skill has passed those scenarios. Some skills also include deterministic checks for specific outputs; those checks do not replace reviewing the resulting work.
