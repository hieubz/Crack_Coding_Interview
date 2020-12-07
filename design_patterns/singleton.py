

class Singleton:
    __instance = None

    # private constructor
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()

        return Singleton.__instance



s = Singleton()
print(s)

s = Singleton.get_instance()
print(s)
