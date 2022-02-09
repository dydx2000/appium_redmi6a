import sys
sys.path.append("..")
# import hello.vehicle

from hello.vehicle import Vichle




class Car:
    def __init__(self, name, ):
        self.name = name

    def say(self):
        print("hello, I'm {}".format(self.name))


if __name__ == '__main__':
    vi = Car("snake")
    vi.say()
    car = Vichle("k")
    car.say()
