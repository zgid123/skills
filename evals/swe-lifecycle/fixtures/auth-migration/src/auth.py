"""Authentication adapter backed by the current provider package."""


class AuthProvider:
    def __init__(self, provider):
        self.provider = provider

    def authenticate(self, request):
        return self.provider.verify(request.headers.get("Authorization"))
