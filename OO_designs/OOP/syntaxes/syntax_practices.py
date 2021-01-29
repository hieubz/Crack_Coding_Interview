class Sample:
    """name mangling will change the names of the variables
    with a double underscore
    => change to the form _ClassName_variableName

    1. an underscore: internal use only but note specify truly private
    so this one can be call directly from other modules if it is specified in __all__
    2. two underscore: private and only be accessed by its own class

    """

    def __init__(self):
        self.np = "non private"
        self._wp = "weak private"
        self.__p = "private"  # name mangling

    def public_method(self):
        print(self.__private_method())

    def __private_method(self):
        print("weak private method")
        return "global"


s = Sample()
print(s.np)
print(s._wp)
print(s._Sample__p)

s.public_method()
s._Sample__private_method()
