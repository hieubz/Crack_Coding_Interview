"""
if there is no factory pattern
"""


class Pizza:
    def __init__(self):
        pass

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class CheesePizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class PizzaFactory:
    def __init__(self):
        self.pizza = None

    def create_pizza(self, p_type):
        if p_type == 'cheese':
            self.pizza = CheesePizza()
        elif p_type == 'clam':
            self.pizza = ClamPizza()

        return self.pizza


class PizzaStore:

    def __init__(self, factory):
        self.factory = factory

    # no factory
    def order_pizza(self, p_type):
        pizza = None
        if p_type == 'cheese':
            pizza = CheesePizza()
        elif p_type == 'clam':
            pizza = ClamPizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def order_pizza_2(self, p_type):
        pizza = self.factory.create_pizza(p_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def show_pizzas(self):
        pass
