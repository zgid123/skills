"""Small, dependency-light statistics helpers for analyst work.

Import what you need:

    from stats_helpers import wilson_ci, diff_proportions_ci, bootstrap_ci, capacity_table, calibration_table

Every function documents its population and assumptions. These cover common analyst needs;
for complex designs (survey replicate weights, mixed models) follow the data's documentation.
Run `python stats_helpers.py --selftest` to check the functions.
"""

from __future__ import annotations

import argparse
import math
from numbers import Integral, Real
from typing import Callable, Sequence

import numpy as np
import pandas as pd

Z95 = 1.959963984540054


def wilson_ci(k: int, n: int, z: float = Z95) -> tuple[float, float, float]:
    """Proportion k/n with a Wilson score interval; NaNs when the valid count n is zero."""
    def count(value: int, name: str) -> int:
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer count")
        if isinstance(value, Integral):
            result = int(value)
        elif isinstance(value, Real):
            number = float(value)
            if not math.isfinite(number) or not number.is_integer():
                raise ValueError(f"{name} must be a finite whole-number count")
            result = int(number)
        else:
            raise TypeError(f"{name} must be an integer count")
        if result < 0:
            raise ValueError(f"{name} cannot be negative")
        return result

    k, n = count(k, "k"), count(n, "n")
    if k > n:
        raise ValueError("k cannot exceed n")
    if isinstance(z, bool) or not isinstance(z, Real):
        raise TypeError("z must be a finite positive number")
    z = float(z)
    if not math.isfinite(z) or z <= 0:
        raise ValueError("z must be a finite positive number")
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p = k / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (p, max(0.0, centre - half), min(1.0, centre + half))


def diff_proportions_ci(k1: int, n1: int, k2: int, n2: int, z: float = Z95) -> tuple[float, float, float]:
    """Difference p1 - p2 of two independent proportions with Newcombe's hybrid score interval.

    Returns (difference, low, high). Assumes independent groups and independent units; for
    paired or clustered data use bootstrap_ci with a cluster key instead.
    """
    p1, l1, u1 = wilson_ci(k1, n1, z)
    p2, l2, u2 = wilson_ci(k2, n2, z)
    d = p1 - p2
    low = d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    high = d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (d, low, high)


def bootstrap_ci(
    data: pd.DataFrame,
    statistic: Callable[[pd.DataFrame], float],
    n_boot: int = 1000,
    seed: int = 0,
    cluster: str | None = None,
    level: float = 0.95,
    bootstrap_cluster_col: str | None = None,
) -> tuple[float, float, float]:
    """Percentile bootstrap interval for any statistic of a DataFrame.

    `cluster` resamples whole groups (e.g., student_id) so repeated rows of one entity stay
    together. By default, source IDs remain unchanged and repeated draws share their source ID.
    Set `bootstrap_cluster_col` to give each draw a distinct ID while preserving the source ID;
    the same additional column is supplied to the callback for the original-data estimate.
    Returns (estimate on full data, low, high). The interval reflects sampling variability of
    the evaluated rows only — not model-training or selection uncertainty.
    """
    if not isinstance(data, pd.DataFrame) or data.empty:
        raise ValueError("data must be a non-empty DataFrame")
    if not callable(statistic):
        raise TypeError("statistic must be callable")
    if isinstance(n_boot, bool) or not isinstance(n_boot, Integral) or n_boot < 1:
        raise ValueError("n_boot must be a positive integer")
    if not math.isfinite(level) or not 0 < level < 1:
        raise ValueError("level must be between 0 and 1")
    if cluster is not None:
        if cluster not in data.columns:
            raise ValueError(f"cluster column {cluster!r} is missing")
        if data[cluster].isna().any():
            raise ValueError(f"cluster column {cluster!r} contains missing values")
    if bootstrap_cluster_col is not None:
        if cluster is None:
            raise ValueError("bootstrap_cluster_col requires cluster")
        if not bootstrap_cluster_col or bootstrap_cluster_col in data.columns:
            raise ValueError("bootstrap_cluster_col must be a new, non-empty column name")

    def evaluate(sample: pd.DataFrame, label: str) -> float:
        value = float(statistic(sample))
        if not math.isfinite(value):
            raise ValueError(f"statistic returned a non-finite value for {label}")
        return value

    rng = np.random.default_rng(seed)
    if bootstrap_cluster_col is None:
        original = data
    else:
        original = data.copy()
        original.insert(
            len(original.columns),
            bootstrap_cluster_col,
            pd.factorize(data[cluster], sort=False)[0],
        )
    estimate = evaluate(original, "the original data")
    stats = np.empty(n_boot)
    if cluster is None:
        n = len(data)
        for i in range(n_boot):
            stats[i] = evaluate(data.iloc[rng.integers(0, n, n)], f"bootstrap replicate {i + 1}")
    else:
        groups = {key: idx for key, idx in data.groupby(cluster).indices.items()}
        keys = list(groups)
        for i in range(n_boot):
            chosen = [keys[index] for index in rng.integers(0, len(keys), len(keys))]
            source_indices = [groups[key] for key in chosen]
            rows = np.concatenate(source_indices)
            sample = data.iloc[rows]
            if bootstrap_cluster_col is not None:
                draw_ids = np.repeat(np.arange(len(chosen)), [len(idx) for idx in source_indices])
                sample.insert(len(sample.columns), bootstrap_cluster_col, draw_ids)
            stats[i] = evaluate(sample, f"bootstrap replicate {i + 1}")
    alpha = (1 - level) / 2
    low, high = np.quantile(stats, [alpha, 1 - alpha])
    return (estimate, float(low), float(high))


def capacity_table(
    y_true: Sequence[int],
    score: Sequence[float],
    capacities: Sequence[float] = (0.1, 0.2, 0.3),
    thresholds: dict[float, float] | None = None,
) -> pd.DataFrame:
    """Review-workload view of a risk score.

    For each capacity c, flag the top c share of entities by score (or use a pre-set
    threshold per capacity, e.g., chosen on validation data, via `thresholds`). Returns
    flagged count, alert rate, precision, recall, true/false positives and missed positives.
    Ties at the threshold can push the alert rate above the capacity; that is reported, not hidden.
    """
    y = np.asarray(y_true)
    s = np.asarray(score, dtype=float)
    if y.ndim != 1 or s.ndim != 1 or len(y) != len(s):
        raise ValueError("y_true and score must be one-dimensional arrays of equal length")
    if len(y) == 0:
        raise ValueError("y_true and score must contain at least one observation")
    if not np.isin(y, [0, 1]).all():
        raise ValueError("y_true values must be binary 0/1 labels")
    if not np.isfinite(s).all():
        raise ValueError("score values must be finite")
    y = y.astype(int)
    if len(capacities) == 0:
        raise ValueError("capacities must contain at least one value")
    if any(not math.isfinite(c) or not 0 <= c <= 1 for c in capacities):
        raise ValueError("capacities must be finite values between 0 and 1")
    if thresholds is not None:
        missing = set(capacities) - set(thresholds)
        if missing:
            raise ValueError(f"thresholds are missing capacities: {sorted(missing)}")
        if any(not math.isfinite(value) for value in thresholds.values()):
            raise ValueError("threshold values must be finite")
    n, positives = len(y), int(y.sum())
    rows = []
    for c in capacities:
        if c == 0:
            thr = None
            flagged = np.zeros(n, dtype=bool)
        elif thresholds is not None:
            thr = thresholds[c]
            flagged = s >= thr
        else:
            k = max(1, int(round(c * n)))
            thr = float(np.sort(s)[::-1][k - 1])
            flagged = s >= thr
        tp = int((flagged & (y == 1)).sum())
        fp = int((flagged & (y == 0)).sum())
        fn = positives - tp
        nf = int(flagged.sum())
        rows.append(
            {
                "capacity": c,
                "threshold": thr,
                "flagged": nf,
                "alert_rate": nf / n if n else math.nan,
                "precision": tp / nf if nf else math.nan,
                "recall": tp / positives if positives else math.nan,
                "true_positives": tp,
                "false_positives": fp,
                "missed_positives": fn,
                "n": n,
                "prevalence": positives / n if n else math.nan,
            }
        )
    return pd.DataFrame(rows)


def calibration_table(y_true: Sequence[int], prob: Sequence[float], bins: Sequence[float] = (0, 0.2, 0.4, 0.6, 0.8, 1.0)) -> pd.DataFrame:
    """Mean predicted vs observed outcome rate per fixed probability bin, with Wilson intervals."""
    y = np.asarray(y_true)
    p = np.asarray(prob, dtype=float)
    if y.ndim != 1 or p.ndim != 1 or len(y) != len(p):
        raise ValueError("y_true and prob must be one-dimensional arrays of equal length")
    if len(y) == 0:
        raise ValueError("y_true and prob must contain at least one observation")
    if not np.isin(y, [0, 1]).all():
        raise ValueError("y_true values must be binary 0/1 labels")
    if not np.isfinite(p).all() or ((p < 0) | (p > 1)).any():
        raise ValueError("prob values must be finite and between 0 and 1")
    if len(bins) < 2 or any(not math.isfinite(edge) for edge in bins) or any(a >= b for a, b in zip(bins, bins[1:])):
        raise ValueError("bins must be finite and strictly increasing")
    if p.min() < bins[0] or p.max() > bins[-1]:
        raise ValueError("bins must cover every probability")
    df = pd.DataFrame({"y": y.astype(int), "p": p})
    df["bin"] = pd.cut(df["p"], bins=list(bins), include_lowest=True)
    rows = []
    for b, g in df.groupby("bin", observed=True):
        k, n = int(g["y"].sum()), len(g)
        obs, lo, hi = wilson_ci(k, n)
        rows.append({"bin": str(b), "n": n, "mean_predicted": g["p"].mean(), "observed": obs, "observed_low": lo, "observed_high": hi})
    return pd.DataFrame(rows)


def weighted_share(indicator: Sequence[float], weights: Sequence[float]) -> tuple[float, int, float]:
    """Weighted share of a 0/1 indicator over valid (non-missing) responses.

    Returns (weighted share, valid unweighted n, sum of weights). This is a point estimate only:
    design-correct standard errors need the survey's replicate weights or strata/cluster
    information (see playbooks/survey-analysis.md).
    """
    x = np.asarray(indicator, dtype=float)
    w = np.asarray(weights, dtype=float)
    if x.ndim != 1 or w.ndim != 1 or len(x) != len(w):
        raise ValueError("indicator and weights must be one-dimensional arrays of equal length")
    if not np.isfinite(x[~np.isnan(x)]).all() or not np.isin(x[~np.isnan(x)], [0, 1]).all():
        raise ValueError("non-missing indicator values must be binary 0/1")
    if not np.isfinite(w[~np.isnan(w)]).all() or (w[~np.isnan(w)] < 0).any():
        raise ValueError("non-missing weights must be finite and non-negative")
    ok = ~np.isnan(x) & ~np.isnan(w)
    if not ok.any():
        return (math.nan, 0, 0.0)
    total_weight = float(np.sum(w[ok]))
    if total_weight == 0:
        return (math.nan, int(ok.sum()), 0.0)
    return (float(np.sum(x[ok] * w[ok]) / total_weight), int(ok.sum()), total_weight)


def replicate_se(full_estimate: float, replicate_estimates: Sequence[float], method: str = "fay", fay_k: float = 0.5) -> float:
    """Standard error from replicate-weight estimates.

    method="fay": Fay's BRR (PISA/TALIS use k=0.5 with 80 replicates):
        SE = sqrt( sum((theta_r - theta)^2) / (R * (1 - k)^2) )
    method="jk2": paired jackknife: SE = sqrt( sum((theta_r - theta)^2) ).
    Check the dataset's technical report for the right method and constants.
    """
    r = np.asarray(replicate_estimates, dtype=float)
    if r.ndim != 1 or len(r) == 0 or not np.isfinite(r).all() or not math.isfinite(full_estimate):
        raise ValueError("full and replicate estimates must be finite, with at least one replicate")
    sq = np.sum((r - full_estimate) ** 2)
    if method == "fay":
        if not math.isfinite(fay_k) or not 0 <= fay_k < 1:
            raise ValueError("fay_k must be between 0 and 1")
        return float(math.sqrt(sq / (len(r) * (1 - fay_k) ** 2)))
    if method == "jk2":
        return float(math.sqrt(sq))
    raise ValueError(f"unknown method {method!r}")


def _selftest() -> None:
    p, lo, hi = wilson_ci(8, 10)
    assert abs(p - 0.8) < 1e-12 and 0.49 < lo < 0.50 and 0.94 < hi < 0.95, (p, lo, hi)
    assert all(math.isnan(v) for v in wilson_ci(0, 0))
    d, lo, hi = diff_proportions_ci(56, 70, 48, 80)
    assert abs(d - 0.2) < 1e-12 and lo < d < hi and 0.05 < lo < 0.06 and 0.33 < hi < 0.34, (d, lo, hi)
    df = pd.DataFrame({"g": [1, 1, 2, 2, 3, 3], "x": [1, 2, 3, 4, 5, 6]})
    est, lo, hi = bootstrap_ci(df, lambda d: d["x"].mean(), n_boot=200, seed=1, cluster="g")
    assert est == 3.5 and lo <= est <= hi
    t = capacity_table([1, 1, 0, 0, 0, 1, 0, 0, 0, 0], [0.9, 0.8, 0.7, 0.1, 0.2, 0.3, 0.05, 0.15, 0.25, 0.35], [0.2, 0.5])
    assert t.loc[0, "flagged"] == 2 and t.loc[0, "precision"] == 1.0 and abs(t.loc[0, "recall"] - 2 / 3) < 1e-12
    assert t.loc[1, "missed_positives"] == 0
    c = calibration_table([0, 1, 1, 0], [0.1, 0.9, 0.7, 0.3], bins=(0, 0.5, 1))
    assert list(c["n"]) == [2, 2] and list(c["observed"]) == [0.0, 1.0]
    s, n, _ = weighted_share([1, 0, np.nan, 1], [2, 1, 5, 1])
    assert abs(s - 0.75) < 1e-12 and n == 3
    assert abs(replicate_se(0.5, [0.6, 0.4], "fay") - math.sqrt(0.02 / (2 * 0.25))) < 1e-12
    print("stats_helpers self-test passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--selftest", action="store_true", help="run built-in checks")
    if parser.parse_args().selftest:
        _selftest()
    else:
        parser.print_help()
