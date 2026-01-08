# import math
# import turtle
#
#
# class Circle:
#     """This class allow to create an objects with two parameters radius and diameter"""
#
#     def __init__(self, radius=None, diameter=None):
#         self.radius, self.diameter = self.radius_diameter(radius, diameter)
#
#     @staticmethod
#     def radius_diameter(radius, diameter):
#         return (radius, radius * 2) if radius else (diameter / 2, diameter)
#
#     def __repr__(self):
#         return f"{self.__dict__}"
#
#     def __add__(self, other):
#         if isinstance(other, Circle):
#             return Circle(self.radius + other.radius)
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def circle_area(self):
#         return math.pi * self.radius ** 2
#
#     def sort_list(self, *args):
#         out_list = [self]
#         for circles in args:
#             out_list.append(circles)
#         return sorted(out_list)
#
#
# c1 = Circle(radius=5)
# c2 = Circle(diameter=20)
# # print(c1.diameter)
# # print(c2.radius)
# # print(c1.circle_area())
# # print(c1)
# # print(c1 + c2)
# # print(c1 == c2)
# # print(c1.sort_list(c2))
# for each_circle in c1.sort_list(c2):
#     turtle.circle(each_circle.diameter)

import math
import turtle


class Circle:
    """This class allow to create an objects with two parameters radius and diameter"""

    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    @classmethod
    def radius_initialization(cls):
        radius = input("Please input a radius or leave blank: ").strip()
        diameter = input("Please input diameter or leave blank: ").strip()
        if radius and diameter:
            print("You should input only one parameter!")
        elif radius:
            if radius.isnumeric():
                return cls(float(radius))
            else:
                print("You should input only number!")
        elif diameter:
            if diameter.isnumeric():
                return cls(float(diameter) / 2)
            else:
                print("You should input only number!")
        else:
            print("You should input one of the parameters radius or diameter!")

    @property
    def circle_are(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"{self.__dict__}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


def sort_list(*args):
    return sorted(args) if args else f"There is no elements"


def print_circles(*args):
    for each_circle in sort_list(*args):
        turtle.circle(each_circle.radius)


c1 = Circle.radius_initialization()
print(c1)
# print(c1.circle_are)
# c4 = Circle(50)
# c2 = Circle(20)
# c3 = Circle(30)
# # print(sort_list(c4, c2, c3))
# print(print_circles(c4, c2, c3))
# # print(c1 + c2)
# print(c1 == c2)

# print_circles(c4, c2, c3)



