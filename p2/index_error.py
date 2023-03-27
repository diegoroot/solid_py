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
    
    def get_total(drinks):
        total = 0
        for drink in drinks:
            if drink.type == 'Gaseosa':
                total += drink.price * 0.1
            elif drink.type == 'Licor':
                total += drink.price * 0.2
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
    }
]
drinks_objs = []
for drink in drinks:
    drinks_objs.append(Drink(**drink))

print(Drink.get_total(drinks_objs))