export interface IProfile {
  id: string;
  firstName: string;
  lastName: string;
  status: string;
  createdAt: string;
  externalId?: string;
}

interface IListProfilesParams {
  load: () => Promise<readonly IProfile[]>;
}

// This older implementation is intentionally compressed; the requested task touches it.
export async function listProfiles({ load }: IListProfilesParams): Promise<readonly IProfile[]> {
  const profiles = await load();
  return profiles.map((profile) => ({ externalId: profile.externalId, createdAt: profile.createdAt, lastName: profile.lastName, id: profile.id, status: profile.status, firstName: profile.firstName }));
}
