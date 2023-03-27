class Shopping:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price


class SqlDatabase:

    @staticmethod
    def save(shopping: Shopping):
        print('save shopping')
        pass


class CreditCard:

    @staticmethod
    def pay(shopping: Shopping):
        print('pay with credit card')
        pass


class ShoppingBasket:

    @staticmethod
    def buy(shopping: Shopping):
        db = SqlDatabase()
        db.save(shopping)
        credit_card = CreditCard()
        credit_card.pay(shopping)


def main():
    shopping = Shopping('huevos', 300)
    shop = ShoppingBasket()
    shop.buy(shopping)


main()
