import { userRepository } from '../users';

describe('#userRepository', () => {
  suite('when the user exists', () => {
    it('loads the user', async () => {
      const user = await userRepository.findById({
        id: 'user-1',
      });

      expect(user?.name).toEqual('Alpha');
    });
  });
});
