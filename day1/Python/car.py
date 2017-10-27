class Car():

    def __init__(self, name):
        self._name = name

    def hello(self):
        print("Hello %s" % self._name)

if __name__ == '__main__':
    car = Car('hiroshi')
    car.hello()