import unittest

from src.convert import convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert(0, "C"), 32)


if __name__ == "__main__":
    unittest.main()
