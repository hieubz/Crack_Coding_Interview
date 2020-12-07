# a class should have only one job. If a class has more than one responsibility
# it becomes coupled. A change to one responsibility results to modification of
# the other responsibility

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass

    def save(self, animal):
        pass


# if the app changes in a way that it affects database management functions,
# the classes that make use of Animal properties will have to be touched and recompiled
# to compensate for the new changes

# it's like a domino effect, touch one card if effects all other cards in line
# violate >< conform

# we create another class that will handle the sole responsibility of storing
# an animal to a database


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id):
        pass

    def save(self, animal):
        pass


"""
when designing our classes, we should aim to put related features together,
so whenever they tend to change, they change for the same reason. And we should
try to separate features if they will change for different reasons
"""


# Facade pattern

class Animal:
    def __init__(self, name):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)

    def save(self):
        self.db.save(self)
