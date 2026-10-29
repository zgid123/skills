#!/usr/bin/env python3
"""Create disposable, fixed repository fixtures for paired skill behavior runs."""

import argparse
import os
import shutil
import subprocess
from pathlib import Path


EVALS = Path(__file__).resolve().parent
SEEDS = EVALS / "fixtures"


def git(root, *args, env=None):
    return subprocess.run(
        ["git", "-C", str(root), *args], check=True, text=True,
        capture_output=True, env=env, timeout=15,
    ).stdout.strip()


def commit_env(date):
    env = dict(os.environ)
    env.update({
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_AUTHOR_NAME": "SWE lifecycle eval",
        "GIT_AUTHOR_EMAIL": "eval@example.invalid",
        "GIT_COMMITTER_NAME": "SWE lifecycle eval",
        "GIT_COMMITTER_EMAIL": "eval@example.invalid",
        "GIT_AUTHOR_DATE": date,
        "GIT_COMMITTER_DATE": date,
    })
    return env


def prepare_history_fixture(root):
    docs = root / "docs"
    (docs / "specs/requirements").mkdir(parents=True)
    (docs / "changelog/foundation").mkdir(parents=True)
    (docs / "architecture").mkdir(parents=True)
    (docs / "decisions").mkdir(parents=True)
    (docs / "knowledge").mkdir(parents=True)
    (docs / "README.md").write_text(
        "# Documentation\n\n[Project](project.md)\n"
        "[Authentication requirement](specs/requirements/00003-authentication.md)\n",
        encoding="utf-8",
    )
    (docs / "project.md").write_text(
        '---\nowner: "Platform team"\nchangelog_policy: meaningful\nreserved_ids: []\n---\n\n'
        "# Token service\n\nAuthentication source is being maintained.\n",
        encoding="utf-8",
    )
    (docs / "specs/requirements/00003-authentication.md").write_text(
        '---\nid: "REQ-00003"\ntitle: "Authentication"\nstatus: approved\n'
        'owner: "Security team"\ncreated_at: "2026-09-01"\nupdated_at: "2026-09-01"\n'
        'dependencies: []\nrelated_changes: []\n---\n\n# Authentication\n\n'
        "## Overview\nValidate refresh credentials.\n\n## Functional requirements\n"
        "FR-001: Reject invalid credentials.\n\n## Acceptance criteria\n"
        "AC-001: Invalid refresh credentials are rejected.\n",
        encoding="utf-8",
    )
    (docs / "changelog/foundation/0001-auth-module.md").write_text(
        '---\nid: "LOG-foundation-0001"\ntitle: "Add authentication module"\n'
        'status: finalized\nowner: "Platform team"\ndate: "2026-09-02"\n'
        'type: feature\nrequirements: ["REQ-00003"]\nchanges: []\ndecisions: []\n'
        'github_issues: []\ngithub_prs: []\ncommit: null\ncomponents: ["src/old_auth.py"]\n---\n\n'
        "# Add authentication module\n\n## Summary\nAdd the authentication module.\n\n"
        "## Previous behavior\nAuthentication was not present.\n\n## New behavior\nRequests can validate refresh credentials.\n\n"
        "## Implementation details\nSource is [`src/old_auth.py`](../../../src/old_auth.py).\n\n"
        "## Tests and verification\nThe comparison helper accepts matching tokens.\n\n"
        "## Documentation updated\nAuthentication requirement added.\n",
        encoding="utf-8",
    )

    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "SWE lifecycle eval")
    git(root, "config", "user.email", "eval@example.invalid")
    git(root, "config", "commit.gpgsign", "false")
    git(root, "remote", "add", "origin", "https://github.com/example/token-service.git")
    git(root, "add", "--all")
    git(root, "commit", "-m", "Add initial authentication module", env=commit_env("2026-09-02T12:00:00+00:00"))
    original_commit = git(root, "rev-parse", "HEAD")

    git(root, "switch", "-c", "feature/audit-log")
    (docs / "README.md").write_text(
        "# Documentation\n\n[Project](project.md)\n"
        "[Authentication requirement](specs/requirements/00003-authentication.md)\n"
        "[Audit logging requirement](specs/requirements/00003-audit-logging.md)\n",
        encoding="utf-8",
    )
    (docs / "specs/requirements/00003-audit-logging.md").write_text(
        '---\nid: "REQ-00003"\ntitle: "Audit logging"\nstatus: draft\n'
        'owner: "Platform team"\ncreated_at: "2026-10-01"\nupdated_at: "2026-10-01"\n'
        'dependencies: []\nrelated_changes: []\n---\n\n# Audit logging\n\n'
        "## Overview\nRecord security-relevant actions.\n\n## Functional requirements\n"
        "FR-001: Record successful and failed authentication attempts.\n\n## Acceptance criteria\n"
        "AC-001: Each authentication attempt is associated with its timestamp and outcome.\n",
        encoding="utf-8",
    )
    (docs / "architecture/audit-logging.md").write_text(
        "# Audit logging design\n\n"
        "[Requirement](../specs/requirements/00003-audit-logging.md)\n",
        encoding="utf-8",
    )
    git(root, "add", "--all")
    git(root, "commit", "-m", "Draft audit logging requirement", env=commit_env("2026-10-01T13:00:00+00:00"))
    git(root, "switch", "main")
    git(root, "mv", "src/old_auth.py", "src/auth.py")
    git(root, "commit", "-m", "Rename authentication module", env=commit_env("2026-10-02T12:00:00+00:00"))
    (root / "FIXTURE_CONTEXT.md").write_text(
        f"The initial source revision is `{original_commit}`. The remote is a fixture value and must not be contacted.\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()
    output = args.output_root.resolve()
    output.mkdir(parents=True, exist_ok=True)
    names = ["tiny-bootstrap", "token-reuse-bug", "rate-limit-feature", "auth-migration", "history-and-id-collision"]
    for name in names:
        destination = output / name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(SEEDS / name, destination)
        if name == "history-and-id-collision":
            prepare_history_fixture(destination)
    print(output)


if __name__ == "__main__":
    main()
