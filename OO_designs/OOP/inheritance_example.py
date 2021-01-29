class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        return f'{self.name} says {sound}'


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        """
        super is used to call the parent class's.speak() method
        with the same argument passed to sound
        :param sound:
        :return:
        """

        return super().speak(sound)
