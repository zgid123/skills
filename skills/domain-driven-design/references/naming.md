# DDD File Naming — TypeScript

These rules apply to all TypeScript projects that follow Alpha's DDD structure. The folder already provides the technology or layer context, so file names only need to describe the business concept.

## Domain Layer

### Entities

Files in `domain/entities/` use the suffix `Entity`:

```txt
domain/
  entities/
    UserEntity.ts
    OrderEntity.ts
    InvoiceEntity.ts
```

### Repository Contracts

Files in `domain/repositories/` use the `I` prefix (interface) and `Repository` suffix. No technology name in the contract — the interface belongs to the domain, not to any implementation:

```txt
domain/
  repositories/
    IUserRepository.ts
    IOrderRepository.ts
```

```ts
// ✅ domain/repositories/IAuthRepository.ts
export interface IAuthRepository {
  findById(id: string): Promise<UserEntity | null>;
  save(user: UserEntity): Promise<void>;
}

// ❌ AuthRepository.ts — missing the I prefix; this looks like an implementation
// ❌ auth-repository.ts — kebab-case; use PascalCase with the I prefix
// ❌ auth.repository.ts — dot-separated; use PascalCase with the I prefix
```

### Errors

Group all errors for a domain concept into a single file named `<domain>Errors.ts` — **camelCase**, because the file is a module that exports multiple classes, not a single class. PascalCase is reserved for files that export exactly one class whose name matches the file.

```txt
domain/
  errors/
    userErrors.ts
    orderErrors.ts
    authErrors.ts
```

```ts
// ✅ domain/errors/userErrors.ts
export class UserNotFoundError extends Error {
  constructor(id: string) {
    super(`User ${id} not found`);
    this.name = 'UserNotFoundError';
  }
}

export class UserAlreadyExistsError extends Error {
  constructor(email: string) {
    super(`User with email ${email} already exists`);
    this.name = 'UserAlreadyExistsError';
  }
}

// ❌ UserErrors.ts — PascalCase implies a single exported class matching the file name
// ❌ UserNotFoundError.ts, UserAlreadyExistsError.ts — one file per error is too scattered; group by domain
// ❌ user-errors.ts — kebab-case; use camelCase for multi-export modules
```

### Value Objects

Files in `domain/value-objects/` use the suffix `ValueObject` unless the project has a consistent alternative:

```txt
domain/
  value-objects/
    EmailValueObject.ts
    MoneyValueObject.ts
```

---

## Application Layer

### Commands

Files in `application/commands/` use the suffix `Command`:

```txt
application/
  commands/
    SignInCommand.ts
    CancelOrderCommand.ts
    CreateInvoiceCommand.ts
```

### Queries

Files in `application/queries/` use the suffix `Query`:

```txt
application/
  queries/
    GetUserQuery.ts
    ListOrdersQuery.ts
    GetInvoiceSummaryQuery.ts
```

---

## Infrastructure Layer

Infrastructure repository implementations live inside the technology folder, which already provides context. Do not repeat the technology name in the file name:

```txt
infrastructure/
  drizzle/
    repositories/
      AuthRepository.ts      ✅ folder says "drizzle", file says the domain
      UserRepository.ts
  mongoose/
    repositories/
      SessionRepository.ts   ✅ folder says "mongoose", file says the domain
  redis/
    repositories/
      TokenRepository.ts     ✅ folder says "redis", file says the domain
```

```ts
// ✅ infrastructure/drizzle/repositories/AuthRepository.ts
export class AuthRepository implements IAuthRepository { ... }

// ❌ DrizzleAuthRepository.ts — technology prefix is redundant; the folder provides it
// ❌ drizzle-auth.repository.ts — kebab-case + dot-separated; use PascalCase
// ❌ auth.repository.ts — dot-separated; use PascalCase
```

---

## Barrel Exports

Add an `index.ts` barrel at the **content folder level** — the leaf directories that hold the actual files. Do not add a barrel at the layer level (`domain/`, `application/`, `infrastructure/`).

```txt
domain/
  entities/
    index.ts        ✅ barrel for entities
    OrderEntity.ts
    UserEntity.ts
  errors/
    index.ts        ✅ barrel for errors
    orderErrors.ts
    userErrors.ts
  repositories/
    index.ts        ✅ barrel for repository contracts
    IOrderRepository.ts
    IUserRepository.ts
  index.ts          ❌ no barrel at the domain layer root

application/
  commands/
    index.ts        ✅ barrel for commands
    CancelOrderCommand.ts
    CreateOrderCommand.ts
  queries/
    index.ts        ✅ barrel for queries
    GetOrderQuery.ts
  index.ts          ❌ no barrel at the application layer root

infrastructure/
  drizzle/
    repositories/
      index.ts      ✅ barrel for drizzle repositories
      OrderRepository.ts
  index.ts          ❌ no barrel at the infrastructure layer root
```

The layer-level barrel (`domain/index.ts`) is omitted intentionally. It would aggregate everything in the domain into one re-export surface, making it easy to accidentally couple consumers to the wrong layer. Each content folder's barrel is enough — consumers import from the folder they actually need:

```ts
// ✅ Import from the content folder barrel
import { OrderEntity } from '#/domain/entities';
import { IOrderRepository } from '#/domain/repositories';
import { CancelOrderCommand } from '#/application/commands';

// ❌ Never import through a layer barrel
import { OrderEntity, IOrderRepository } from '#/domain';
import { CancelOrderCommand } from '#/application';
```

---

## Summary Table

| Layer | Folder | Pattern | Example |
|---|---|---|---|
| Entity | `domain/entities/` | `<Name>Entity.ts` | `OrderEntity.ts` |
| Repository contract | `domain/repositories/` | `I<Name>Repository.ts` | `IOrderRepository.ts` |
| Domain error group | `domain/errors/` | `<domain>Errors.ts` | `userErrors.ts` |
| Value object | `domain/value-objects/` | `<Name>ValueObject.ts` | `EmailValueObject.ts` |
| Command | `application/commands/` | `<Feature>Command.ts` | `CancelOrderCommand.ts` |
| Query | `application/queries/` | `<Feature>Query.ts` | `ListOrdersQuery.ts` |
| Infra repository | `infrastructure/<tech>/repositories/` | `<Name>Repository.ts` | `AuthRepository.ts` |
