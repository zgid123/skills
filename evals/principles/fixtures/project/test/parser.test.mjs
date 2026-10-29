import assert from 'node:assert/strict';
import { test } from 'node:test';

import { parse_name } from '../src/parser.mjs';

test('parser preserves existing behavior', () => {
  assert.equal(parse_name(' Alpha '), 'Alpha');
});
