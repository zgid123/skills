---
name: TypeScript
description: Guidelines for writing TypeScript in Alpha's Projects
---

# Purpose

This skill defines how to write and structure TypeScript so that code is type-safe, readable, and
consistent across Alpha's projects.

# General Principles

- **`@alphacifer/tsconfig`** is **required**. Every project must extend it; do not override or
  loosen options—fix code instead unless the project documents an exception.
- **Prefer types over `any`**: Use precise types, generics, and inference; use `unknown` and narrow
  when the type is dynamic.
- **Explicit over implicit**: Prefer explicit return types on public APIs and exports; rely on
  inference for locals and private helpers.
- **Small, focused modules**: Prefer small files and single responsibility; use barrel exports only
  when they clearly simplify the public API.

# Types and Interfaces

- Use **interfaces** for object shapes that may be extended or implemented; use **type** for unions,
  intersections, mapped types, and aliases.
- Prefer **readonly** and **const** assertions where values should not change.
- Model **nullable** intent explicitly: use `T | null` or optional `?`; avoid optional chaining as a
  substitute for proper null handling in domain logic.
- Prefer **branded types** or **nominal typing** (e.g., branded IDs) over raw primitives when domain
  meaning matters.

```ts
// Do:

// ✅ Interface for object shape; type for union
interface IUser {
  readonly id: TUserId;
  name: string;
}

type TStatus = 'pending' | 'done';

// ✅ Readonly and const where values should not change
const status = { pending: 'pending', done: 'done' } as const;

// ✅ Branded type for domain identity (e.g. IDs)
type TUserId = string & { readonly __brand: unique symbol };

// ✅ Explicit nullable in and out
function find(id: string | null): IUser | null {
  return null;
}

// Don't:

// ❌ Use interface for object shapes, not type
type User = { id: string; name: string };

// ❌ Use readonly / const where value should not change
let statusValue = 'pending';

// ❌ Use branded type for domain IDs, not raw primitive
type UserId = string;

// ❌ Model null explicitly; don't rely on optional chaining
function get(u?: User) {
  return u?.name;
}
```

# Modules and Imports

- **ES modules** only (`import`/`export`); avoid `require` unless integrating with CommonJS.
- **Path resolution**: Use **alias** only when the target is in `compilerOptions.paths`; otherwise
  use **relative**. When importing **across** path roots (e.g. `src/app` → `src/utils`), use the
  alias from `paths`. Follow the prefix the project defines (`~`, `@/`, etc.); match the editor's
  shortest path and keep bundler in sync.

```ts
// Do:

// ✅ Same folder / same root → relative; across roots → alias from paths
// File: src/app/user/user.service.ts
import { IUser } from './user.entity';
import { TUserId } from '../types';
import { formatDate } from '~/utils/date';

// Don't:

// ❌ Same folder: use relative
import { IUser } from '~/app/user/user.entity';

// ❌ Across roots: use alias from paths
import { formatDate } from '../../../utils/date';
```

# Style and Formatting

- **Lint/format**: Use the project's linter and formatter; run the project's check or format script
  when making changes.
- **Naming**: **Interfaces** `I` prefix (e.g. `IUser`, `IUserRepository`); **type aliases** `T`
  prefix (e.g. `TUser`, `TStatus`); **classes** PascalCase; camelCase for functions/variables;
  UPPER_SNAKE for constants when appropriate.
- **Avoid `enum`**; prefer a plain object with `as const` and a T-prefixed type alias.
- Prefer **const** over **let**.
- Prefer **early returns** and **guard clauses** to reduce nesting.
- **`if` and `switch`** must use block braces `{}`; no single-statement form without braces.
- **Objects**: format with one property per line and a trailing comma after the last property.

```ts
// Do:

// ✅ Prefer const over let
const maxRetries = 3;

// ✅ Plain object + as const, not enum
const status = {
  pending: 'pending',
  done: 'done',
} as const;
type TStatus = (typeof status)[keyof typeof status];

// ✅ Early return; if/switch use {}; object one property per line + trailing comma
async function handleUser(user: IUser | null) {
  if (!user) {
    return {
      ok: false,
      error: new Error('Not found'),
    };
  }
  await process(user);
}

function getLabel(value: number) {
  switch (value) {
    case 1: {
      return 'one';
    }
    default: {
      return 'other';
    }
  }
}

// Don't:

// ❌ Use const when value does not change
let maxRetries = 3;

// ❌ Use plain object + as const, not enum
enum StatusEnum {
  Pending,
  Done,
}

// ❌ Use early return instead of nested if/else
async function handleUserNested(user: IUser | null) {
  if (user) {
    await process(user);
  } else {
    return {
      ok: false,
      error: new Error('Not found'),
    };
  }
}

// ❌ if/switch must use {} — no single-statement without braces
if (flag) doSomething();
switch (x) {
  case 1:
    return 'a';
}

// ❌ Object: one property per line + trailing comma
return { ok: false, error: new Error('Not found') };
```

# Testing and Tooling

- Use the project's test runner and assertion style (see `skills/testing/SKILL.md`); prefer typed
  helpers and factories.
- All tsconfig files must extend **`@alphacifer/tsconfig`**; add only project-specific overrides
  (e.g. `include`, `outDir`).
