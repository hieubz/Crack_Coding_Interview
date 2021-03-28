"""
- Interface is used to specify behaviors that classes must implement
- in OOP, an interface is a set of publicly accessible methods on an object which can be used by other parts \
of the program to interact with that object

- Interface contains only abstract methods (but Python does not support creation of interface through any keyword
 => you will have to define an interface using abstract class itself)
- If you create an abstract class which contains only abstract methods that acts as an interface in Python


ABC: define base classes which are abstract in nature.

"""

from abc import ABC, abstractmethod


class Bird(ABC):
    """
    any class derives from our Bird class, it must implement the fly method too.
    """

    @abstractmethod
    def fly(self):
        pass


class FourWheelVehicle(ABC):

    @abstractmethod
    def speed_up(self):
        pass


class Car(FourWheelVehicle):
    def speed_up(self):
        print("Running!")

    def test(self):
        print("test")


if __name__ == '__main__':
    f = Car()
    f.test()
