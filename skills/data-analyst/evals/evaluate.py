"""Deterministic factual checks, never an automatic analytical-quality grader."""
import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

FIXTURES = Path(__file__).parent / 'fixtures' / 'development'


def rows(name):
    with (FIXTURES / name).open(newline='') as source:
        return list(csv.DictReader(source))


def fixture_oracles():
    """Recompute critical facts from inputs rather than model-written prose."""
    orders = rows('orders.csv')
    transactions = rows('transactions.csv')
    totals = defaultdict(float)
    counts = defaultdict(int)
    for row in transactions:
        month = row['date'][:7]
        totals[month] += float(row['revenue_usd'])
        counts[month] += 1
    events = defaultdict(list)
    for row in rows('events.csv'):
        events[row['session_id']].append((int(row['minute']), row['event']))
    funnel = [0] * 4
    for session in events.values():
        cursor = -math.inf
        for step, event in enumerate(['landing_view', 'product_view', 'add_to_cart', 'checkout_complete']):
            times = [time for time, name in session if name == event and time >= cursor]
            if not times:
                break
            cursor = min(times)
            funnel[step] += 1
    survey = rows('survey.csv')
    weights = [float(row['weight']) for row in survey]
    revenue = {row['order_id']: float(row['revenue']) for row in orders}
    months = {row['month']: float(row['revenue']) for row in rows('months.csv')}
    previous = months.get('2026-02')
    season = [float(row['value']) for row in sorted(rows('season.csv'), key=lambda row: int(row['day']))][-7:]
    return {
        'orders.count': len(orders),
        'responses.rows': len(rows('responses.csv')),
        'responses.users': len({row['user_id'] for row in rows('responses.csv')}),
        'orders.revenue': sum(revenue.values()),
        'orders.aov': sum(revenue.values()) / len(orders),
        'join.naive_revenue': sum(revenue[row['order_id']] for row in rows('items.csv')),
        'transactions.august_revenue': totals['2026-08'],
        'transactions.september_revenue': totals['2026-09'],
        'transactions.august_aov': totals['2026-08'] / counts['2026-08'],
        'transactions.september_aov': totals['2026-09'] / counts['2026-09'],
        'funnel.counts': funnel,
        'survey.weighted': sum(float(row['satisfied']) * float(row['weight']) for row in survey) / sum(weights),
        'survey.unweighted': sum(float(row['satisfied']) for row in survey) / len(survey),
        'survey.effective_n': sum(weights) ** 2 / sum(weight ** 2 for weight in weights),
        'calendar.march_mom': None if previous in (None, 0) else months['2026-03'] / previous - 1,
        'season.forecast': [season[horizon % 7] for horizon in range(10)],
    }


def matches(actual, expected, tolerance=1e-6):
    if isinstance(expected, list):
        return isinstance(actual, list) and len(actual) == len(expected) and all(matches(a, b, tolerance) for a, b in zip(actual, expected))
    if expected is None:
        return actual is None
    return isinstance(actual, (int, float)) and not isinstance(actual, bool) and math.isfinite(actual) and abs(actual - expected) <= tolerance


def evaluate_submission(submission, required):
    """Check declared facts and ledger consistency; execution/meaning need review.

    A ledger item has fact, expected, actual, condition (eq/le/ge), status,
    method and evidence. 'expected' must match our independent fixture oracle.
    """
    oracle = fixture_oracles()
    errors = []
    facts = submission.get('facts', {})
    ledger = submission.get('ledger', [])
    for fact in required:
        if fact not in oracle:
            raise ValueError(f'Unknown oracle: {fact}')
        if fact not in facts or not matches(facts[fact], oracle[fact]):
            errors.append(f'{fact}: missing or incorrect result')
        checks = [item for item in ledger if item.get('fact') == fact]
        if len(checks) != 1:
            errors.append(f'{fact}: requires exactly one ledger check')
            continue
        item = checks[0]
        condition = item.get('condition')
        expected, actual = item.get('expected'), item.get('actual')
        if not matches(expected, oracle[fact]):
            errors.append(f'{fact}: expected quantity contradicts fixture')
        valid = matches(actual, expected)
        if condition in ('le', 'ge') and isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
            valid = math.isfinite(actual) and (actual <= expected if condition == 'le' else actual >= expected)
        if condition not in ('eq', 'le', 'ge'):
            errors.append(f'{fact}: invalid or missing condition')
            valid = False
        if item.get('status') == 'PASS' and not valid:
            errors.append(f'{fact}: false PASS; observed quantity fails condition')
        if item.get('status') != 'PASS':
            errors.append(f'{fact}: check not verified as passing')
        if not item.get('method') or not item.get('evidence'):
            errors.append(f'{fact}: lacks method or evidence locator')
        if condition != 'eq':
            errors.append(f'{fact}: fixture result requires equality, not weakened bound')
        if not matches(actual, facts.get(fact)):
            errors.append(f'{fact}: ledger and reported result disagree')
    return {'factual_checks_passed': not errors, 'errors': errors,
            'analytical_quality': 'REQUIRES INDEPENDENT REVIEW',
            'overall_pass': None,
            'limitations': 'JSON consistency cannot prove execution, inference validity, completeness, useful insight or artifact usability.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('submission', type=Path)
    parser.add_argument('--required', nargs='+', required=True)
    args = parser.parse_args()
    print(json.dumps(evaluate_submission(json.loads(args.submission.read_text()), args.required), indent=2))
