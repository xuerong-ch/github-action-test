import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_supported_operations(self):
        for left, operator, right, expected in [
            (2, "+", 3, 5), (2, "-", 5, -3),
            (-2, "*", 3, -6), (1.5, "+", 2.25, 3.75),
        ]:
            with self.subTest(operator=operator, left=left, right=right):
                self.assertEqual(calculate(left, operator, right), expected)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(2, "%", 3)


if __name__ == "__main__":
    unittest.main()
