Alpha's Projects' skills for AI Agent.

This is a living repository of "Skills" (system instructions) designed to guide AI Agents (like Cursor, Claude Code, or Windsurf) to code exactly the way I want.

This repository reflects my personal standards. There is no absolute "right" or "wrong" here—only what works best for my projects. With an open mind, I am always learning from others, and this repository will evolve as I grow as a developer.

Each skill lives under `skills/<name>/SKILL.md`. Start with `AGENTS.md` for trigger rules, then read only the references relevant to the task. Evaluation prompts and expected outcomes live in each skill's `evals/evals.json`; Slidev cases include input project fixtures under `skills/slidevjs/evals/files/`.

Run `python3 scripts/validate_skills.py` after changing skills or evaluations. It checks skill metadata, local Markdown links, `AGENTS.md` skill paths, evaluation cases, and fixture paths. The evaluation prompts are scenarios to run against the original and revised skill on the same model; the validator does not measure model behavior.
