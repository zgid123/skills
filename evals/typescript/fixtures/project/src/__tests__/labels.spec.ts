import { formatLabels } from '../labels';

describe('#formatLabels', () => {
  suite('when labels include missing and padded values', () => {
    it('normalizes labels without changing the input', () => {
      const labels = ['  Alpha  ', null, '', '   ', 'Beta'] as const;
      const result = formatLabels({
        labels,
      });

      expect(result).toEqual(['Alpha', 'Unknown', 'Unknown', 'Unknown', 'Beta']);
      expect(labels).toEqual(['  Alpha  ', null, '', '   ', 'Beta']);
    });
  });

  suite('when no labels are supplied', () => {
    it('preserves an empty collection', () => {
      const result = formatLabels({
        labels: [],
      });

      expect(result).toEqual([]);
    });
  });
});
