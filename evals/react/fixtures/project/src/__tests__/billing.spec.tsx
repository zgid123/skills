import { renderToStaticMarkup } from 'react-dom/server';

import BillingPage from '../../app/billing/page';

describe('#BillingPage', () => {
  suite('when rendered', () => {
    it('renders the billing page', () => {
      expect(renderToStaticMarkup(<BillingPage />)).toContain('Billing');
    });
  });
});
