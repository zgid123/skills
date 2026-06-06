# Testing Domain Behavior

Test domain behavior directly. Domain tests should be fast, framework-free, and free of database or HTTP setup.

Follow the [Vitest convention](../../testing/references/vitest/convention.md) for file structure, naming, and `describe`/`suite`/`it` layout.

## What to Test

- Valid state transitions on entities and aggregates.
- Invalid state transitions — assert the correct domain error is thrown.
- Invariants — behavior that must always hold regardless of input.
- Domain error cases — wrong state, missing precondition, business rule violation.
- Value object validation — reject invalid values at construction.
- Important business edge cases surfaced by domain language.

Do not test implementation details (private fields, internal method calls, ORM queries). Test behavior through the entity's public API.

## Entity Transitions

```ts
// domain/entities/OrderEntity.ts
export class OrderEntity {
  private status: 'pending' | 'cancelled' = 'pending';

  cancel(reason: string): void {
    if (this.status === 'cancelled') {
      throw new OrderAlreadyCancelledError();
    }
    this.status = 'cancelled';
  }
}

// __tests__/domain/entities/OrderEntity.spec.ts
import { OrderEntity } from '#/domain/entities/OrderEntity';
import { OrderAlreadyCancelledError } from '#/domain/errors/orderErrors';

describe('#OrderEntity', () => {
  describe('.cancel', () => {
    suite('when order is pending', () => {
      it('cancels the order', () => {
        const order = new OrderEntity();

        order.cancel('customer request');

        expect(order.status).toEqual('cancelled');
      });
    });

    suite('when order is already cancelled', () => {
      it('throws OrderAlreadyCancelledError', () => {
        const order = new OrderEntity();
        order.cancel('first cancellation');

        expect(() => order.cancel('second cancellation')).toThrowError(
          OrderAlreadyCancelledError,
        );
      });
    });
  });
});
```

## Value Object Validation

```ts
// domain/value-objects/Email.ts
export class Email {
  readonly value: string;

  constructor(value: string) {
    if (!value.includes('@')) throw new InvalidEmailError(value);
    this.value = value.toLowerCase().trim();
  }
}

// __tests__/domain/value-objects/Email.spec.ts
import { Email } from '#/domain/value-objects/Email';
import { InvalidEmailError } from '#/domain/errors/userErrors';

describe('#Email', () => {
  suite('when value is a valid email address', () => {
    it('creates an Email with the normalised value', () => {
      const email = new Email('  User@Example.com  ');

      expect(email.value).toEqual('user@example.com');
    });
  });

  suite('when value has no @ symbol', () => {
    it('throws InvalidEmailError', () => {
      expect(() => new Email('notanemail')).toThrowError(InvalidEmailError);
    });
  });
});
```

## Commands with In-Memory Fakes

Use in-memory fakes instead of mocks for repository dependencies. A fake keeps tests readable and avoids fragile call-count assertions.

```ts
// __tests__/application/commands/CancelOrderCommand.spec.ts
import {
  CancelOrderCommand,
  CancelOrderCommandHandler,
} from '#/application/commands/CancelOrderCommand';
import { InMemoryOrderRepository } from '#/test-support/fakes/InMemoryOrderRepository';
import { OrderFactory } from '#/test-support/factories/OrderFactory';
import { OrderAlreadyCancelledError } from '#/domain/errors/orderErrors';

describe('#CancelOrderCommandHandler', () => {
  let repository: InMemoryOrderRepository;
  let handler: CancelOrderCommandHandler;

  beforeEach(() => {
    repository = new InMemoryOrderRepository();
    handler = new CancelOrderCommandHandler(repository);
  });

  suite('when order exists and is pending', () => {
    it('persists the cancelled order', async () => {
      const order = OrderFactory.build({ status: 'pending' });
      await repository.save(order);

      await handler.exec(
        new CancelOrderCommand({
          orderId: order.id,
          reason: 'customer request',
        }),
      );

      const saved = await repository.findById(order.id);
      expect(saved?.status).toEqual('cancelled');
    });
  });

  suite('when order is already cancelled', () => {
    it('throws OrderAlreadyCancelledError', async () => {
      const order = OrderFactory.build({ status: 'cancelled' });
      await repository.save(order);

      await expect(
        handler.exec(
          new CancelOrderCommand({
            orderId: order.id,
            reason: 'duplicate',
          }),
        ),
      ).rejects.toThrowError(OrderAlreadyCancelledError);
    });
  });
});
```

## Fakes vs Mocks

Prefer **in-memory fakes** (classes that implement the repository contract using a `Map`) over spy/mock objects for domain and application tests. Fakes keep the test focused on behavior; mocks make tests fragile by asserting internal call sequences.

Only use mocks for true external boundaries: 3rd-party APIs, email gateways, payment providers.
