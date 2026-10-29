import assert from 'node:assert/strict';
import { test } from 'node:test';

import { creationRoute, updateRoute } from '../src/routes.mjs';

test('routes preserves existing behavior', () => {
  assert.deepEqual(creationRoute({ createdAt: '2026-10-28T14:00:00Z' }), { createdAt: '2026-10-28' });
  assert.deepEqual(updateRoute({ updatedAt: '2026-10-29T14:00:00Z' }), { updatedAt: '2026-10-29' });
});
