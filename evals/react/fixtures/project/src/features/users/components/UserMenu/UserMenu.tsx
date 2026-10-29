import type { JSX } from 'react';

import { useMenu } from './hooks';

export function UserMenu(): JSX.Element {
  const { isOpen, toggle } = useMenu();

  return <button onClick={toggle}>{isOpen ? 'Close menu' : 'Open menu'}</button>;
}
