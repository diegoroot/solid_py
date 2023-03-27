class Vehicle:

    def go(self):
        raise NotImplementedError

class Flyable(Vehicle):

    def fly(self):
        pass


class Aircraft(Flyable):

    def go(self):
        print("going")

    def fly(self):
        print("Flying")

class Car(Vehicle):

    def go(self):
        print("Going")


#helicóptero ?? go???
class Vehicle:

    def go(self):
        raise NotImplementedError

class Flyable():

    def fly(self):
        raise NotImplementedError


class Aircraft(Vehicle, Flyable):

    def go(self):
        print("Going")

    def fly(self):
        print("Flying")

class Car(Vehicle):

    def go(self):
        print("Going")

class Aircraft(Flyable):

    def fly(self):
        print("Flying")