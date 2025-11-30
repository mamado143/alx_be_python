#!/usr/bin/python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ----- ADDITION TESTS -----
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(5, -2), 3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertEqual(self.calc.add(7, 0), 7)

    # ----- SUBTRACTION TESTS -----
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    # ----- MULTIPLICATION TESTS -----
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(5, -2), -10)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # ----- DIVISION TESTS -----
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_float_result(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_divide_positive_and_negative(self):
        self.assertEqual(self.calc.divide(10, -2), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
