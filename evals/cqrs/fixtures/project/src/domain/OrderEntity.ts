interface IOrderParams {
  id: string;
  status?: 'pending' | 'shipped' | 'cancelled';
}

interface ICancelOrderParams {
  reason: string;
}

export class OrderEntity {
  public readonly id: string;
  public status: 'pending' | 'shipped' | 'cancelled';
  public cancellationReason: string | null = null;

  public constructor({ id, status = 'pending' }: IOrderParams) {
    this.id = id;
    this.status = status;
  }

  public cancel({ reason }: ICancelOrderParams): void {
    if (this.status !== 'pending' || reason.trim().length === 0) {
      throw new Error('Only pending orders with a reason can be cancelled');
    }

    this.status = 'cancelled';
    this.cancellationReason = reason;
  }
}
