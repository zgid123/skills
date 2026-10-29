import unittest

from src.gateway import application


class GatewayTests(unittest.TestCase):
    def test_gateway_returns_ok(self):
        response = {}

        def start_response(status, headers):
            response["status"] = status
            response["headers"] = dict(headers)

        self.assertEqual(application({}, start_response), [b"ok"])
        self.assertEqual(response["status"], "200 OK")


if __name__ == "__main__":
    unittest.main()
