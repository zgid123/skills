import { useState } from 'react';

interface IUseMenuResult {
  isOpen: boolean;
  toggle: () => void;
}

export function useMenu(): IUseMenuResult {
  const [isOpen, setIsOpen] = useState(false);

  return {
    isOpen,
    toggle: () => {
      setIsOpen((current) => !current);
    },
  };
}
