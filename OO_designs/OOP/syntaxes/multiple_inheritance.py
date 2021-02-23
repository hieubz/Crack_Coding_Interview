# class Contact:
#     # class variable / class attribute
#     all_contacts = []
#
#     def __init__(self, name, email):
#         # when initiate the instance of class
#         # => assign value of input params to instance variables
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)
#
#
# # Mixin
# class MailSender:
#     def send_email(self, message):
#         print(self.email)
#
#
# def send_email(message, param):
#     print(message, param)
#     # do smt
#
#
# """
# Mixin is complicate
# => we could have used single inheritance and added the send_email function to the subclass
# => we create a function only for sending an email
# """
#
#
# class EmailableContact(Contact, MailSender):
#     pass
#
#
# e = EmailableContact("Hieu", "hieupd@gmail.com")
# e.send_email("fucking awesome")
#
# """
# we can work with multiple inheritance in python but it gets very messy when we have to call methods on the superclass
# because there are multiple super classes
#
# """
#
#
# class AddressHolder:
#     def __init__(self, street, city, state, code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.code = code
#
#
# class Friend(Contact, AddressHolder):
#     def __init__(self, name, email, phone, street, city, state, code):
#         Contact.__init__(self, name, email)
#         AddressHolder.__init__(self, street, city, state, code)
#         self.phone = phone


"""
the above code can works but that's relatively harmless - 
imagine trying to connect to a database twice for every request! disaster!!!
=> we can use super()....
"""


# solution: using kwargs for sets of arguments


class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        print("contact")
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        print("address")
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone





f = Friend()
print(f)







