"""Benchmark clustered bootstrap runtime on a fixed synthetic workload."""

from __future__ import annotations

import json
import platform
import statistics
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "skills" / "data-analyst" / "scripts"))
import stats_helpers as stats  # noqa: E402


CLUSTERS = 3_000
ROWS_PER_CLUSTER = 2
REPLICATES = 200
RUNS = 3
LIMIT_SECONDS = 10.0


def main() -> int:
    cluster_id = np.repeat(np.arange(CLUSTERS), ROWS_PER_CLUSTER)
    values = (cluster_id % 97).astype(float) + np.tile([0.0, 1.0], CLUSTERS)
    data = pd.DataFrame({"cluster_id": cluster_id, "value": values})
    timings = {}

    for mode, extra_column in (("source_ids", None), ("distinct_draw_ids", "bootstrap_id")):
        samples = []
        for seed in range(RUNS):
            started = time.perf_counter()
            stats.bootstrap_ci(
                data,
                lambda sample: sample["value"].mean(),
                cluster="cluster_id",
                n_boot=REPLICATES,
                seed=seed,
                bootstrap_cluster_col=extra_column,
            )
            samples.append(time.perf_counter() - started)
        timings[mode] = {
            "seconds": [round(value, 3) for value in samples],
            "median_seconds": round(statistics.median(samples), 3),
            "limit_seconds": LIMIT_SECONDS,
        }

    result = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "clusters": CLUSTERS,
        "rows_per_cluster": ROWS_PER_CLUSTER,
        "replicates": REPLICATES,
        "runs_per_mode": RUNS,
        "timings": timings,
    }
    print(json.dumps(result, indent=2))
    return int(any(value["median_seconds"] >= LIMIT_SECONDS for value in timings.values()))


if __name__ == "__main__":
    raise SystemExit(main())
