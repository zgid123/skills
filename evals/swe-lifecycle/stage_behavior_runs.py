#!/usr/bin/env python3
"""Stage isolated, identical repository snapshots for paired lifecycle eval runs."""

import json
import shutil
import subprocess
import sys
from pathlib import Path


EVALS = Path(__file__).resolve().parent
SKILL_ROOT = EVALS.parents[1] / "skills" / "swe-lifecycle"
WORKSPACE = SKILL_ROOT.parent / "swe-lifecycle-workspace" / "iteration-1"
SEEDS = Path("/tmp/swe-lifecycle-eval-seeds")


def main():
    subprocess.run([sys.executable, str(EVALS / "prepare_fixtures.py"), str(SEEDS)], check=True)
    eval_data = json.loads((EVALS / "evals.json").read_text(encoding="utf-8"))
    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)
    WORKSPACE.mkdir(parents=True)
    (WORKSPACE / "README.md").write_text(
        "# SWE lifecycle behavioral evaluation — iteration 1\n\n"
        "Each task has isolated with-skill and baseline working repositories copied from the same prepared fixture. "
        "No run has permission to contact GitHub or any remote. Outputs contain the run report and final repository snapshot.\n",
        encoding="utf-8",
    )
    seed_names = {
        1: "tiny-bootstrap", 2: "token-reuse-bug", 3: "rate-limit-feature",
        4: "auth-migration", 5: "history-and-id-collision",
    }
    for evaluation in eval_data["evals"]:
        name = evaluation["name"]
        directory = WORKSPACE / f"eval-{evaluation['id']}-{name}"
        directory.mkdir()
        metadata = {
            "eval_id": evaluation["id"],
            "eval_name": name,
            "prompt": evaluation["prompt"],
            "assertions": evaluation["expectations"],
        }
        (directory / "eval_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        seed = SEEDS / seed_names[evaluation["id"]]
        for configuration in ("with_skill", "without_skill"):
            run_dir = directory / configuration / "run-1"
            (run_dir / "outputs").mkdir(parents=True)
            shutil.copytree(seed, run_dir / "repo")
    print(WORKSPACE)


if __name__ == "__main__":
    main()
