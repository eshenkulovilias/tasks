import unittest
from tovar import func


class TestTovar(unittest.TestCase):
    def test_tov(self):
        self.assertEqual(func(50, 32), "Чек оплачен")

    def test_tova(self):
        self.assertEqual(func(50, 56), "99 рублей недостаточно")
