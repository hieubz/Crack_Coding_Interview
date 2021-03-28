import threading


class Singleton:
    __instance = None
    __lock = threading.Lock()

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

        return Singleton.__instance

    @classmethod
    def get_instance_thread_safe(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()

        return cls.__instance


s = Singleton()
print(s.get_instance())
print(s.get_instance_thread_safe())
