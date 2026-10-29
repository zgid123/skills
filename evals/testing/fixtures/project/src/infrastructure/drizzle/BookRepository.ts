import { eq } from 'drizzle-orm';
import type { LibSQLDatabase } from 'drizzle-orm/libsql';

import { books, type TBook, type TNewBook } from './schema';

interface IBookRepositoryParams {
  db: LibSQLDatabase;
}

interface IFindBookParams {
  id: number;
}

export class BookRepository {
  readonly #db: LibSQLDatabase;

  public constructor({ db }: IBookRepositoryParams) {
    this.#db = db;
  }

  public async create(params: TNewBook): Promise<TBook> {
    const [book] = await this.#db.insert(books).values(params).returning();

    if (!book) {
      throw new Error('Insert did not return a book');
    }

    return book;
  }

  public async findById({ id }: IFindBookParams): Promise<TBook | null> {
    const [book] = await this.#db.select().from(books).where(eq(books.id, id));

    return book ?? null;
  }

  public async findAll(): Promise<TBook[]> {
    return this.#db.select().from(books);
  }
}
