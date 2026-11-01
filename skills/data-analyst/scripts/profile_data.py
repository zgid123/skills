"""Fast first look at tabular files: shape, types, nulls, distinct counts, examples, candidate keys.

Usage:
    python profile_data.py data/*.csv                     # Markdown to stdout
    python profile_data.py big.csv --nrows 200000 -o notes/profile.md
    python profile_data.py table.parquet --max-cols 80

A profile shows fitness for use; it is not an analysis. Use it to decide what to inspect next:
column meanings still need the data dictionary and real records. With --nrows, counts describe
the first N rows only, which may not be representative of the full file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd


def read_table(path: Path, nrows: int | None) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".parquet":
        df = pd.read_parquet(path)
        return df.head(nrows) if nrows else df
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, nrows=nrows)
    sep = "\t" if suffix in {".tsv", ".tab"} else ","
    return pd.read_csv(path, sep=sep, nrows=nrows, low_memory=False)


def _fmt(value) -> str:
    text = str(value).replace("|", "\\|").replace("\n", " ")
    return text if len(text) <= 40 else text[:37] + "..."


def column_summary(s: pd.Series) -> dict:
    n = len(s)
    nulls = int(s.isna().sum())
    non_null = s.dropna()
    distinct = int(non_null.nunique())
    info = {
        "column": s.name,
        "dtype": str(s.dtype),
        "null %": f"{nulls / n:.1%}" if n else "—",
        "distinct": f"{distinct:,}",
        "summary": "",
    }
    if non_null.empty:
        info["summary"] = "all null"
    elif pd.api.types.is_numeric_dtype(s) and not pd.api.types.is_bool_dtype(s):
        q = non_null.quantile([0, 0.5, 1])
        zeros = (non_null == 0).mean()
        info["summary"] = f"min {q.iloc[0]:,.4g} · median {q.iloc[1]:,.4g} · max {q.iloc[2]:,.4g}" + (f" · zeros {zeros:.0%}" if zeros >= 0.05 else "")
    else:
        top = non_null.astype(str).value_counts().head(3)
        info["summary"] = ", ".join(f"{_fmt(k)} ({v / len(non_null):.0%})" for k, v in top.items())
        if distinct > 3 and non_null.astype(str).str.match(r"^\d{4}-\d{2}-\d{2}").mean() > 0.9:
            info["summary"] += f" · range {_fmt(non_null.min())} → {_fmt(non_null.max())}"
    return info


def candidate_keys(df: pd.DataFrame, limit: int = 5) -> list[str]:
    """Single columns, then pairs, then triples that are unique and non-null in the rows read."""
    from itertools import combinations

    n = len(df)
    singles = [c for c in df.columns if df[c].notna().all() and df[c].nunique() == n]
    if singles:
        return [f"`{c}`" for c in singles[:limit]]
    cols = [c for c in df.columns if df[c].notna().all() and 1 < df[c].nunique() < n]
    for size, max_cols in ((2, 25), (3, 12)):
        found = []
        for combo in combinations(cols[:max_cols], size):
            if not df.duplicated(list(combo)).any():
                found.append(" + ".join(f"`{c}`" for c in combo))
                if len(found) >= limit:
                    return found
        if found:
            return found
    return []


def profile(path: Path, nrows: int | None, max_cols: int) -> str:
    df = read_table(path, nrows)
    lines = [f"## {path.name}", ""]
    scope = f"first {len(df):,} rows (sampled with --nrows)" if nrows and len(df) >= nrows else f"{len(df):,} rows"
    lines.append(f"- Rows read: {scope}; columns: {df.shape[1]}")
    dup = int(df.duplicated().sum())
    lines.append(f"- Exact duplicate rows: {dup:,}" + (" — check whether these are true duplicates or legitimate repeats" if dup else ""))
    keys = candidate_keys(df)
    lines.append(f"- Candidate keys (unique, non-null here): {', '.join(keys) if keys else 'none found among single columns or pairs'}")
    lines.append("")
    lines.append("| Column | Type | Null % | Distinct | Values |")
    lines.append("| --- | --- | --- | --- | --- |")
    for col in df.columns[:max_cols]:
        info = column_summary(df[col])
        lines.append(f"| `{_fmt(info['column'])}` | {info['dtype']} | {info['null %']} | {info['distinct']} | {info['summary']} |")
    if df.shape[1] > max_cols:
        lines.append(f"\n_{df.shape[1] - max_cols} more columns not shown (raise --max-cols)._")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", type=Path, help="CSV, TSV, Parquet or Excel files")
    parser.add_argument("--nrows", type=int, default=None, help="read only the first N rows of each file")
    parser.add_argument("--max-cols", type=int, default=60, help="maximum columns to list per file")
    parser.add_argument("-o", "--output", type=Path, help="write Markdown here instead of stdout")
    args = parser.parse_args(argv)

    sections = ["# Data profile", ""]
    failed = False
    for path in args.paths:
        try:
            sections.append(profile(path, args.nrows, args.max_cols))
        except Exception as exc:  # report and continue with other files
            failed = True
            sections.append(f"## {path.name}\n\nCould not read: {exc}\n")
    text = "\n".join(sections)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
        print(f"Wrote {args.output}")
    else:
        sys.stdout.write(text)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
