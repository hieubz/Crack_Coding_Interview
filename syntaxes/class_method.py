"""
a class method is a method that is bound to a class rather than its object
it doesn't require creation of a class instance

1. static method knows nothing about the class and just deals with the parameters
 - static method do not use anything related to its class or instance but only deals with parameters
2. class method: class is passed to the function as the first parameter - cls
 - use when you need to have a method which returns an instance - factory method
 - flexible in creating instances in inheritance
"""
from datetime import date


class Person:
    age = 25

    # self points to an instance of the class
    # methods can easily access attributes and other methods of one object
    def method(self):
        return 'instance method', self

    @classmethod
    def print_age(cls):
        """
        is used in factory design where we wnat to call many functions
        with class name rather than object
        - gives us ability to define factory methods. We can produce instances
        by any ways we like
        :return:
        """
        print('The age is: ', cls.age)

    @staticmethod
    def show_notification(noti):
        print(noti)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def something(self):
        return

    @classmethod
    def init_from_string(cls, info):
        """
        create factory methods. Factory methods return class object (similar to a constructor)
        for different use cases

        => a class method to create a Student object by string info
        :param info:
        :return:
        """
        name, age = info.split(' _ ')
        return cls(name, age)

    @classmethod
    def init_from_json(cls, json_file):
        pass

    @staticmethod
    def fuck(name):
        """
        use to create utility functions
        :param name:
        :return:
        """
        return name


print(Student.fuck("hieu _ 20"))