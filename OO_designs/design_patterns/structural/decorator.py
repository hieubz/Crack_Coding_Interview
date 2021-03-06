"""
a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special
wrapper objects that contain the behaviors
In some cases, we should not use inheritance because it causes class explosion
Decorator provide a flexible alternative to subclassing for extending functionality
"""


class AbstractCoffee:

    def cost(self):
        pass

    def get_ingredients(self):
        pass


class ConcreteCoffee(AbstractCoffee):
    def __init__(self):
        self.description = "coffee"

    def cost(self):
        return 1.00

    def get_ingredients(self):
        return self.description


class AbstractCoffeeDecorator(AbstractCoffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def cost(self):
        return self.decorated_coffee.cost() + 0.0

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ""


class Sugar(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def cost(self):
        return self.decorated_coffee.cost() + 0.1

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'


class Milk(AbstractCoffeeDecorator):
    def __init__(self, decorated_coffee):
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def cost(self):
        return self.decorated_coffee.cost() + 0.15

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'


if __name__ == '__main__':
    my_coffee = ConcreteCoffee()
    print('Ingredients: {}; Cost: {}'.format(my_coffee.get_ingredients(), my_coffee.cost()))

    my_coffee = Sugar(my_coffee)
    print('Ingredients: {}; Cost: {}'.format(my_coffee.get_ingredients(), my_coffee.cost()))

    my_coffee = Milk(my_coffee)
    print('Ingredients: {}; Cost: {}'.format(my_coffee.get_ingredients(), my_coffee.cost()))





















