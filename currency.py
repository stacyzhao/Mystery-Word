# Currency objects
# Must be created with an amount and a currency code.
# Must equal another Currency object with the same amount and currency code.
# Must NOT equal another Currency object with different amount or currency code.
# Must be able to be added to another Currency object with the same currency code.
# Must be able to be subtracted by another Currency object with the same currency code.
# Must raise a DifferentCurrencyCodeError when you try to add or subtract two Currency objects with different currency codes.
# Must be able to be multiplied by an int or float and return a Currency object.
# Currency() must be able to take one argument with a currency symbol embedded in it, like "$1.20" or ""€" 7.00", and figure out the correct currency code. It can also take two arguments, one being the amount and the other being the currency code.
class DifferentCurrencyCodeError(Exception):
    pass

class Currency:
    currencies = {"USD": "$", "EUR": "€", "INR": "₹", "CNY": "¥"}

    def __init__(self, amount, currency_code=""):
        if isinstance(amount, str):
            self.amount = float(amount[1:].strip())
            self.currency_code = self.convert_currency_symbol(amount[0])
        else:
            self.amount = amount
            self.currency_code = currency_code

    def __eq__(self, other):
        return self.currency_code == other.currency_code and self.amount == other.amount

    def __ne__(self, other):
        return self.currency_code != other.currency_code and self.amount != other.amount

    def __add__(self, other):
        if self.same_currency(other.currency_code):
            return Currency(round(self.amount + other.amount, 2),self.currency_code)

    def __sub__(self, other):
        if self.same_currency(other.currency_code):
            return Currency(round(self.amount - other.amount, 2),self.currency_code)

    def same_currency(self, currency_code):
        if self.currency_code == currency_code:
            return True
        else:
            raise DifferentCurrencyCodeError("Different Currency Code.")

    def is_float(self, other):
        try:
            isinstance(other.amount, float)
        except:
            return float(other.amount)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            amount = round(self.amount * other,2)
        else:
            amount = round(self.amount * other.amount,2)
        return Currency(amount, self.currency_code)

    def convert_currency_symbol(self, currency_symbol):
        for key in Currency.currencies:
            value = Currency.currencies[key]
            if currency_symbol == value:
                return key

#
# currencytest = Currency(5, "USD")
# currencytest1 = Currency(4.9999999, "EUR")
# currencytest2 = Currency(4.99, "EUR")
# currencytest3 = Currency("$2.999999")
# print("eq: ", currencytest1 == currencytest2)
# print("add: ", currencytest1 + currencytest2)
# print("sub: ", currencytest1 - currencytest2)
# print("mul: ",currencytest * currencytest1)
# print("check_currency: ", currencytest3.amount, currencytest3.currency_code)
# print((currencytest * 5).amount)
