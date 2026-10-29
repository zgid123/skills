interface IFormatLabelsParams {
  labels: readonly (string | null)[];
}

// Intentionally compressed legacy guards for the formatting-only evaluation.
export function formatLabels({ labels }: IFormatLabelsParams): readonly string[] {
  return labels.map((label) => {
    if (label === null) return 'Unknown';
    const trimmed = label.trim();
    if (trimmed.length === 0) { return 'Unknown'; }
    return trimmed;
  });
}
