import assert from 'node:assert/strict';
import { test } from 'node:test';

import { category_slug, product_slug } from '../src/slugs.mjs';

test('slugs preserves existing behavior', () => {
  assert.equal(product_slug(' Red Chair '), 'red-chair');
  assert.equal(category_slug(' Home '), 'home');
});
