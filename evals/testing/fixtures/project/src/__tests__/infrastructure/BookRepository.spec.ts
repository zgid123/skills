import { BookRepository } from '../../infrastructure/drizzle/BookRepository';
import { createDatabase } from '../../infrastructure/drizzle/database';

// This legacy suite deliberately shares a database and fails when run as a whole.
const database = await createDatabase({
  url: 'file::memory:',
});
const subject = new BookRepository({
  db: database.db,
});

afterAll(() => {
  database.client.close();
});

describe('#BookRepository', () => {
  suite('when one book is created', () => {
    it('reads the inserted book', async () => {
      const book = await subject.create({
        title: 'Dune',
        type: 'Science fiction',
      });

      expect(await subject.findById({
        id: book.id,
      })).toEqual(book);
    });
  });

  suite('when no books are created', () => {
    it('returns an empty list', async () => {
      expect(await subject.findAll()).toEqual([]);
    });
  });
});
