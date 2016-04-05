import unittest
from currency import *

currencytest = Currency(5, "USD")
currencytest1 = Currency(4.99, "EUR")
currencytest2 = Currency(4.99, "EUR")
currencytest3 = Currency(6.99, "EUR")

class TestCurrency(unittest.TestCase):

    def test_eq(self):
        self.assertTrue(currencytest1 == currencytest2)
        self.assertFalse(currencytest2 == currencytest3)

    def test_ne(self):
        self.assertTrue(currencytest != currencytest2)
        self.assertFalse(currencytest2 != currencytest3)

    def test_add(self):
        new_currency = currencytest1 + currencytest2
        self.assertEqual(new_currency.amount, 9.98)

    def test_sub(self):
        new_currency = currencytest3 - currencytest1
        self.assertEqual(new_currency.amount, 2.00)

    def test_mul(self):
        new_currency = currencytest3 * currencytest1
        self.assertEqual(new_currency.amount, 34.88)
        new_currency = currencytest3 * 3
        self.assertEqual(new_currency.amount, 20.97)


if __name__ == '__main__':
    unittest.main()
