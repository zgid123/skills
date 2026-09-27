"""Check the structure and local references of this repository's skills."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def validate() -> list[str]:
    errors: list[str] = []
    names: set[str] = set()

    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        content = skill_file.read_text()
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
        if frontmatter is None:
            errors.append(f"{skill_file}: missing frontmatter")
            continue

        fields = dict(re.findall(r"^(name|description):\s*(.+)$", frontmatter.group(1), re.MULTILINE))
        name = fields.get("name")
        if name != skill_file.parent.name or not fields.get("description"):
            errors.append(f"{skill_file}: name must match directory and description must be present")
        if name in names:
            errors.append(f"{skill_file}: duplicate skill name {name}")
        names.add(name)

        eval_file = skill_file.parent / "evals/evals.json"
        if not eval_file.exists():
            errors.append(f"{eval_file}: missing evaluation cases")
            continue
        try:
            evals = json.loads(eval_file.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"{eval_file}: invalid JSON: {exc}")
            continue
        if evals.get("skill_name") != name:
            errors.append(f"{eval_file}: skill_name must match frontmatter")
        if not evals.get("evals"):
            errors.append(f"{eval_file}: add at least one evaluation case")
        ids: set[int] = set()
        for case in evals.get("evals", []):
            case_id = case.get("id")
            if not isinstance(case_id, int) or case_id in ids:
                errors.append(f"{eval_file}: IDs must be unique integers")
            ids.add(case_id)
            if not case.get("prompt") or not case.get("expected_output"):
                errors.append(f"{eval_file}: case {case_id} needs a prompt and expected output")
            if not case.get("expectations"):
                errors.append(f"{eval_file}: case {case_id} needs verifiable expectations")
            for fixture in case.get("files", []):
                if not (skill_file.parent / fixture).exists():
                    errors.append(f"{eval_file}: missing fixture {fixture}")

    for markdown in SKILLS.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", markdown.read_text()):
            if target.startswith(("https:", "http:", "#", "mailto:")):
                continue
            if not (markdown.parent / target.split("#", 1)[0]).exists():
                errors.append(f"{markdown}: broken link {target}")

    agents = (ROOT / "AGENTS.md").read_text()
    for target in re.findall(r"`(skills/[^`]+/SKILL\.md)`", agents):
        if "<" in target or ">" in target:
            continue
        if not (ROOT / target).exists():
            errors.append(f"AGENTS.md: missing skill {target}")

    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print(problem)
    print(f"{len(problems)} issue(s) found")
    raise SystemExit(bool(problems))
