import unittest
from area import area


class TestArea(unittest.TestCase):
    def test_correct_arguments(self):
        self.assertEqual(area(2, 5), 10)

    def test_incorrect_arguments(self):
        with self.assertRaises(ValueError):
            area('five', [10, 5])
