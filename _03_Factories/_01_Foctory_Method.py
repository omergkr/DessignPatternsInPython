"""

Object creation logic becomes too convoluted
Initializer is not descriptive
    - Name is always __init__
    - Cannot overload with same sets of arguments with different names
    - Can turn into "optional parameter hell"
Wholesale object creation (non-piecewise, unlike Builder ) can be outsourced to
    - A separate method (Factory Method)
    - That may exist in a separate class (Factory)
    - Can create hierarchy of factories with Abstract Factory

FACTORY -> A component responsible solely for the wholesale (not piecewise) creation of objects

A factory methods is a static method that creates objects
A factory is any entity that can take care of object creation
A factory can be external or reside inside the object as an inner class
Hierarchies of factories can be used to create related objects


"""
from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # redeclaration won't work
    # if you would just stay with Cartesian coordinates, everything would be fine
    # ,but you want to initialize it from polar coordinates
    # def __init__(self, rho, theta):

    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)

    # Factory methods
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

    # inner factory class
    class Factory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)

    factory = Factory()


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


# p1 = Point(2, 3, CoordinateSystem.CARTESIAN)
# print(p1)
p2 = PointFactory.new_cartesian_point(1, 2)
# or you can expose factory through the type
p3 = Point.Factory.new_cartesian_point(5, 6)
p4 = Point.factory.new_cartesian_point(7, 8)
print(p2, p3, p4)
