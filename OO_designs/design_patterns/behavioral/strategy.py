from abc import ABC, abstractmethod


# Interface for Behaviors

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("flying with the wings")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("cannot fly")


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("quack quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("cannot quack")


# Context


class Duck:

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    def perform_quack(self):
        self._quack_behavior.quack()

    def perform_fly(self):
        self._fly_behavior.fly()

    def set_fly(self, fly_behavior: FlyBehavior):
        """
        allows replacing a Strategy object at runtime.
        :param fly_behavior:
        :return:
        """
        self._fly_behavior = fly_behavior

    def set_quack(self, quack_type: QuackBehavior):
        self._quack_behavior = quack_type


class RubberDuck(Duck):

    def __init__(self):
        mute_quack = MuteQuack()
        fly_noways = FlyNoWay()
        super(RubberDuck, self).__init__(fly_noways, mute_quack)

    def display(self):
        print("- Rubber Duck")
        self.perform_quack()
        self.perform_fly()


class BauDuck(Duck):

    def __init__(self):
        quack = Quack()
        fly_wings = FlyWithWings()
        super(BauDuck, self).__init__(fly_wings, quack)

    def display(self):
        print("- Bau Duck")
        self.perform_quack()
        self.perform_fly()


if __name__ == '__main__':
    rubber_duck = RubberDuck()
    bau_duck = BauDuck()
    rubber_duck.display()
    bau_duck.display()
