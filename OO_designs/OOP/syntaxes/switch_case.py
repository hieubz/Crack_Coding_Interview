"""
Python does not have a switch case statement
=> we can use dictionary mapping
"""


def week(w):
    switcher = {
        0: 'Sunday',
        1: 'Monday'
    }

    return switcher.get(w, 'invalid day of week')


class Switcher:
    def indirect(self, i):
        method_name = 'pizza_' + str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    @staticmethod
    def pizza_0():
        return 'zero'

    @staticmethod
    def pizza_1():
        return 'one'


class Zero:

    def create(self):
        print("zero")
        return self


class One:

    def create(self):
        print("one")
        return self


def indirect(i):
    switcher = {
        0: Zero,
        1: One,
    }
    func = switcher.get(i, lambda: 'invalid')
    return func()


if __name__ == '__main__':
    # print(week(1))
    # s = Switcher()
    # pizza = s.indirect(1)
    # print(pizza)

    print(indirect(1))
