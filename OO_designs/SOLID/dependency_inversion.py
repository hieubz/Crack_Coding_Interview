"""
high level modules should not depend upon low level modules. Both should depend upon abstractions

"""


class IFood:
    def bake(self):
        raise NotImplemented

    def eat(self):
        raise NotImplemented


class Pizza(IFood):
    def bake(self):
        print("pizza was baked")

    def eat(self):
        print("pizza was ate")


class Bread(IFood):
    def bake(self):
        print("bread was baked")

    def eat(self):
        print("bread was ate")


class Production:
    def __init__(self, food: IFood):
        self.food = food

    def produce(self):
        self.food.bake()

    def consume(self):
        self.food.eat()


if __name__ == '__main__':
    pizza = Pizza()
    p = Production(pizza)
    p.produce()
    p.consume()
