import { useId, type JSX } from 'react';

interface IEmailPreviewProps {
  email: string;
}

export function EmailPreview({ email }: IEmailPreviewProps): JSX.Element {
  const id = useId();
  const descriptionId = `${id}-description`;

  return <p aria-describedby={descriptionId}><span id={descriptionId}>Email: {email}</span></p>;
}
