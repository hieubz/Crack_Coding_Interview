"""
abstract class is a special class that can not initiated, works as base classes
the purpose of abstract classes are providing base functions, guides for concrete classes
INTERFACE: create interface when we provide additional behaviors and they are optional for those classes

"""

from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, num_months):
        self.name = name
        self.num_months = num_months

    def display_user(self):
        print(self.name)

    @abstractmethod
    def process_fee(self):
        pass


class GoldUser(User):
    GOLD_PACKAGE = 1000

    def process_fee(self):
        return self.num_months * GoldUser.GOLD_PACKAGE


class PlatinumUser(User):
    PLATINUM_PACKAGE = 2000

    def process_fee(self):
        return self.num_months * PlatinumUser.PLATINUM_PACKAGE
