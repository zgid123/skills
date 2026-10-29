export interface IInvoiceSummary {
  id: string;
  total: number;
  status: 'open' | 'paid';
}

interface IListInvoiceParams {
  status: 'open' | 'paid';
}

export interface IInvoiceProjection {
  list(params: IListInvoiceParams): Promise<readonly IInvoiceSummary[]>;
}
