import os
import sys
# sys.path.append(".."
import time

print(__file__)
current_dir = os.path.dirname(__file__)
print(current_dir)
parent_dir = os.path.join(current_dir,"../")
print(parent_dir)
sys.path.append(parent_dir)
# sys.path.append("../")


# sys.path.append(os.path.dirname(__file__))

import hello.vehicle as vehicle
from world.Car import *


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
