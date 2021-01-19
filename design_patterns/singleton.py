class Singleton:
    __instance = None

    # private constructor
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This is a singleton class")
        else:
            Singleton.__instance = self

    # public method
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        else:
            return Singleton.__instance


s = Singleton()
print(s.get_instance())
