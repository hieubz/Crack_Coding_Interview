"""
Open-closed Principle

classes, modules, functions should be open for extension, not modification

But following OCP usually introduces new levels of abstraction, which adds complexity to our code
=> concentrate on those areas that are most likely to change in your designs and apply it there.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


animals = [Animal('lion'), Animal('mouse')]


def animal_sound(animals):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('fuck')


"""
the function animal_sound does not conform to the open-closed principle because
it cannot be closed against new kinds of animals.
If we add a new animal, we have to modify this function. You see, for every new animal,
a new logic is added to the function. 
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def make_sound(self):
        pass


# and then every animal adds its own implementation on how it makes a sound in the
# make_sound

class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'fuck'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


"""
we have each animal extend the Animal class and implement the virtual make_sound method
Now if we add a new animal, animal_sound does not need to change anymore
"""

"""
Another example: give a discount of 20% to your favorite customers
40% discount to VIP customers
"""

# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price
#
#     def give_discount(self):
#         if self.customer == 'fav':
#             return self.price * 0.2
#         if self.customer == 'vip':
#             return self.price * 0.4


"""
this fails the OCP principle. Because OCP forbids it
If we want to give a new percent discount maybe to a different type of customer,
you will see that a new logic will be added
=> to make it follow the OCP, we will add a new class that will extend the Discount
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 1.2


class SuperVIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 1.5


class DiamondDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
