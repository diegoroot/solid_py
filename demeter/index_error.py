class Motor:
    
    def start():
        print('start motor')
        pass


class Vehicle:

    motor = Motor


class Person:
    vehicle = Vehicle


def main():
    diego = Person()
    diego.vehicle.motor.start()


main()