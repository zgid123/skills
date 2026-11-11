# BEM

Use BEM when requested or already established. It is independent of stylesheet scoping; global CSS does not automatically require BEM, and CSS Modules may optionally use it.

## Naming

- Use `block`, `block__element`, `block--modifier`, and `block__element--modifier` with kebab-case words, unless the existing project uses another BEM convention.
- Name a block for its responsibility, an element for its role within that block, and a modifier for a meaningful state or variation. Prefer `product-card` to a presentation-specific name such as `blue-box`.
- Keep element names flat relative to their block. Use `product-card__title`, not `product-card__header__title`; DOM nesting does not create a chain of BEM elements.
- Apply a modifier alongside its base class. Use `product-card product-card--featured` and `product-card__action product-card__action--disabled` rather than replacing the base class.
- Keep selectors class-based and shallow. A block's name supplies context without requiring a selector tied to its exact DOM ancestry.

Keep the modifier alongside its base class and name nested elements relative to the block, not their DOM parent:

```html
<!-- DO: retain the base class and use a flat element name. -->
<article class="product-card product-card--featured">
  <header class="product-card__header">
    <h2 class="product-card__title">Trail pack</h2>
  </header>
</article>
```

```html
<!-- DON'T: omit the base class or encode DOM nesting in element names. -->
<article class="product-card--featured">
  <header class="product-card__header">
    <h2 class="product-card__header__title">Trail pack</h2>
  </header>
</article>
```

When changing existing names, update all associated markup, selectors, and references within scope. Do not rename unrelated blocks. For optional BEM inside CSS Modules, also read the [CSS Modules reference](css-modules.md).

Source: [BEM naming documentation](https://github.com/getbem/getbem.github.io/blob/master/src/pages/naming.mdx).
