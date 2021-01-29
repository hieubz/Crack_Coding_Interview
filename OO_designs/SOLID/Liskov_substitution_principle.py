"""
a sub-class must be substitutable for its super-class
the aim of this principle to ensure that a sub-class can assume the place of its
super class without errors.
"""


def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())


"""
the animal_leg_count function cares less the type of Animal passed, it
just calls the leg_count method. All it knows is that the parameter must be of an Animal type, either the Animal 
class or its sub-class

The Animal class now have to implement/define a leg_count method. And its sub-classes have to implement
the leg_count method
"""


class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass


"""
when it's passed to the animal_leg_count function, it returns the number of legs a lion has
you see, just call the leg_count method because a sub-class of Animal ...
"""