# Local validator tests and lifecycle behavior evaluation

Run the deterministic validator suite from the repository root:

```sh
python3 -m unittest discover -s evals/swe-lifecycle -p 'test_*.py' -v
```

The tests create isolated temporary projects, exercise the validator API and its CLI from an unrelated working directory, and remove their fixtures afterward. They need Python's standard library and Git; they make no GitHub requests. The checkout test disables system/global Git configuration, hooks, and commit signing. Positive fixtures cover sparse documentation, a designed feature, migration with ADR supersession, a bug record, and requirement evolution. Negative fixtures exercise malformed metadata, IDs, status, dates, filenames, references, supersession, sections, and links.

These tests establish validator behavior. Constructed documentation fixtures do not establish that an agent follows discovery, approval, implementation, or GitHub workflows correctly.

## Evaluate agent behavior

`evals.json` defines five realistic tasks: tiny-project bootstrap, a routine defect repair, an already-approved feature, a migration awaiting approval, and source-history/ID-collision maintenance. The task prompts do not prescribe lifecycle artifacts. Each with-skill and baseline run must start from a byte-identical repository snapshot and the same user authorization. The with-skill run receives the installed skill path; the baseline does not receive lifecycle instructions. Use isolated working copies, with GitHub disconnected and no real remote writes. Preserve each starting snapshot, final files, command/test output, and any Git history used by the scenario. Preserve full transcripts when the execution environment exposes them; otherwise retain the runner's report and state that the transcript was unavailable.

For a benchmark, run each prompt with and without this skill against identical repository snapshots. Grade each expectation against a file path, output, or transcript excerpt; record failures and pending steps explicitly. Treat fabricated verification, unauthorized changes, loss of historical meaning, and broken implementation as critical failures. Score documentation usefulness and unnecessary interruptions separately from correctness; do not reward document count. Compare paired outputs qualitatively as well as by expectation pass rate. Do not credit invented issue URLs or revision identifiers. One run per prompt is an exploratory comparison, not a stable statistical estimate. Human review remains necessary for requirement quality, useful historical detail, and appropriate scope.

`prepare_fixtures.py` builds the fixed repositories. It creates a real local Git history and an unmerged feature branch for the maintenance scenario; its configured remote is fixture-only and must never be contacted. `stage_behavior_runs.py` copies identical snapshots into `skills/swe-lifecycle-workspace/iteration-1/` (relative to the repository root). Each runner edits only its assigned `repo/` and saves its report under that run's `outputs/` directory. Keep the task prompt and authorization identical across each pair; the only difference is access to `skills/swe-lifecycle/SKILL.md` and its references.

The deterministic suite covers validator behavior only. It is not evidence that the lifecycle workflow improves agent behavior; report behavioral results only after paired runs have actually completed.
