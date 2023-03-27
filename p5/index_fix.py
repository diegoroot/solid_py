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


class Persistence:

    @staticmethod
    def save(shopping: Shopping):
        print('save')
        pass


class SqlDatabase(Persistence):

    @staticmethod
    def save(shopping: Shopping):
        print('save basket on sql')
        pass


class PaymentMethod:

    @staticmethod
    def pay(shopping: Shopping):
        print('pay shopping')
        pass


class CreditCard(PaymentMethod):

    @staticmethod
    def pay(shopping: Shopping):
        print('pay with credit card')
        pass


class ShoppingBasket:
    persistence = None
    payment_method = None

    def __init__(self, persistence, payment_method):
        self.persistence = persistence
        self.payment_method = payment_method

    def buy(self, shopping: Shopping):
        self.persistence.save(shopping)
        self.payment_method.pay(shopping)


def main():
    shopping = Shopping('huevos', 300)
    shop = ShoppingBasket(Persistence, PaymentMethod)
    shop.buy(shopping)


main()


class Server(Persistence):

    @staticmethod
    def save(shopping: Shopping):
        print('Save on server')
        pass


class Paypal(PaymentMethod):

    @staticmethod
    def pay(shopping: Shopping):
        print('Pay with paypal')
        pass


def main():
    shopping = Shopping('huevos', 300)
    shop = ShoppingBasket(SqlDatabase, CreditCard)
    shop.buy(shopping)
    print()
    shopping = Shopping('Cerveza', 5000)
    shop = ShoppingBasket(Server, Paypal)
    shop.buy(shopping)


main()
