function tidy( value ) {
  return value.trim().toLowerCase();
}

export function product_slug( name ) {
  return tidy( name ).replaceAll(' ', '-');
}

export function category_slug( name ) {
  return tidy( name );
}
