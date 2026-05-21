---
name: TypeScript Style
description: Naming and formatting guidelines for Alpha's TypeScript projects
---

# Style and Formatting

- Use the project's linter and formatter; run the project's check or format script when making changes.
- Prefix **interfaces** with `I`, for example `IUser` or `IUserRepository`.
- Prefix **type aliases** with `T`, for example `TUser` or `TStatus`.
- Use PascalCase for classes, camelCase for functions/variables, and UPPER_SNAKE for constants when appropriate.
- Avoid `enum`; prefer a plain object with `as const` and a T-prefixed type alias.
- Prefer `const` over `let`.
- Define private class fields and methods with ECMAScript `#private` syntax instead of the TypeScript `private` keyword.
- Prefer early returns and guard clauses to reduce nesting.
- Conditions must always use block braces `{}`; do not use single-statement form without braces.
- Format objects with one property per line and a trailing comma after the last property.
- When passing an object parameter to a function, always put it on multiple lines, even with one property. Put each property on its own line, include a trailing comma, and sort properties by key length from shortest to longest.
- In callbacks, use concise arrow returns only for short expressions; use a block body with `return` when returning a multi-line object or doing non-trivial mapping.

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

// ✅ Conditions always use block braces
if (a) {
  return 1;
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

// ✅ Object parameters are multi-line and sorted by key length
const user = await userRepository.findById({
  id: userId,
});

await emailService.sendWelcomeEmail({
  to: user.email,
  locale: user.locale,
  userName: user.name,
});

// ✅ Private class fields and methods use #private syntax
class UserService {
  readonly #userRepository: IUserRepository;

  public constructor(params: IUserServiceParams) {
    this.#userRepository = params.userRepository;
  }

  public async find(params: IFindUserParams): Promise<IUser | null> {
    return this.#findById(params.id);
  }

  async #findById(id: TUserId): Promise<IUser | null> {
    return this.#userRepository.findById(id);
  }
}

// ✅ Use block body + return for multi-line object mapping
const orderSummaries = orders.map((order) => {
  return {
    id: order.id,
    customerName: order.customer.name,
    total: order.items.reduce((sum, item) => {
      return sum + item.price * item.quantity;
    }, 0),
  };
});
```

```ts
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

// ❌ Conditions must not use single-statement form without braces
if (a) return 1;
if (flag) doSomething();
switch (x) {
  case 1:
    return 'a';
}

// ❌ Object: one property per line + trailing comma
return { ok: false, error: new Error('Not found') };

// ❌ Object parameters must not be inline, even with one property
const user = await userRepository.findById({ id: userId });

// ❌ Object parameters must not be sorted longest-first
await emailService.sendWelcomeEmail({
  userName: user.name,
  locale: user.locale,
  to: user.email,
});

// ❌ Do not use TypeScript private keyword for class internals
class UserService {
  private readonly userRepository: IUserRepository;

  public constructor(params: IUserServiceParams) {
    this.userRepository = params.userRepository;
  }

  public async find(params: IFindUserParams): Promise<IUser | null> {
    return this.findById(params.id);
  }

  private async findById(id: TUserId): Promise<IUser | null> {
    return this.userRepository.findById(id);
  }
}

// ❌ Do not force long object mappings into concise arrow returns
const orderSummaries = orders.map((order) => ({
  id: order.id,
  customerName: order.customer.name,
  total: order.items.reduce((sum, item) => sum + item.price * item.quantity, 0),
}));
```
