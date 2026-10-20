# DDD File Naming — TypeScript

These rules apply to all TypeScript projects that follow Alpha's DDD structure. The folder already provides the technology or layer context, so file names only need to describe the business concept.

## Domain Layer

The examples use a local `domain/` folder. In a monorepo domain package, apply the same names under `packages/@domain/<context>/src/` instead.

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
export interface IFindUserParams {
  id: string;
}

export interface ISaveUserParams {
  user: UserEntity;
}

export interface IAuthRepository {
  findById(params: IFindUserParams): Promise<UserEntity | null>;
  save(params: ISaveUserParams): Promise<void>;
}

// ❌ AuthRepository.ts — missing the I prefix; this looks like an implementation
// ❌ auth-repository.ts — kebab-case; use PascalCase with the I prefix
// ❌ auth.repository.ts — dot-separated; use PascalCase with the I prefix
```

### Errors

Each domain concept gets one error class in its own **PascalCase** file. The file name matches the exported class name exactly.

```txt
packages/@domain/auth/src/
  errors/
    AuthError.ts
    UserError.ts
    index.ts
  constants/
    authErrors.ts
    userErrors.ts
    index.ts
```

Keep error codes, names, and message constants in `constants/<concept>Errors.ts`, alongside `errors/`. Error classes use the framework-free `ApplicationError` from `@domain/core`; do not import `HonoError` or HTTP framework libraries into the domain package.

```ts
// packages/@domain/auth/src/constants/authErrors.ts
export const UNAUTHORIZED_CODE = 10_000;
export const UNAUTHORIZED_NAME = 'UNAUTHORIZED';
export const UNAUTHORIZED_MESSAGE = 'Unauthorized';
```

```ts
// packages/@domain/auth/src/errors/AuthError.ts
import { ApplicationError } from '@domain/core';

import {
  UNAUTHORIZED_CODE,
  UNAUTHORIZED_MESSAGE,
  UNAUTHORIZED_NAME,
} from '../constants/authErrors';

export class AuthError extends ApplicationError {
  public static unauthorized(): AuthError {
    return new AuthError({
      code: UNAUTHORIZED_CODE,
      name: UNAUTHORIZED_NAME,
      message: UNAUTHORIZED_MESSAGE,
      httpCode: 401,
    });
  }
}
```

The reference project's framework-free base error carries `httpCode` metadata. Preserve that established contract without coupling errors to Hono; the transport error handler interprets it. Follow existing code ranges rather than assigning arbitrary new codes.

Keep `errors/index.ts` for error classes and `constants/index.ts` for constants. When clients need error metadata, expose an intentional package subpath such as `@domain/auth/constants` and re-export it through `@contracts/auth` rather than exporting server error implementations to clients. This replaces the older convention that restricted constants to `errors/constants/`.

Use `AuthError.ts` for one error class, not `authErrors.ts`, `AuthErrors.ts`, or `auth-error.ts`.

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

In TypeScript projects, command classes extend `Command` from `@cqrsx/core`, and their handler classes live in the same file. For example, `CancelOrderCommand.ts` exports both `CancelOrderCommand` and `CancelOrderCommandHandler`. Do not create a separate `CancelOrderCommandHandler.ts` file.

### Queries

Files in `application/queries/` use the suffix `Query`:

```txt
application/
  queries/
    GetUserQuery.ts
    ListOrdersQuery.ts
    GetInvoiceSummaryQuery.ts
```

In TypeScript projects, query classes extend `Query<TResult>` from `@cqrsx/core`, and their handler classes live in the same file. For example, `GetInvoiceSummaryQuery.ts` exports both `GetInvoiceSummaryQuery` and `GetInvoiceSummaryQueryHandler`. Do not create a separate `GetInvoiceSummaryQueryHandler.ts` file.

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

Add an `index.ts` barrel at the **content folder level** — the leaf directories that hold the actual files. Do not add a barrel at the app-local layer level (`domain/`, `application/`, `infrastructure/`). A workspace package entrypoint such as `packages/@domain/auth/src/index.ts` is an intentional public API and is required when the package exports it; it is not an app-local layer barrel.

```txt
domain/
  entities/
    index.ts        ✅ barrel for entities
    OrderEntity.ts
    UserEntity.ts
  errors/
    index.ts        ✅ barrel for error classes
    OrderError.ts
    UserError.ts
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
| --- | --- | --- | --- |
| Entity | `domain/entities/` | `<Name>Entity.ts` | `OrderEntity.ts` |
| Repository contract | `domain/repositories/` | `I<Name>Repository.ts` | `IOrderRepository.ts` |
| Domain error class | `domain/errors/` | `<Name>Error.ts` | `UserError.ts` |
| Domain error constants | `domain/constants/` or domain package `src/constants/` | `<domain>Errors.ts` | `authErrors.ts` |
| Value object | `domain/value-objects/` | `<Name>ValueObject.ts` | `EmailValueObject.ts` |
| Command | `application/commands/` | `<Feature>Command.ts` | `CancelOrderCommand.ts` |
| Query | `application/queries/` | `<Feature>Query.ts` | `ListOrdersQuery.ts` |
| Infra repository | `infrastructure/<tech>/repositories/` | `<Name>Repository.ts` | `AuthRepository.ts` |
