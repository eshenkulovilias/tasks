import unittest


def add(x1, x2):
    return x1 + x2


def multiply(x1, x2):
    return x1 * x2


def subtract(x1, x2):
    return x1 - x2


def divide(x1, x2):
    if x2 != 0:
        return x1 / x2


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

