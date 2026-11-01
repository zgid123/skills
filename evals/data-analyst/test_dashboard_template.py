"""Exercise the bundled dashboard line renderer in Node without a browser dependency."""

import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "skills" / "data-analyst" / "assets" / "dashboard-template.html"


NODE_PROBE = r"""
const fs = require('fs');
const vm = require('vm');
const html = fs.readFileSync(process.argv[1], 'utf8').replace(/<!--[\s\S]*?-->/g, '');
const blocks = [...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)];
const dataBlock = blocks.find((m) => m[1].includes('application/json'));
const codeBlock = blocks.find((m) => !m[1].includes('application/json'));
const payload = JSON.parse(dataBlock[2]);
const code = codeBlock[2].replace(
  '        renderHeader();\n        renderControls();\n        render();',
  '        globalThis.__test = { line }; return;'
);
if (code === codeBlock[2]) throw new Error('renderer test hook not found');
const context = { document: { getElementById: () => ({ textContent: JSON.stringify(payload) }) } };
vm.createContext(context);
vm.runInContext(code, context);
const chart = (data, cfg, width = 560) => {
  const el = { clientWidth: width, innerHTML: '' };
  context.__test.line(el, data, cfg);
  return el.innerHTML;
};
const outputs = {};
outputs.numeric = chart([
  { day: 100, value: 3, series: 'A' },
  { day: 2, value: 2, series: 'A' },
  { day: 1, value: 1, series: 'A' }
], { x: 'day', y: 'value', series: 'series' });
outputs.dates = chart([
  { day: '2026-03-01', value: 3, series: 'A' },
  { day: '2026-01-01', value: 1, series: 'A' },
  { day: '2026-02-01', value: 2, series: 'A' }
], { x: 'day', y: 'value', series: 'series', xType: 'date' });
outputs.category = chart([
  { day: 'B', value: 2, series: 'A' },
  { day: 'A', value: 1, series: 'A' }
], { x: 'day', y: 'value', series: 'series' });
outputs.numericCategory = chart([
  { day: 2, value: 1, series: 'A' },
  { day: 1, value: 2, series: 'A' },
  { day: 3, value: 3, series: 'A' }
], { x: 'day', y: 'value', series: 'series', xType: 'category' });
outputs.multiCategory = chart([
  { day: 'a', value: 1, series: 'A' },
  { day: 'b', value: 2, series: 'A' },
  { day: 'c', value: 3, series: 'A' },
  { day: 'c', value: 1, series: 'B' },
  { day: 'a', value: 2, series: 'B' },
  { day: 'b', value: 3, series: 'B' }
], { x: 'day', y: 'value', series: 'series', xType: 'category' });
const dailyDates = Array.from({ length: 30 }, (_, i) => {
  const date = new Date(Date.UTC(2026, 8, i + 1)).toISOString().slice(0, 10);
  return { day: date, value: i, series: 'daily' };
});
outputs.denseDates = chart(dailyDates, { x: 'day', y: 'value', series: 'series', xType: 'date' });
outputs.narrowDates = chart(dailyDates, { x: 'day', y: 'value', series: 'series', xType: 'date' }, 300);
outputs.gap = chart([
  { day: 1, value: 1, series: 'A' },
  { day: 2, value: null, series: 'A' },
  { day: 3, value: 3, series: 'A' }
], { x: 'day', y: 'value', series: 'series' });
outputs.collisions = chart([
  { day: 1, value: 1, series: 'A' }, { day: 2, value: 3, series: 'A' },
  { day: 1, value: 2, series: 'B' }, { day: 2, value: 3, series: 'B' },
  { day: 1, value: 3, series: 'C' }, { day: 2, value: 3, series: 'C' }
], { x: 'day', y: 'value', series: 'series' });
outputs.single = chart([{ day: 7, value: 4, series: 'A' }], { x: 'day', y: 'value', series: 'series' });
outputs.empty = chart([{ day: 1, value: null, series: 'A' }], { x: 'day', y: 'value', series: 'series' });
outputs.filteredEmpty = chart([], { x: 'day', y: 'value', series: 'series' });
try {
  chart([{ day: 'not-a-date', value: 1, series: 'A' }], { x: 'day', y: 'value', series: 'series', xType: 'date' });
  outputs.invalidDate = 'accepted';
} catch (error) { outputs.invalidDate = error.message; }
try {
  chart([{ day: 1, value: 1, series: 'A' }], { x: 'day', y: 'value', series: 'series', xType: 'unknown' });
  outputs.invalidType = 'accepted';
} catch (error) { outputs.invalidType = error.message; }
console.log(JSON.stringify(outputs));
"""


def rendered_cases():
    result = subprocess.run(
        ["node", "-e", NODE_PROBE, str(TEMPLATE)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


class DashboardLineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = rendered_cases()

    def test_numeric_axis_preserves_irregular_spacing_and_sorts(self):
        points = re.search(r'<polyline[^>]*points="([^"]+)"', self.outputs["numeric"]).group(1)
        xs = [float(point.split(",")[0]) for point in points.split()]
        self.assertEqual(xs, sorted(xs))
        self.assertAlmostEqual((xs[2] - xs[1]) / (xs[1] - xs[0]), 98)

    def test_explicit_date_axis_sorts_dates_and_preserves_time_spacing(self):
        html = self.outputs["dates"]
        labels = re.findall(r'<text class="x-tick-label"[^>]+>([^<]+)</text>', html)
        self.assertEqual(labels, ["2026-01-01", "2026-02-01", "2026-03-01"])
        points = re.search(r'<polyline[^>]*points="([^"]+)"', html).group(1)
        xs = [float(point.split(",")[0]) for point in points.split()]
        self.assertAlmostEqual((xs[1] - xs[0]) / (xs[2] - xs[1]), 31 / 28, delta=0.02)

    def test_category_axis_keeps_first_seen_order(self):
        html = self.outputs["category"]
        labels = re.findall(r'<text x="[^"]+" y="252" text-anchor="middle">([^<]+)</text>', html)
        self.assertEqual(labels, ["B", "A"])

    def test_category_series_follow_shared_domain_for_string_and_numeric_labels(self):
        for output in [self.outputs["numericCategory"], self.outputs["multiCategory"]]:
            with self.subTest(output=output[:80]):
                points = re.findall(r'<polyline[^>]*points="([^"]+)"', output)
                self.assertTrue(points)
                for line in points:
                    x_positions = [float(point.split(",")[0]) for point in line.split()]
                    self.assertEqual(x_positions, sorted(x_positions))

    def test_dense_date_labels_keep_endpoints_without_collisions(self):
        for name in ["denseDates", "narrowDates"]:
            with self.subTest(width=name):
                html = self.outputs[name]
                labels = re.findall(
                    r'<text class="x-tick-label" x="([\d.]+)" y="252" text-anchor="(start|middle|end)">([^<]+)</text>',
                    html,
                )
                self.assertLess(len(labels), 30)
                self.assertEqual(labels[0][2], "2026-09-01")
                self.assertEqual(labels[-1][2], "2026-09-30")
                self.assertFalse({"2026-09-20", "2026-09-22"}.issubset({label[2] for label in labels}))
                spans = []
                for raw_x, anchor, label in labels:
                    x = float(raw_x)
                    width = len(label) * 7
                    left = x if anchor == "start" else x - width if anchor == "end" else x - width / 2
                    spans.append((left, left + width))
                self.assertTrue(all(right + 8 <= next_left for (_, right), (next_left, _) in zip(spans, spans[1:])))
                self.assertEqual(html.count("<circle"), 30)

    def test_missing_measurement_breaks_the_line(self):
        self.assertEqual(self.outputs["gap"].count("<polyline"), 0)
        self.assertEqual(self.outputs["gap"].count("<circle"), 2)

    def test_line_end_labels_are_spread_and_single_points_render(self):
        labels = re.findall(r'class="line-end-label"[^>]*y="([\d.]+)"', self.outputs["collisions"])
        values = sorted(map(float, labels))
        self.assertEqual(len(values), 3)
        self.assertTrue(all(b - a >= 14 for a, b in zip(values, values[1:])))
        self.assertEqual(self.outputs["single"].count("<circle"), 1)
        self.assertIn('cx="239"', self.outputs["single"])

    def test_all_missing_values_show_an_empty_state(self):
        self.assertIn("No valid values", self.outputs["empty"])
        self.assertIn("No valid values", self.outputs["filteredEmpty"])

    def test_invalid_explicit_x_types_are_rejected(self):
        self.assertIn("valid ISO", self.outputs["invalidDate"])
        self.assertIn("Unknown line xType", self.outputs["invalidType"])


EXTENDED_PROBE = NODE_PROBE.replace(
    "  '        globalThis.__test = { line }; return;'",
    "  '        globalThis.__test = { line, bar, interval, kpiState, kpiCard, state }; return;'",
).replace(
    "const payload = JSON.parse(dataBlock[2]);",
    "const payload = process.argv[2] ? JSON.parse(process.argv[2]) : JSON.parse(dataBlock[2]);",
).replace(
    "console.log(JSON.stringify(outputs));",
    """const renderWith = (name, data, cfg) => {
  const el = { clientWidth: 560, innerHTML: '' };
  context.__test[name](el, data, cfg);
  return el.innerHTML;
};
outputs.barMissing = renderWith('bar', [
  { category: 'A', value: 8 }, { category: 'B', value: null }, { category: 'C', value: 0 }
], { x: 'category', y: 'value' });
outputs.intervalMissing = renderWith('interval', [
  { category: 'A', value: 0.4, low: 0.2, high: 0.6 },
  { category: 'B', value: null, low: 0.1, high: 0.9 }
], { x: 'category', y: 'value', low: 'low', high: 'high' });
outputs.kpiNorth = context.__test.kpiState({ table: 'kpi', value: 'orders' });
outputs.kpiNorthCard = context.__test.kpiCard({ table: 'kpi', value: 'orders', label: 'Order count' });
context.__test.state.region = 'All';
outputs.kpiAll = context.__test.kpiState({ table: 'kpi', value: 'orders' });
outputs.kpiAllCard = context.__test.kpiCard({ table: 'kpi', value: 'orders', label: 'Order count' });
context.__test.state.region = 'West';
outputs.kpiWest = context.__test.kpiState({ table: 'kpi', value: 'orders' });
outputs.kpiWestCard = context.__test.kpiCard({ table: 'kpi', value: 'orders', label: 'Order count' });
console.log(JSON.stringify(outputs));""",
)


class DashboardMissingAndKpiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = {
            "filters": [{"id": "region", "label": "Region", "options": ["North", "All", "West"], "default": "North"}],
            "tables": {"kpi": [
                {"region": "North", "orders": 7},
                {"region": "All", "orders": 11},
                {"region": "All", "orders": 13},
            ]},
        }
        result = subprocess.run(
            ["node", "-e", EXTENDED_PROBE, str(TEMPLATE), json.dumps(payload)],
            check=True,
            capture_output=True,
            text=True,
        )
        cls.outputs = json.loads(result.stdout)

    def test_missing_bar_and_interval_are_unavailable_without_marks(self):
        bar = self.outputs["barMissing"]
        self.assertIn(">B</text>", bar)
        self.assertIn("Unavailable", bar)
        self.assertNotRegex(bar, r"<title>B:")
        self.assertIn("<title>C: 0</title>", bar)
        interval = self.outputs["intervalMissing"]
        self.assertIn(">B</text>", interval)
        self.assertIn("Unavailable", interval)
        self.assertEqual(interval.count("<circle"), 1)

    def test_kpi_returns_value_ambiguous_and_unavailable_states(self):
        self.assertEqual(self.outputs["kpiNorth"], {"state": "value", "value": "7"})
        self.assertEqual(self.outputs["kpiAll"], {"state": "ambiguous", "value": "—"})
        self.assertEqual(self.outputs["kpiWest"], {"state": "unavailable", "value": "—"})
        self.assertIn(">7</div>", self.outputs["kpiNorthCard"])
        self.assertIn("ambiguous", self.outputs["kpiAllCard"])
        self.assertIn("unavailable", self.outputs["kpiWestCard"])


if __name__ == "__main__":
    unittest.main()
