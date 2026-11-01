"""Regression tests for the bundled data-analyst Python helpers.

Requires the script dependencies pandas, numpy, and matplotlib documented by the skill.
"""

import contextlib
import io
import json
import math
import re
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "skills" / "data-analyst" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import chart_style  # noqa: E402
import profile_data  # noqa: E402
import stats_helpers as stats  # noqa: E402


class BootstrapTests(unittest.TestCase):
    def test_missing_cluster_id_is_rejected(self):
        data = pd.DataFrame({"id": ["a", None], "value": [0, 100]})
        with self.assertRaisesRegex(ValueError, "missing"):
            stats.bootstrap_ci(data, lambda sample: sample.value.mean(), cluster="id")

    def test_duplicate_cluster_draws_remain_distinct(self):
        data = pd.DataFrame({"id": ["a", "b"], "value": [1, 2]})
        result = stats.bootstrap_ci(
            data,
            lambda sample: sample.bootstrap_id.nunique(),
            cluster="id",
            n_boot=200,
            seed=7,
            bootstrap_cluster_col="bootstrap_id",
        )
        self.assertEqual(result, (2.0, 2.0, 2.0))
        self.assertEqual(list(data.columns), ["id", "value"])

    def test_cluster_bootstrap_preserves_source_ids_for_metadata_callbacks(self):
        data = pd.DataFrame({"id": ["a", "b"], "value": [10.0, 20.0]})
        cluster_weight = {"a": 1.0, "b": 2.0}

        def statistic(sample):
            sampled_ids = sample.groupby("bootstrap_id")["id"].first()
            return float(sampled_ids.map(cluster_weight).sum())

        estimate, low, high = stats.bootstrap_ci(
            data,
            statistic,
            cluster="id",
            bootstrap_cluster_col="bootstrap_id",
            n_boot=200,
            seed=7,
        )
        self.assertEqual(estimate, 3.0)
        self.assertLessEqual(2.0, low)
        self.assertGreaterEqual(4.0, high)
        self.assertEqual(list(data.columns), ["id", "value"])

    def test_bootstrap_cluster_column_requires_cluster_and_must_be_new(self):
        data = pd.DataFrame({"id": ["a", "b"], "value": [1, 2]})
        with self.assertRaisesRegex(ValueError, "requires cluster"):
            stats.bootstrap_ci(data, lambda sample: sample.value.mean(), bootstrap_cluster_col="draw")
        with self.assertRaisesRegex(ValueError, "new"):
            stats.bootstrap_ci(
                data,
                lambda sample: sample.value.mean(),
                cluster="id",
                bootstrap_cluster_col="id",
            )


class WilsonIntervalTests(unittest.TestCase):
    def test_accepts_integer_types_and_whole_number_floats(self):
        self.assertEqual(stats.wilson_ci(np.int64(3), np.int32(10)), stats.wilson_ci(3.0, 10.0))

    def test_empty_population_remains_undefined(self):
        self.assertTrue(all(math.isnan(value) for value in stats.wilson_ci(0, 0)))

    def test_rejects_invalid_counts_and_z_values(self):
        for k, n, z in [(-1, 10, 1.96), (11, 10, 1.96), (1.5, 10, 1.96), (1, 1.5, 1.96),
                        (math.nan, 10, 1.96), (1, math.inf, 1.96), (1, 10, 0), (1, 10, -1.96),
                        (1, 10, math.nan), (1, 10, math.inf)]:
            with self.subTest(k=k, n=n, z=z), self.assertRaises((TypeError, ValueError)):
                stats.wilson_ci(k, n, z)

    def test_nonpositive_and_nonfinite_z_cannot_create_reversed_or_false_bounds(self):
        with self.assertRaises(ValueError):
            stats.wilson_ci(3, 10, z=-1.96)
        with self.assertRaises(ValueError):
            stats.wilson_ci(3, 10, z=math.nan)


class ChartMissingValueTests(unittest.TestCase):
    def test_nan_bar_is_unavailable_without_drawing_a_bar(self):
        fig, ax = chart_style.figure()
        chart_style.bar(ax, ["A", "Missing", "Zero"], [8, math.nan, 0], sort=False)
        self.assertEqual(len(ax.patches), 2)
        self.assertIn("Unavailable", [text.get_text() for text in ax.texts])
        self.assertEqual([tick.get_text() for tick in ax.get_yticklabels()], ["A", "Missing", "Zero"])
        plt.close(fig)

    def test_sorted_bars_put_largest_first_and_missing_last(self):
        labels, values = ["a", "b", "Missing", "c"], [1.0, 3.0, math.nan, 2.0]
        fig, ax = chart_style.figure()
        chart_style.bar(ax, labels, values, horizontal=True)
        top_to_bottom = [tick.get_text() for tick in ax.get_yticklabels()][::-1]
        self.assertEqual(top_to_bottom, ["b", "c", "a", "Missing"])
        plt.close(fig)
        fig, ax = chart_style.figure()
        chart_style.bar(ax, labels, values, horizontal=False)
        self.assertEqual([tick.get_text() for tick in ax.get_xticklabels()], ["b", "c", "a", "Missing"])
        plt.close(fig)

    def test_line_with_missing_last_value_gets_no_end_label(self):
        fig, ax = chart_style.figure()
        chart_style.lines(ax, [1, 2, 3], {"a": [1.0, 2.0, math.nan], "b": [1.0, 1.0, 1.0]})
        labels = [text.get_text() for text in ax.texts]
        self.assertFalse(any("nan" in label for label in labels))
        self.assertTrue(any(label.startswith("b") for label in labels))
        plt.close(fig)

    def test_nan_interval_is_unavailable_without_drawing_an_interval(self):
        fig, ax = chart_style.figure()
        chart_style.intervals(ax, ["A", "Missing"], [0.4, math.nan], [0.2, 0.1], [0.6, 0.9])
        self.assertEqual(len(ax.lines), 3)  # valid interval, valid estimate, reference only
        self.assertIn("Unavailable", [text.get_text() for text in ax.texts])
        self.assertEqual([tick.get_text() for tick in ax.get_yticklabels()], ["A", "Missing"])
        plt.close(fig)

    def test_rejects_empty_data_invalid_parameters_and_nonfinite_statistics(self):
        with self.assertRaisesRegex(ValueError, "non-empty"):
            stats.bootstrap_ci(pd.DataFrame(), lambda sample: 0)
        data = pd.DataFrame({"value": [1]})
        for kwargs in ({"n_boot": 0}, {"level": 1}, {"cluster": "missing"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                stats.bootstrap_ci(data, lambda sample: 1, **kwargs)
        with self.assertRaisesRegex(ValueError, "non-finite"):
            stats.bootstrap_ci(data, lambda sample: math.nan)


class RiskMetricTests(unittest.TestCase):
    def test_zero_capacity_flags_nobody_and_ties_are_reported(self):
        zero = stats.capacity_table([1, 0], [0.9, 0.1], [0]).iloc[0]
        self.assertEqual(zero.flagged, 0)
        tied = stats.capacity_table([1, 0, 0], [0.9, 0.9, 0.1], [0.34]).iloc[0]
        self.assertEqual(tied.flagged, 2)
        self.assertAlmostEqual(tied.alert_rate, 2 / 3)

    def test_invalid_capacity_inputs_are_rejected(self):
        for labels, scores, capacities in [([], [], [0.2]), ([1], [0.5], []), ([1], [math.nan], [0.2]), ([2], [0.5], [0.2]), ([1], [0.5], [1.1]), ([1, 0], [0.5], [0.2])]:
            with self.subTest(labels=labels, scores=scores, capacities=capacities), self.assertRaises(ValueError):
                stats.capacity_table(labels, scores, capacities)

    def test_supplied_thresholds_must_cover_requested_capacities(self):
        with self.assertRaisesRegex(ValueError, "missing capacities"):
            stats.capacity_table([1, 0], [0.9, 0.1], [0.5, 1.0], thresholds={0.5: 0.8})

    def test_calibration_rejects_invalid_or_uncovered_probabilities(self):
        for probabilities in ([math.nan], [1.01], [0.1, 0.9]):
            with self.subTest(probabilities=probabilities), self.assertRaises(ValueError):
                stats.calibration_table([1] * len(probabilities), probabilities, bins=(0, 0.5, 0.8))

    def test_weighted_and_replicate_helpers_reject_invalid_inputs(self):
        with self.assertRaisesRegex(ValueError, "equal length"):
            stats.weighted_share([1], [1, 2])
        with self.assertRaisesRegex(ValueError, "binary"):
            stats.weighted_share([2], [1])
        with self.assertRaisesRegex(ValueError, "non-negative"):
            stats.weighted_share([1], [-1])
        with self.assertRaisesRegex(ValueError, "at least one replicate"):
            stats.replicate_se(0.5, [])


class RepairFixtureTests(unittest.TestCase):
    fixtures = ROOT / "evals" / "data-analyst" / "fixtures" / "development" / "repair"

    def test_diagnosis_fixture_separates_mix_shift_from_segment_change(self):
        data = pd.read_csv(self.fixtures / "diagnosis.csv")
        totals = data.groupby("period").agg(completed=("completed", "sum"), eligible=("eligible", "sum"))
        rates = data.assign(rate=data.completed / data.eligible).pivot(index="segment", columns="period", values="rate")
        self.assertAlmostEqual(totals.loc["A", "completed"] / totals.loc["A", "eligible"], 0.78)
        self.assertAlmostEqual(totals.loc["B", "completed"] / totals.loc["B", "eligible"], 0.42)
        self.assertAlmostEqual(totals.loc["C", "completed"] / totals.loc["C", "eligible"], 0.34)
        self.assertTrue(np.allclose(rates[["A", "B"]], [[0.9, 0.9], [0.3, 0.3]]))
        self.assertAlmostEqual(rates.loc["Beta", "C"], 0.2)

    def test_early_warning_fixture_has_expected_eligibility_and_capacity(self):
        data = pd.read_csv(self.fixtures / "early-warning.csv")
        eligible = data[data.withdrawn_before_cutoff == False].copy()  # noqa: E712
        at_risk = eligible.outcome.isin(["fail", "withdraw"])
        selected = eligible.nlargest(2, "risk_score_at_day30")
        true_positive = selected.outcome.isin(["fail", "withdraw"]).sum()
        self.assertEqual(len(eligible), 6)
        self.assertEqual(int(at_risk.sum()), 3)
        self.assertEqual(selected.student_id.tolist(), ["S1", "S2"])
        self.assertEqual(true_positive, 1)
        self.assertEqual(int(at_risk.sum() - true_positive), 2)
        self.assertTrue((eligible.score_available_day <= 30).all())
        self.assertTrue((eligible.grade_available_day > 30).all())

    def test_survey_fixture_has_planted_weighted_share_and_fay_se(self):
        data = pd.read_csv(self.fixtures / "survey.csv")
        weighted, n, _ = stats.weighted_share(data.satisfied, data.final_weight)
        replicate_estimates = [stats.weighted_share(data.satisfied, data[f"replicate_{i}"])[0] for i in range(1, 5)]
        standard_error = stats.replicate_se(weighted, replicate_estimates, method="fay", fay_k=0.5)
        self.assertEqual(n, 4)
        self.assertEqual(data.satisfied.mean(), 0.5)
        self.assertAlmostEqual(weighted, 0.75)
        self.assertAlmostEqual(standard_error, 0.16598, places=4)

    def test_runner_dictionaries_do_not_state_planted_answers_or_decisions(self):
        diagnosis = json.loads((self.fixtures / "diagnosis-dictionary.json").read_text())
        survey = json.loads((self.fixtures / "survey-dictionary.json").read_text())
        early_warning = json.loads((self.fixtures / "early-warning-dictionary.json").read_text())
        self.assertNotIn("unweighted_estimate", survey)
        self.assertNotIn("weighted_estimate", survey)
        self.assertNotIn("outcome_definition_open_to_user", early_warning)
        self.assertNotIn("baseline composition", json.dumps(diagnosis).lower())
        self.assertNotIn("within-segment rates unchanged", json.dumps(diagnosis).lower())

    def test_documented_cohort_query_preserves_grid_zeroes_and_maturity(self):
        import sqlite3

        reference = ROOT / "skills" / "data-analyst" / "references" / "sql-for-analysis.md"
        text = reference.read_text()
        section = text.split("### 4. Cohort Retention Analysis", 1)[1].split("### 5.", 1)[0]
        query = re.search(r"\s*```sql\n([\s\S]*?)\n\s*```", section).group(1)
        fixture = json.loads((self.fixtures / "cohort-retention.json").read_text())
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE users (user_id TEXT, signup_at TEXT)")
        con.execute("CREATE TABLE user_events (user_id TEXT, event_at TEXT)")
        con.executemany("INSERT INTO users VALUES (?, ?)", [(r["user_id"], r["signup_at"]) for r in fixture["users"]])
        con.executemany("INSERT INTO user_events VALUES (?, ?)", [(r["user_id"], r["event_at"]) for r in fixture["events"]])
        rows = con.execute(query, {"cutoff": fixture["cutoff"], "max_period": fixture["maximum_period_offset"]}).fetchall()
        self.assertEqual(rows, [
            ("2026-01", 2, 0, 1, 0.5),
            ("2026-01", 2, 1, 1, 0.5),
            ("2026-01", 2, 2, 0, 0.0),
            ("2026-03", 1, 0, 1, 1.0),
            ("2026-03", 1, 1, None, None),
            ("2026-03", 1, 2, None, None),
        ])

    def test_documentation_keeps_statistical_and_reconciliation_conditions(self):
        statistics = (ROOT / "skills" / "data-analyst" / "references" / "statistics-and-inference.md").read_text()
        tests = statistics.split("| Analytical Scenario", 1)[1].split("\n\n", 1)[0]
        self.assertRegex(tests, r"Mann.?Whitney[^\n]*(?:not|distribution|rank)[^\n]*")
        self.assertRegex(tests, r"Wilcoxon[^\n]*(?:not|distribution|symmetric)[^\n]*")
        self.assertIn("independent tests", statistics)
        quality = (ROOT / "skills" / "data-analyst" / "references" / "data-quality.md").read_text().lower()
        for component in ("shipping", "tax", "discount"):
            self.assertIn(component, quality)

    def test_documented_order_reconciliation_uses_source_components(self):
        import sqlite3

        reference = ROOT / "skills" / "data-analyst" / "references" / "data-quality.md"
        text = reference.read_text()
        section = text.split("### 4. Reconciliation and Aggregation Sanity Checks", 1)[1].split("### 5.", 1)[0]
        query = re.search(r"\s*```sql\n([\s\S]*?)\n\s*```", section).group(1)
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE orders (order_id INTEGER, total_amount REAL, discount REAL, shipping REAL, tax REAL)")
        con.execute("CREATE TABLE order_line_items (order_id INTEGER, item_amount REAL)")
        con.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", [(1, 155, 15, 8, 12), (2, 150, 15, 8, 12)])
        con.executemany("INSERT INTO order_line_items VALUES (?, ?)", [(1, 100), (1, 50), (2, 100), (2, 50)])
        self.assertEqual(con.execute(query).fetchall(), [(2, 150.0, 150.0)])


class ChartAndProfilerTests(unittest.TestCase):
    def test_lines_supports_datetime_x_and_spreads_colliding_labels(self):
        fig, ax = chart_style.figure()
        chart_style.lines(ax, pd.date_range("2026-01-01", periods=3), {"A": [1, 2, 3], "B": [2, 2, 3], "C": [3, 2, 3]})
        fig.canvas.draw()
        annotations = ax.texts
        self.assertEqual(len(annotations), 3)
        offsets = sorted(annotation.get_position()[1] for annotation in annotations)
        self.assertTrue(all(right - left >= 12 for left, right in zip(offsets, offsets[1:])))
        chart_style.plt.close(fig)

    def test_lines_rejects_empty_or_mismatched_inputs(self):
        fig, ax = chart_style.figure()
        with self.assertRaisesRegex(ValueError, "at least one"):
            chart_style.lines(ax, [], {"A": []})
        with self.assertRaisesRegex(ValueError, "same number"):
            chart_style.lines(ax, [1, 2], {"A": [1]})
        chart_style.plt.close(fig)

    def test_profiler_returns_failure_for_bad_files_and_continues(self):
        with tempfile.TemporaryDirectory() as temp:
            valid = Path(temp) / "valid.csv"
            valid.write_text("id,value\n1,2\n")
            missing = Path(temp) / "missing.csv"
            malformed = Path(temp) / "malformed.csv"
            malformed.write_text("id,value\n1,2\n3,4,5\n")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                status = profile_data.main([str(valid), str(missing), str(malformed)])
            self.assertEqual(status, 1)
            self.assertIn("valid.csv", output.getvalue())
            self.assertIn("Could not read", output.getvalue())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(profile_data.main([str(valid)]), 0)

    def test_example_report_arithmetic_reconciles(self):
        report = (ROOT / "skills" / "data-analyst" / "references" / "example-report.md").read_text()
        sessions = int(re.search(r"product-view sessions stayed near ([\d,]+)", report).group(1).replace(",", ""))
        rates = re.search(r"Conversion fell from ([\d.]+)% .*? to ([\d.]+)%", report)
        before, after = (float(value) / 100 for value in rates.groups())
        claimed_lost_orders = int(re.search(r"difference of approximately ([\d,]+) orders per week", report).group(1).replace(",", ""))
        implied_lost_orders = sessions * (before - after)
        self.assertLessEqual(abs(implied_lost_orders - claimed_lost_orders) / claimed_lost_orders, 0.05)
        self.assertIn("3,400 of the 3,700-order decline (92%)", report)
        revenue = int(re.search(r"\*\*\$([\d,]+)\*\* at \$61 per order", report).group(1).replace(",", ""))
        self.assertLessEqual(abs(claimed_lost_orders * 61 - revenue) / revenue, 0.05)

    def test_storytelling_example_uses_one_exposure_outcome_population_and_period(self):
        example = (ROOT / "skills" / "data-analyst" / "references" / "visualization-and-storytelling.md").read_text()
        skill = (ROOT / "skills" / "data-analyst" / "SKILL.md").read_text()
        title = re.search(r"\*\*Students missing ([^*]+)\*\*", example).group(1)
        self.assertIn("by day 60", title)
        self.assertIn("fail or withdraw by course end", title)
        self.assertIn("missed an assignment due by day 60", skill)
        self.assertIn("fail or withdraw by course end", skill)
        self.assertNotIn("Missing one early assignment triples withdrawal risk", skill)
        self.assertIn("missed at least one assignment due by day 60", example)
        self.assertIn("submitted every assignment due by day 60", example)
        self.assertIn("active at day 60", example)
        self.assertIn("by course end", example)
        rates = re.search(r"85% .*? compared with 26%", example)
        self.assertIsNotNone(rates)
        self.assertIn("about 3.3 times", title)
        self.assertLessEqual(abs(85 / 26 - 3.3), 0.1)
        self.assertNotIn("first assignment", example)


if __name__ == "__main__":
    unittest.main()
