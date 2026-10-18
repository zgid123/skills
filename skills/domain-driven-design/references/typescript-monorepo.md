# TypeScript Monorepo Domains

For TypeScript monorepos, keep the domain in a local package so it can stay framework-free and be reused by apps, workers, tests, and adapters. The examples use `apps/<app-name>` as a placeholder, not a required directory convention. Follow the repository layout, such as `workspaces/<project-name>` for monorepo applications or `services/<project-name>` for microservices; neither the parent directory nor the application name is prescribed by DDD. Read [Modular Monolith Structure](./large-monolith.md) for root composition and module ownership.

Use this layout when creating a new TypeScript bounded context:

```txt
packages/
  @domain/
    <business-domain>/
      src/
        constants/
        entities/
        errors/
        services/
        repositories/
        index.ts
      package.json

apps/
  <app-name>/
    src/
      modules/
        <bounded-context>/
          application/
            commands/
            queries/
          infrastructure/
            drizzle/
              schemas/
              seeds/
              repositories/
            mongoose/
              repositories/
            redis/
              repositories/
            security/
          adapters/
            restful/
              context.ts
              wire.ts
              hono/
                internal/
                public/
                  v1/
                  v2/
            graphql/
            grpc/
```

Shared API contracts live alongside domain packages when multiple applications consume them:

```txt
packages/
  @contracts/
    <business-domain>/
      src/
        schemas/
          internal/
          public/
        viewModels/
          internal/
        errors/
        index.ts
```

Use contracts for transport validation and response view models, with visibility/version organization as the API requires. Adapters consume those schemas and serialize application results; domain entities do not depend on the API contracts package. Keep business validation and transitions in the domain even when a request schema validates input shape. A query may return domain entities when appropriate; the adapter still controls what is exposed through the response view model.

Rules for TypeScript monorepos:

- The domain package must not import from apps, adapters, infrastructure, ORM libraries, HTTP frameworks, GraphQL libraries, or environment configuration.
- Export only intentional domain APIs from the domain package entrypoint. Declare subpath exports such as `@domain/auth/constants` when error metadata is intentionally shared through the contracts package; do not expose internal implementation paths.
- Keep repository and capability contracts in the domain package when they are part of the domain boundary, such as `IUserRepository` in `repositories/` and `IUserProvisioner` in `services/`.
- Put concrete repository implementations in the app or infrastructure package that owns the persistence technology instance.
- Application commands and queries may depend on the domain package, repository contracts, and `@cqrsx/core`.
- Adapters call application commands and queries; they should not call ORM repositories directly.
- Infrastructure implements domain/application contracts and maps ORM records to domain objects.

## Referencing the Domain Package

Reference the domain through the workspace package name. In a monorepo, a workspace package should be consumed like a normal package after it is declared as a workspace dependency.

Use a package name and folder path that match the repo convention:

```txt
packages/
  @domain/
    orders/
      package.json
      src/
        index.ts
```

```json
{
  "name": "@domain/orders",
  "private": true,
  "type": "module",
  "exports": {
    ".": "./src/index.ts"
  }
}
```

Then declare it as a workspace dependency from the app or package that needs it:

```json
{
  "dependencies": {
    "@domain/orders": "workspace:*"
  }
}
```

Application, infrastructure, and adapter code should import from the package entrypoint:

```ts
import { type IOrderRepository, OrderEntity, OrderError } from '@domain/orders';
```

Do not import domain code through relative paths into `packages/`, and do not add `tsconfig` path aliases to fake package imports. The package manager workspace should link `@domain/orders` like any other dependency.

Do not make the domain package depend on the app to solve wiring. In the monolith, root `adapters/restful/wire.ts` calls module wiring functions using the shared bus and client. A module's `adapters/restful/wire.ts` constructs its repositories and registers handlers:

```ts
import type { Cqrsx } from '@cqrsx/core';

import type { TDrizzle } from '#/infrastructure/drizzle/config';

import {
  CancelOrderCommand,
  CancelOrderCommandHandler,
} from '../../application/commands';
import { OrderRepository } from '../../infrastructure/drizzle/repositories';

export interface IWireOrdersParams {
  readonly cqrsx: Cqrsx;
  readonly drizzle: TDrizzle;
}

export function wireOrders({ cqrsx, drizzle }: IWireOrdersParams): void {
  const orderRepository = new OrderRepository({
    drizzle,
  });

  cqrsx.register(
    CancelOrderCommand,
    new CancelOrderCommandHandler({
      orderRepository,
    }),
  );
}
```

Do not create a new bus inside each module or import infrastructure instances inside application handlers. Keep concrete dependencies at composition boundaries.

For other languages, preserve the same dependency rules even if the physical layout differs. Use the language's normal module/package conventions instead of forcing the TypeScript monorepo layout.
