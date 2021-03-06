"""
high level modules should not depend upon low level modules. Both should depend upon abstractions

"""


class IFood:
    def bake(self):
        raise NotImplementedError

    def eat(self):
        raise NotImplementedError


class Bread(IFood):
    def bake(self):
        print("baked")

    def eat(self):
        print("eaten")


class Pastry(IFood):
    def bake(self):
        print("baked")

    def eat(self):
        print("eaten")


class Production:
    """
    food now is any concrete implementation of IFood
    this is also dependency injection when it is a parameter not hardcoded
    """
    def __init__(self, food):
        self.food = food

    def produce(self):
        self.food.bake()

    def comsume(self):
        self.food.eat()
