# class Button(object):
#     html = ""
#
#     def get_html(self):
#         return self.html
#
#
# class Image(Button):
#     html = "<img>"
#
#
# class Input(Button):
#     html = "input"
#
#
# class Flask(Button):
#     html = "flask"
#
#
# class ButtonFactory:
#     def create_button(self, typ):
#         target_class = typ.capitalize()
#         return globals()[target_class]()
#
#
# button_obj = ButtonFactory()
# button = ['image', 'input', 'flask']
# for b in button:
#     print(button_obj.create_button(b).get_html())


"""
without factory pattern
"""

# class GenericTires:
#     def tire_type(self):
#         return 'generic'
#
#
# class MountainTires:
#     def tire_type(self):
#         return 'mountain'
#
#
# class Bicycle:
#     def __init__(self):
#         self.tires = self.add_tires()
#
#     def add_tires(self):
#         return GenericTires()
#
#     def get_tire_type(self):
#         return self.tires.tire_type()
#
#
# # add new classes and override the method. You do not have to make adjustment
# # to the base class
# class MountainBike(Bicycle):
#     def add_tires(self):
#         return MountainTires()
#
#
# bike = MountainBike()
# print(bike.get_tire_type())

"""
with factory pattern
"""


class GenericTires:
    def part_type(self):
        return 'generic tire'


class GenericFrame:
    def part_type(self):
        return 'generic frame'


class MountainTires:
    def part_type(self):
        return 'mountain tire'


class MountainFrame:
    def part_type(self):
        return 'mountain frame'


# part factory is simply a separate class
class GenericBike:
    def add_tires(self):
        return GenericTires()

    def add_frame(self):
        return GenericFrame()


class MountainBike:
    def add_tires(self):
        return MountainTires()

    def add_frame(self):
        return MountainFrame()


class Bicycle:
    # no longer specify the type of parts to install in the parent class at all.
    # adding parts is handled by each respective add_tires() and add_frame() method inside the part factory

    # the parent Bicycle class calls the methods to add parts within the part factory class
    # each instance is still a Bicycle but built with different part
    def __init__(self, factory):
        self.tires = factory().add_tires()
        self.frame = factory().add_frame()

    def show_parts(self):
        return self.tires.part_type(), self.frame.part_type()


mountain_bike = Bicycle(MountainBike)
print(mountain_bike.show_parts())

road_bike = Bicycle(GenericBike)
print(road_bike.show_parts())
