import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    include: ['src/__tests__/**/*.spec.ts', 'src/__tests__/**/*.e2e.ts', 'src/__tests__/**/*.spec.tsx', 'packages/*/src/__tests__/**/*.spec.ts'],
  },
});
