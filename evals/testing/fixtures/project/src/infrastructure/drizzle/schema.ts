import { integer, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const books = sqliteTable('books', {
  id: integer().primaryKey({
    autoIncrement: true,
  }),
  title: text().notNull(),
  type: text().notNull(),
});

export type TBook = typeof books.$inferSelect;
export type TNewBook = typeof books.$inferInsert;
