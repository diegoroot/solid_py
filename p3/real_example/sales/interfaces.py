from .models import SaleAbstract

class SaleWithTaxesInterface(SaleAbstract):

    def generate():
        print('Se genera la venta')

    def calcule_taxes():
        print('Se calculan los impuestos')


class SaleWithoutTaxesInterface(SaleAbstract):

    def generate():
        print('Se genera la venta')