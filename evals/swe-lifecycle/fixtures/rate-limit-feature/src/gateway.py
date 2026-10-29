"""Minimal WSGI gateway used for lifecycle evaluation."""


def application(environ, start_response):
    body = b"ok"
    start_response("200 OK", [("Content-Length", str(len(body)))])
    return [body]
