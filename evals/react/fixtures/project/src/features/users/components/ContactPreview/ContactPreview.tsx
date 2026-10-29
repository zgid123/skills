import { useId, type JSX } from 'react';

interface IContactPreviewProps {
  email: string;
}

export function ContactPreview({ email }: IContactPreviewProps): JSX.Element {
  const id = useId();
  const descriptionId = `${id}-description`;

  return <p aria-describedby={descriptionId}><span id={descriptionId}>Contact: {email}</span></p>;
}
