"""Run: python3 -m unittest discover -s skills/data-analyst/evals -v"""
import copy
import unittest

from evaluate import evaluate_submission, fixture_oracles


def submission():
    return {'facts': {'orders.revenue': 300}, 'ledger': [
        {'fact': 'orders.revenue', 'expected': 300, 'actual': 300,
         'condition': 'eq', 'status': 'PASS', 'method': 'sum orders.csv revenue',
         'evidence': 'results/checks.json:orders.revenue'}]}


class EvaluatorTests(unittest.TestCase):
    def test_fixture_properties(self):
        facts = fixture_oracles()
        expected = {'responses.rows': 5, 'responses.users': 3, 'orders.count': 3, 'orders.revenue': 300, 'orders.aov': 100,
                    'join.naive_revenue': 700, 'transactions.august_revenue': 18000,
                    'transactions.september_revenue': 13200,
                    'transactions.august_aov': 180, 'transactions.september_aov': 132,
                    'funnel.counts': [3, 2, 1, 1], 'survey.weighted': .2,
                    'survey.unweighted': .5, 'survey.effective_n': 100 / 34,
                    'calendar.march_mom': None,
                    'season.forecast': [8, 9, 10, 11, 12, 13, 14, 8, 9, 10]}
        self.assertEqual(facts, expected)

    def test_consistent_strong_result_still_requires_review(self):
        result = evaluate_submission(submission(), ['orders.revenue'])
        self.assertTrue(result['factual_checks_passed'])
        self.assertIsNone(result['overall_pass'])
        self.assertEqual(result['analytical_quality'], 'REQUIRES INDEPENDENT REVIEW')

    def test_false_pass_cannot_hide_failed_quantity(self):
        output = submission()
        output['ledger'][0]['actual'] = 700
        self.assertFalse(evaluate_submission(output, ['orders.revenue'])['factual_checks_passed'])

    def test_response_rows_do_not_verify_unique_users(self):
        output = {'facts': {'responses.users': 3}, 'ledger': [
            {'fact': 'responses.users', 'expected': 3, 'actual': 5,
             'condition': 'eq', 'status': 'PASS', 'method': 'count distinct user_id',
             'evidence': 'checks.json:response_rows'}]}
        self.assertFalse(evaluate_submission(output, ['responses.users'])['factual_checks_passed'])
        output['ledger'][0]['actual'] = 3
        output['ledger'][0]['evidence'] = 'checks.json:unique_users'
        self.assertTrue(evaluate_submission(output, ['responses.users'])['factual_checks_passed'])

    def test_fabricated_expected_value_rejected(self):
        output = submission()
        output['facts']['orders.revenue'] = 700
        output['ledger'][0].update(expected=700, actual=700)
        self.assertFalse(evaluate_submission(output, ['orders.revenue'])['factual_checks_passed'])

    def test_weakened_condition_cannot_auto_pass(self):
        output = submission()
        output['ledger'][0]['condition'] = 'le'
        self.assertFalse(evaluate_submission(output, ['orders.revenue'])['factual_checks_passed'])

    def test_headings_and_checklist_are_not_evidence(self):
        output = {'report': '# Business Understanding\n# Investigation\n# Verification\nAll checks PASS; hypotheses tested.', 'facts': {}, 'ledger': []}
        self.assertFalse(evaluate_submission(output, ['orders.revenue'])['factual_checks_passed'])

    def test_shallow_correct_numbers_cannot_pass_analytical_review(self):
        output = submission()
        output['report'] = 'Revenue is 300. We should grow sales.'
        result = evaluate_submission(output, ['orders.revenue'])
        self.assertTrue(result['factual_checks_passed'])
        self.assertIsNone(result['overall_pass'])

    def test_missing_evidence_duplicate_and_unverified_rejected(self):
        for mutation in ['missing', 'duplicate', 'unverified']:
            with self.subTest(mutation=mutation):
                output = copy.deepcopy(submission())
                if mutation == 'missing':
                    output['ledger'][0]['evidence'] = ''
                elif mutation == 'duplicate':
                    output['ledger'].append(output['ledger'][0])
                else:
                    output['ledger'][0]['status'] = 'NOT VERIFIED'
                self.assertFalse(evaluate_submission(output, ['orders.revenue'])['factual_checks_passed'])

    def test_nonfinite_and_boolean_are_not_quantities(self):
        for value in [float('nan'), float('inf'), True]:
            output = submission()
            output['facts']['orders.revenue'] = value
            self.assertFalse(evaluate_submission(output, ['orders.revenue'])['factual_checks_passed'])


if __name__ == '__main__':
    unittest.main()
