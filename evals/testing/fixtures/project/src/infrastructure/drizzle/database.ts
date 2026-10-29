import { createClient, type Client } from '@libsql/client';
import { drizzle, type LibSQLDatabase } from 'drizzle-orm/libsql';

interface ICreateDatabaseParams {
  url: string;
}

interface ITestDatabase {
  client: Client;
  db: LibSQLDatabase;
}

export async function createDatabase({ url }: ICreateDatabaseParams): Promise<ITestDatabase> {
  const client = createClient({
    url,
  });

  await client.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, type TEXT NOT NULL)');

  return {
    client,
    db: drizzle(client),
  };
}
