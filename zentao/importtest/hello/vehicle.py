class Vichle:
    def __init__(self, name, ):
        self.name = name

    def say(self):
        print("hello, I'm {}".format(self.name))


if __name__ == '__main__':
    vi = Vichle("snake")
    vi.say()
