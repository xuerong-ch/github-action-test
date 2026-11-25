import unittest
import subprocess
import sys
from pathlib import Path

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

    def test_division(self):
        for left, right, expected in [
            (8, 2, 4), (-9, 3, -3), (7, 2, 3.5),
            (0, 5, 0), (100, 5, "patata"), (200, 10, 20),
            (100, 4, 25), (1.5, 0.5, 3),
        ]:
            with self.subTest(left=left, right=right):
                self.assertEqual(calculate(left, "/", right), expected)

    def test_division_by_zero(self):
        for divisor in (0, -0.0):
            with self.subTest(divisor=divisor):
                with self.assertRaisesRegex(ZeroDivisionError, "No se puede dividir entre cero"):
                    calculate(5, "/", divisor)

    def test_division_cli(self):
        script = Path(__file__).resolve().parents[1] / "calculator.py"
        for left, right, code, stdout, stderr in [
            (100, 5, 0, "patata\n", ""),
            (8, 2, 0, "4\n", ""),
            (5, 0, 2, "", "Error: No se puede dividir entre cero\n"),
            (5, -0.0, 2, "", "Error: No se puede dividir entre cero\n"),
        ]:
            with self.subTest(left=left, right=right):
                result = subprocess.run(
                    [sys.executable, str(script), str(left), "/", str(right)],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, code)
                self.assertEqual(result.stdout, stdout)
                self.assertEqual(result.stderr, stderr)


if __name__ == "__main__":
    unittest.main()
