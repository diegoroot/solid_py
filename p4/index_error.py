class Vehicle:

    def go(self):
        pass
    
    def fly(self):
        raise NotImplementedError


class Aircraft(Vehicle):

    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):

    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')