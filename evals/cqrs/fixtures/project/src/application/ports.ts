export interface IAuditLog {
  append(entry: string): Promise<void>;
}
