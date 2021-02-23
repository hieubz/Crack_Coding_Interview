class Contact:
    # class variable / class attribute
    all_contacts = []

    def __init__(self, name, email):
        # when initiate the instance of class
        # => assign value of input params to instance variables
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(f"we would send {order} order to {self.name}")


class Friend(Contact):
    # we create a newly method to override __init__
    # => it is automatically called instead of the super class's method
    # def __init__(self, name, email, phone):
    #     self.name = name
    #     self.email = email
    #     self.phone = phone
    #     # => this code has duplicate code with super class
    #     # => complicated

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    # any method can be overridden
