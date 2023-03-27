from abc import abstractmethod


class Drink:
    def __init__(self, name, type, price):
        self.__name = name
        self.__type = type
        self.__price = price
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, new_type):
        self.__type = new_type
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price
    
    @abstractmethod
    def get_total(self):
        pass


class IDrinkWater(Drink):

    def get_total(self):
        return self.price * 0.3

class IDrinkLicor(Drink):

    def get_total(self):
        return self.price * 0.2

class IDrinkGaseosa(Drink):

    def get_total(self):
        return self.price * 0.1

class TotalInvoice(object):

    def __init__(self, invoices):
        assert isinstance(invoices, list), "`shapes` should be of type `list`."
        self.invoices = invoices
    

    @property
    def get_total(self):
        total = 0
        for drink in self.invoices:
            total += drink.get_total()
        return total
    

drinks = [
    {
        'name': 'Coca-cola',
        'type': 'Gaseosa',
        'price': 5000
    },
    {
        'name': 'Cerveza Poker',
        'type': 'Licor',
        'price': 20000
    },
    {
        'name': 'Pepsi',
        'type': 'Gaseosa',
        'price': 4000
    },
    {
        'name': 'Aqua',
        'type': 'Ag',
        'price': 4000
    }
]

drinks_objs = []
for drink in drinks:
    if drink.get('type') == 'Agua':
        drinks_objs.append(IDrinkWater(**drink))
    elif drink.get('type') == 'Licor':
        drinks_objs.append(IDrinkLicor(**drink))
    elif drink.get('type') == 'Gaseosa':
        drinks_objs.append(IDrinkGaseosa(**drink))

total = TotalInvoice(drinks_objs)
print(total.get_total)