"""House chart style for analytical reports (matplotlib).

Import and call the helpers, or run `python chart_style.py --demo out_dir` to see examples.

    import chart_style as cs
    cs.apply()
    fig, ax = cs.figure()
    cs.bar(ax, ["A", "B", "C"], [0.85, 0.26, 0.31], highlight="A", fmt="{:.0%}")
    cs.title(ax, "Missing work triples later risk", "Share later failing or withdrawing, n=5,903")
    cs.source(fig, "Source: OULAD, Oct 2014 presentations")
    cs.save(fig, "figures/risk_by_status")

Design rules encoded here: claim-style titles with a quieter subtitle, one accent colour
for the focus and greys for context, direct labels instead of legends, bars from zero,
minimal chrome, colour-blind-safe categorical palette, PNG + SVG export.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Sequence

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.dates as mdates  # noqa: E402

ACCENT = "#1f6f8b"
ACCENT_2 = "#d9822b"
NEUTRAL = "#9aa5b1"
NEUTRAL_DARK = "#52606d"
INK = "#1f2933"
GRID = "#e4e7eb"
# Okabe-Ito based, distinguishable for common colour-vision deficiencies.
CATEGORICAL = ["#1f6f8b", "#d9822b", "#2a9d8f", "#c44569", "#6c5b7b", "#8d99ae", "#e9c46a", "#264653"]


def apply() -> None:
    """Set global matplotlib defaults for the house style."""
    plt.rcParams.update(
        {
            "figure.dpi": 110,
            "savefig.dpi": 200,
            "font.size": 10.5,
            "font.family": "sans-serif",
            "font.sans-serif": ["Inter", "Helvetica Neue", "Arial", "DejaVu Sans"],
            "text.color": INK,
            "axes.labelcolor": NEUTRAL_DARK,
            "axes.edgecolor": NEUTRAL,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "axes.grid.axis": "y",
            "grid.color": GRID,
            "grid.linewidth": 0.8,
            "axes.axisbelow": True,
            "axes.titlelocation": "left",
            "axes.prop_cycle": matplotlib.cycler(color=CATEGORICAL),
            "xtick.color": NEUTRAL_DARK,
            "ytick.color": NEUTRAL_DARK,
            "legend.frameon": False,
        }
    )


def figure(width: float = 7.5, height: float = 4.2, **kwargs):
    """Create a figure and axes with room for a title, subtitle and source line."""
    fig, ax = plt.subplots(figsize=(width, height), **kwargs)
    fig.subplots_adjust(top=0.80, bottom=0.17)
    return fig, ax


def title(ax, claim: str, subtitle: str | None = None) -> None:
    """Claim as the title (bold), measure/population/period as the subtitle."""
    fig = ax.figure
    fig.text(0.02, 0.95, claim, ha="left", va="top", fontsize=13.5, fontweight="bold", color=INK)
    if subtitle:
        fig.text(0.02, 0.885, subtitle, ha="left", va="top", fontsize=10.5, color=NEUTRAL_DARK)


def source(fig, text: str) -> None:
    """Small source/population note at the bottom-left."""
    fig.text(0.02, 0.02, text, ha="left", va="bottom", fontsize=8.5, color=NEUTRAL_DARK)


def _colors(labels: Sequence[str], highlight: str | Iterable[str] | None) -> list[str]:
    if highlight is None:
        return [ACCENT] * len(labels)
    focus = {highlight} if isinstance(highlight, str) else set(highlight)
    return [ACCENT if label in focus else NEUTRAL for label in labels]


def bar(
    ax,
    labels: Sequence[str],
    values: Sequence[float],
    highlight: str | Iterable[str] | None = None,
    fmt: str = "{:,.0f}",
    horizontal: bool = True,
    sort: bool = True,
) -> None:
    """Sorted bar chart with direct labels; missing values remain visible as unavailable."""
    pairs = list(zip(labels, values))
    if sort:
        # Largest first, missing last; barh draws the first bar at the bottom, so reverse it.
        pairs.sort(key=lambda p: (not np.isfinite(p[1]), -p[1] if np.isfinite(p[1]) else 0))
        if horizontal:
            pairs.reverse()
    labels, values = [p[0] for p in pairs], [p[1] for p in pairs]
    colors = _colors(labels, highlight)
    positions = list(range(len(labels)))
    valid = [i for i, value in enumerate(values) if np.isfinite(value)]
    missing = [i for i, value in enumerate(values) if not np.isfinite(value)]
    span = max((abs(values[i]) for i in valid), default=0) or 1
    if horizontal:
        ax.barh([positions[i] for i in valid], [values[i] for i in valid], color=[colors[i] for i in valid], height=0.62)
        ax.set_yticks(positions, labels)
        ax.set_ylim(-0.5, len(labels) - 0.5)
        ax.grid(axis="y", visible=False)
        ax.grid(axis="x", visible=True)
        if valid:
            ax.set_xlim(min(0, min(values[i] for i in valid)) * 1.15, max(0, max(values[i] for i in valid)) * 1.15 or 1)
        else:
            ax.set_xlim(-1, 1)
        for i in valid:
            v = values[i]
            x = v
            ax.text(x + span * 0.01 * (1 if v >= 0 else -1), positions[i], fmt.format(v),
                    va="center", ha="left" if v >= 0 else "right", fontsize=9.5, color=INK)
        for i in missing:
            ax.text(0, positions[i], "Unavailable", va="center", ha="left", fontsize=9.5, color=NEUTRAL_DARK)
        ax.tick_params(axis="y", length=0)
    else:
        ax.bar([positions[i] for i in valid], [values[i] for i in valid], color=[colors[i] for i in valid], width=0.62)
        ax.set_xticks(positions, labels)
        ax.set_xlim(-0.5, len(labels) - 0.5)
        if valid:
            ax.set_ylim(min(0, min(values[i] for i in valid)) * 1.15, max(0, max(values[i] for i in valid)) * 1.15 or 1)
        else:
            ax.set_ylim(-1, 1)
        for i in valid:
            v = values[i]
            ax.text(positions[i], v + span * 0.01 * (1 if v >= 0 else -1), fmt.format(v),
                    ha="center", va="bottom" if v >= 0 else "top", fontsize=9.5, color=INK)
        for i in missing:
            ax.text(positions[i], 0, "Unavailable", ha="center", va="bottom", fontsize=9.5, color=NEUTRAL_DARK)
        ax.tick_params(axis="x", length=0)
    ax.axhline(0, color=NEUTRAL, linewidth=0.8) if not horizontal else ax.axvline(0, color=NEUTRAL, linewidth=0.8)


def lines(ax, x: Sequence, series: dict[str, Sequence[float]], highlight: str | None = None, fmt: str = "{:.2f}") -> None:
    """Line chart with labels at the line ends instead of a legend; labels that would overlap are pushed apart."""
    if len(x) == 0:
        raise ValueError("x must contain at least one point")
    if any(hasattr(value, "year") and hasattr(value, "month") for value in x):
        locator = mdates.AutoDateLocator(minticks=3, maxticks=6)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    ends = []
    for i, (name, ys) in enumerate(series.items()):
        if len(ys) != len(x):
            raise ValueError(f"series {name!r} must have the same number of values as x")
        if highlight is None:
            color, lw, z = CATEGORICAL[i % len(CATEGORICAL)], 2.2, 3
        else:
            color, lw, z = (ACCENT, 2.6, 4) if name == highlight else (NEUTRAL, 1.6, 2)
        ax.plot(x, ys, color=color, linewidth=lw, marker="o", markersize=4, zorder=z)
        last = list(ys)[-1]
        if last is not None and np.isfinite(last):
            ends.append((name, last, color))
    ax.margins(x=0.02)
    ax.set_xlim(right=ax.get_xlim()[1] + (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.22)

    # Work in points (1/72 inch) so the minimum gap is the same at any figure size or dpi.
    to_pt = 72 / ax.figure.dpi
    ymin_pt, ymax_pt = (v * to_pt for v in sorted(ax.transAxes.transform([(0, 0), (0, 1)])[:, 1]))
    labels = sorted(
        (
            {
                "name": n,
                "value": v,
                "color": c,
                "y0": ax.transData.transform((ax.convert_xunits(x[-1]), ax.convert_yunits(v)))[1] * to_pt,
            }
            for n, v, c in ends
        ),
        key=lambda d: d["y0"],
    )
    gap = 9.5 * 1.35
    for i, lab in enumerate(labels):
        lab["y"] = max(lab["y0"], ymin_pt if i == 0 else labels[i - 1]["y"] + gap)
    for i in range(len(labels) - 1, -1, -1):
        labels[i]["y"] = min(labels[i]["y"], ymax_pt if i == len(labels) - 1 else labels[i + 1]["y"] - gap)
    for lab in labels:
        moved = abs(lab["y"] - lab["y0"]) > 1
        ax.annotate(f"{lab['name']}  {fmt.format(lab['value'])}", (x[-1], lab["value"]),
                    xytext=(8, lab["y"] - lab["y0"]), textcoords="offset points", va="center", fontsize=9.5,
                    color=lab["color"], fontweight="bold" if lab["name"] == highlight else "normal",
                    arrowprops=dict(arrowstyle="-", color=lab["color"], lw=0.8, shrinkA=0, shrinkB=3) if moved else None)


def intervals(ax, labels: Sequence[str], estimates: Sequence[float], lows: Sequence[float], highs: Sequence[float],
              highlight: str | Iterable[str] | None = None, fmt: str = "{:.2f}", reference: float | None = 0.0) -> None:
    """Dot-and-interval plot (estimates with confidence intervals), optional reference line."""
    colors = _colors(labels, highlight)
    ys = list(range(len(labels)))[::-1]
    for y, est, lo, hi, c in zip(ys, estimates, lows, highs, colors):
        if not all(np.isfinite(value) for value in (est, lo, hi)):
            ax.text(0.98, y, "Unavailable", transform=ax.get_yaxis_transform(), ha="right", va="center", color=NEUTRAL_DARK)
            continue
        ax.plot([lo, hi], [y, y], color=c, linewidth=2.2, solid_capstyle="round")
        ax.plot(est, y, "o", color=c, markersize=7)
        ax.annotate(fmt.format(est), (hi, y), xytext=(6, 0), textcoords="offset points", va="center", fontsize=9.5)
    ax.set_yticks(ys, labels)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", visible=True)
    if reference is not None:
        ax.axvline(reference, color=NEUTRAL_DARK, linewidth=1, linestyle="--")


def dumbbell(ax, labels: Sequence[str], before: Sequence[float], after: Sequence[float],
             names: tuple[str, str] = ("Before", "After"), fmt: str = "{:.0%}") -> None:
    """Paired before/after dots per group, connected by a line."""
    ys = list(range(len(labels)))[::-1]
    for y, b, a in zip(ys, before, after):
        ax.plot([b, a], [y, y], color=GRID, linewidth=3, zorder=1)
        ax.plot(b, y, "o", color=NEUTRAL, markersize=8, zorder=2)
        ax.plot(a, y, "o", color=ACCENT, markersize=8, zorder=3)
        ax.annotate(fmt.format(a), (a, y), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=9, color=ACCENT)
    ax.set_yticks(ys, labels)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", visible=True)
    ax.plot([], [], "o", color=NEUTRAL, label=names[0])
    ax.plot([], [], "o", color=ACCENT, label=names[1])
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 1.0), ncol=2, fontsize=9)
    ax.set_ylim(-0.6, len(labels) - 0.4)


def percent_axis(ax, axis: str = "x", decimals: int = 0) -> None:
    """Format an axis holding 0–1 proportions as percentages."""
    from matplotlib.ticker import PercentFormatter

    (ax.xaxis if axis == "x" else ax.yaxis).set_major_formatter(PercentFormatter(1.0, decimals=decimals))


def save(fig, path_stem: str | Path) -> tuple[Path, Path]:
    """Save PNG (for the report) and SVG (for reuse); returns both paths."""
    stem = Path(path_stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    png, svg = stem.with_suffix(".png"), stem.with_suffix(".svg")
    fig.savefig(png, bbox_inches="tight", facecolor="white")
    fig.savefig(svg, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return png, svg


def _demo(out: Path) -> None:
    apply()
    fig, ax = figure()
    bar(ax, ["AAA", "BBB", "DDD", "EEE", "FFF"], [0.50, 0.87, 0.94, 0.96, 0.89], highlight="BBB", fmt="{:.0%}")
    percent_axis(ax)
    title(ax, "Missing work signals risk in every course", "Share later failing or withdrawing among students with a missed assignment by day 60")
    source(fig, "Illustrative data")
    save(fig, out / "demo_bar")

    fig, ax = figure()
    lines(ax, [30, 60, 90], {"Behaviour": [0.49, 0.65, 0.65], "Scores": [0.39, 0.45, 0.57], "Base rate": [0.35, 0.33, 0.31]},
          highlight="Behaviour")
    ax.set_xticks([30, 60, 90])
    ax.set_xlabel("Days after course start")
    title(ax, "Behaviour beats scores until day 90", "Average precision on the later cohort")
    source(fig, "Illustrative data")
    save(fig, out / "demo_lines")

    fig, ax = figure()
    intervals(ax, ["Day 30", "Day 60", "Day 90"], [-0.045, -0.06, 0.031], [-0.059, -0.078, 0.016], [-0.03, -0.043, 0.049],
              highlight=["Day 90"], fmt="{:+.3f}")
    title(ax, "Adding scores only helps by day 90", "Combined minus behaviour-only AP, 95% bootstrap interval")
    source(fig, "Illustrative data")
    save(fig, out / "demo_intervals")

    fig, ax = figure()
    dumbbell(ax, ["Web", "iOS", "Android"], [0.024, 0.033, 0.031], [0.024, 0.032, 0.019], fmt="{:.1%}")
    percent_axis(ax, decimals=1)
    title(ax, "Only Android conversion fell", "Checkout conversion, 1–21 Sep vs 22 Sep–12 Oct")
    source(fig, "Illustrative data")
    save(fig, out / "demo_dumbbell")
    print(f"Wrote demo charts to {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--demo", metavar="OUT_DIR", help="write example charts to OUT_DIR")
    args = parser.parse_args()
    if args.demo:
        _demo(Path(args.demo))
    else:
        parser.print_help()
