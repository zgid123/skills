"""Authentication token verifier before its source rename."""


def accepts(token, expected):
    return token == expected
