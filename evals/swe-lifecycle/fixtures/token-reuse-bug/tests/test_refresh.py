import unittest

from src.refresh import RefreshTokens


class RefreshTokenTests(unittest.TestCase):
    def test_rotation_rejects_a_replayed_token(self):
        tokens = RefreshTokens()
        replacement = tokens.rotate("session-1", "refresh-a")
        self.assertEqual(replacement, "refresh-a-next")
        self.assertIsNone(tokens.rotate("session-1", "refresh-a"))

    def test_rotation_rejects_an_unrelated_token(self):
        tokens = RefreshTokens()
        self.assertIsNone(tokens.rotate("session-1", "other"))
        self.assertEqual(tokens.active["session-1"], {"refresh-a"})


if __name__ == "__main__":
    unittest.main()
