import { Hono } from 'hono';

import { BookRepository } from './infrastructure/drizzle/BookRepository';

interface ICreateAppParams {
  repository: BookRepository;
}

export function createApp({ repository }: ICreateAppParams): Hono {
  const app = new Hono();

  app.post('/books', async (context) => {
    const body: unknown = await context.req.json();

    if (typeof body !== 'object' || body === null || !('title' in body) || !('type' in body) || typeof body.title !== 'string' || typeof body.type !== 'string') {
      return context.json({
        error: 'title and type are required',
      }, 400);
    }

    const book = await repository.create({
      title: body.title,
      type: body.type,
    });

    return context.json(book, 201);
  });

  return app;
}
