import { OrderEntity } from '../../domain/OrderEntity';

describe('#OrderEntity', () => {
  describe('.cancel', () => {
    suite('when the order has shipped', () => {
      it('rejects cancellation', () => {
        const subject = new OrderEntity({
          id: 'order-1',
          status: 'shipped',
        });

        expect(() => subject.cancel({
          reason: 'Changed my mind',
        })).toThrow('Only pending orders');
      });
    });
  });
});
