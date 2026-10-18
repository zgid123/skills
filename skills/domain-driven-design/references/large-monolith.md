# Modular Monolith Structure

Use business modules inside one deployable server. This layout applies to a monolith from its first meaningful module; it does not require many domains. The examples use `apps/<app-name>` as a placeholder. Follow the repository layout and application name, such as `workspaces/<project-name>` for monorepo applications or `services/<project-name>` for microservices; these directory names do not determine deployment boundaries. Create only the layers and technologies currently needed.

In a TypeScript monorepo, keep reusable domain code in `packages/@domain/<context>` and API contracts in `packages/@contracts/<context>`. The server module owns application use cases, concrete infrastructure, and adapters. Do not duplicate the domain in `src/modules/<context>/domain/` when a workspace domain package already owns it. For a standalone server without domain packages, a module-local `domain/` is appropriate.

## Layout

The following Hono monolith example illustrates ownership within an application:

```txt
packages/
  @domain/
    auth/
      src/
        constants/
        entities/
        errors/
        repositories/
        services/
        index.ts
  @contracts/
    auth/
      src/
        errors/
        schemas/
          internal/
          public/
        viewModels/
          internal/
        index.ts
apps/
  <app-name>/
    drizzle.config.ts
    src/
      index.ts
      migrate.ts
      adapters/
        restful/
          context.ts
          wire.ts
          hono/
            index.ts
            endpoints/
              base.ts
              internal.ts
              v1.ts
              index.ts
      infrastructure/
        common/
          env.ts
          loadEnv.ts
        drizzle/
          config.ts
          instance.ts
          migrations/
          seeds/
            index.ts
      modules/
        auth/
          application/
            commands/
            queries/
          adapters/
            restful/
              context.ts
              wire.ts
              hono/
                middlewares/
                internal/
                  users.ts
                public/
                  v1/
                    auth.ts
          infrastructure/
            drizzle/
              schemas/
              repositories/
              seeds/
            betterAuth/
              instance.ts
              services/
                UserProvisioner.ts
          __tests__/
            application/
            adapters/
            infrastructure/
            factories/
      __tests__/
        setup.ts
        adapters/
```

This tree describes ownership, not a scaffold checklist. Add a second module, another API version, or another technology only when required.

## Root Composition and Module Ownership

| Concern | Root server responsibility | Module responsibility |
|---|---|---|
| Transport | Create the app/server, install common middleware and error handling, mount module routes | Define business routes, transport mapping, module middleware, and context types |
| Wiring | Create shared clients and CQRS bus; call module wiring functions | Construct repositories and technical services; inject them into handlers and register messages |
| Persistence | Compose module schemas into the shared client type and instance | Own tables, relations, schemas, and concrete repositories |
| Migrations | Generate and run migrations for the shared database in one root migration history | Expose schema locations to the root migration configuration |
| Seeds | Call each module seed entrypoint | Own business seed data and seed execution for the module |
| Configuration | Load environment and process-wide configuration | Own technology integrations specific to the module |
| Tests | Shared test setup and app-level endpoint tests | Tests mirroring the module's application, infrastructure, and adapters |

Keep business schemas and seed data under `modules/<context>/infrastructure/<technology>/`. Root `infrastructure/drizzle/config.ts` imports module schema exports and composes them into one schema and `TDrizzle`. Root `drizzle.config.ts` points generation at module schema locations and writes generated migrations to `src/infrastructure/drizzle/migrations/`. Root `seeds/index.ts` delegates to module seed functions. Register a new module in each applicable composition point; moving its tables or seed data to root infrastructure would obscure ownership.

Root infrastructure owns shared connections, not every technical instance. A module-specific integration such as Better Auth belongs in `modules/auth/infrastructure/betterAuth/`, even when it uses the shared database client.

## Transport Composition

Root `adapters/restful/hono/index.ts` owns `createApp()` and server lifecycle. Root `adapters/restful/hono/endpoints/` composes the routing surface:

- `base.ts` defines app-level endpoints such as health checks.
- `v1.ts` mounts module public `v1` endpoints under the root `/api/v1` route.
- `internal.ts` mounts module internal endpoints under `/api/internal`.
- `index.ts` combines these groups and applies middleware in the required order.

Module endpoints remain under `modules/<context>/adapters/restful/hono/internal/` or `public/v1/`. Keep public versioning in adapters and leave internal routes unversioned by default. Do not create duplicate root `public/v1/` and `internal/` directories when the project uses `endpoints/v1.ts` and `endpoints/internal.ts` for composition.

Scope middleware deliberately. The reference server mounts public auth routes before authenticated internal routes; preserving registration order prevents public routes from accidentally requiring an authenticated session. Apply access controls to the route groups that need them.

Module context types declare the dependencies and request values their routes use, such as `cqrsx` and `currentUser`. Root context composes the app container and common request variables. Keep Hono contexts out of application handlers and domain objects.

## Explicit Wiring

Root `adapters/restful/wire.ts` receives the shared CQRS bus and database client, calls `wireAuth({ cqrsx, drizzle })` and other module wiring functions, and returns the app container. Module `adapters/restful/wire.ts` constructs concrete collaborators, injects them through named parameter objects, and registers each message/handler pair on that bus. Register once per app instance, not on each request, and do not create a separate bus per module by default.

Application handlers depend on `@domain/<context>` contracts rather than concrete repositories or integration singletons. For example, `CreateUserCommandHandler` receives `IUserProvisioner` from `@domain/auth`; `UserProvisioner` implements it using Better Auth under module infrastructure. Keep the provider API, credential handling, and provider error translation behind that boundary instead of having the handler write provider-owned tables directly.

Composition code may import concrete infrastructure to assemble the application. This is the reason `wire.ts` can know about Drizzle and Better Auth while handlers remain independent of those implementations.

## Adding a Module

1. Add the domain package and shared API contracts only as needed; declare workspace dependencies and use package imports.
2. Add module commands/queries with co-located handlers, infrastructure implementations, routes, and module wiring.
3. Register the module in root wiring and endpoint composition.
4. Compose its schemas and seed entrypoint into root database setup when it owns persisted data; generate migrations in the shared root history.
5. Put domain tests in the domain package and server tests beside the owning module. Follow the testing skill: routes/controllers use `*.e2e.ts`; repositories use infrastructure integration coverage.

Keep this as one deployment. Do not add network boundaries, per-module databases, generic registries, or dependency injection frameworks merely because modules exist.
