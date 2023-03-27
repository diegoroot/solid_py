class Motor:

    def start(self):
        print('start motor')
        pass


class Vehicle:

    motor = Motor()

    def start(self):
        self.motor.start()


class Person:
    vehicle = Vehicle()

    def start(self):
        self.vehicle.start()


def main():
    diego = Person()
    diego.start()


main()



