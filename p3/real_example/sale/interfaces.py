from .models import Sale

class SaleInterface(Sale):

    def generate():
        print('Se genera la venta')

    def calcule_taxes():
        print('Se calculan los impuestos')


# qué pasa si la venta es internacional y no tiene impuestos ????


class SaleWithoutTaxesInterface(Sale):

    def __init__(self, client, price):
        self.__client = client
        self.__price = price
        self.__taxes = 0

    def generate():
        print('Se genera la venta')

    def calcule_taxes():
        print('No se calculan los impuestos es internacional')