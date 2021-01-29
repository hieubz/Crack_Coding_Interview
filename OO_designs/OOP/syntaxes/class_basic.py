class Dog:
    # class attribute
    # belongs to a class rather than an particular object
    # it is shared between all the objects of this class
    species = "Hsi"

    # init is a constructor method, auto run when an instance of class is created
    # self: represents the instance of the class
    # we can access the attributes and methods of the class by self keyword.

    def __init__(self, name, age):
        # create an instance attribute called name and assigns to it the value
        # of the name parameters.
        # instance attribute: belong to one and only one object
        # this variable is only accessible in the scope of this object
        # and it is defined inside the constructor function
        self.name = name
        self.age = age


if __name__ == "__main__":
    d = Dog(2, 3)
    print(d)

# <__main__.Dog object at 0x000001F00FF58400>
# __main__ : means the running file.
