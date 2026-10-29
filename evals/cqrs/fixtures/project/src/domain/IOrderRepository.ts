import type { OrderEntity } from './OrderEntity';

interface IFindOrderParams {
  id: string;
}

interface ISaveOrderParams {
  order: OrderEntity;
}

export interface IOrderRepository {
  findById(params: IFindOrderParams): Promise<OrderEntity | null>;
  save(params: ISaveOrderParams): Promise<void>;
}
