interface IFormatNameParams {
  name: string;
}

export class UserName {
  public format({ name }: IFormatNameParams): string {
    return name;
  }
}
