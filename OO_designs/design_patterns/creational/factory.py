class Pizza:

    def prepare(self):
        pass

    def bake(self):
        pass

    def package(self):
        pass


class A(Pizza):
    def __init__(self):
        self.p_type = "A"

    def prepare(self):
        print(f"preparing {self.p_type}")

    def bake(self):
        print(f"baking {self.p_type}")

    def package(self):
        print(f"packaging {self.p_type}")


class B(Pizza):
    def __init__(self):
        self.p_type = "B"

    def prepare(self):
        print(f"preparing {self.p_type}")

    def bake(self):
        print(f"baking {self.p_type}")

    def package(self):
        print(f"packaging {self.p_type}")


class SimplePizzaFactory:

    @staticmethod
    def create_pizza(p_type):
        if p_type == "A":
            print("creating A pizza")
            return A()
        elif p_type == "B":
            print("creating B pizza")
            return B()


class PizzaStore:
    """
    pizza store get input as factory instance
    factory instance would hide instantiation code from PizzaStore
    there are many clients like PizzaStore who use Factory to create pizzas (PizzaShopMenu need to create them for
     their description and price)
    => when there is any change, we do not have to change PizzaStore or anywhere call to create Pizza but only Factory
    => encapsulation, no duplication, easy to maintain
    """

    def __init__(self, factory):
        self.factory = factory

    def order_pizza(self, p_type):
        pizza = self.factory.create_pizza(p_type)

        pizza.prepare()
        pizza.bake()
        pizza.package()

        return pizza


if __name__ == '__main__':
    pizza_factory = SimplePizzaFactory()
    store = PizzaStore(pizza_factory)
    pizza = store.order_pizza("A")
    print(type(pizza))
