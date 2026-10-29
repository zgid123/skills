export function creationRoute(record) {
  const date = new Date(record.createdAt);
  const createdAt = date.toISOString().slice(0, 10);
  return { createdAt };
}

export function updateRoute(record) {
  const date = new Date(record.updatedAt);
  const updatedAt = date.toISOString().slice(0, 10);
  return { updatedAt };
}
