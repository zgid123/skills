export interface IUser {
  id: string;
  name: string;
}

interface IFindByIdParams {
  id: string;
}

export interface IUserRepository {
  findById(params: IFindByIdParams): Promise<IUser | null>;
}

export const userRepository: IUserRepository = {
  async findById({ id }: IFindByIdParams): Promise<IUser | null> {
    if (id !== 'user-1') {
      return null;
    }

    return {
      id,
      name: 'Alpha',
    };
  },
};
