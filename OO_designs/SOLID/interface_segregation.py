"""
deal with disadvantages of implementing big interface
and when we add another method to the IShape interface, like draw_triangle()
"""


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


"""
if you use this interface, subclasses must define all methods 
"""


class Square(IShape):
    def draw_square(self):
        return "square"

    def draw_rectangle(self):
        return "rectangle"


class Circle(IShape):
    def draw_circle(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_square(self):
        pass


"""
if we add another method to the IShape interface => the classes must implement the new method or error will
be thrown
Solution:
"""


class Shape:
    def draw(self):
        raise NotImplemented


class Circle1(Shape):
    def draw(self):
        print("draw circle")


class Square1(Shape):
    def draw(self):
        print("draw square")
