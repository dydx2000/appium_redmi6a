import importtest.hello.vehicle as vehicle
from importtest.world.Car import *


class Taxi:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name)


if __name__ == '__main__':
    taxi = Taxi('BYD')
    taxi.say()

    vi = vehicle.Vichle("volvo")
    vi.say()

    mini = Car("mini cooper")
    mini.say()
