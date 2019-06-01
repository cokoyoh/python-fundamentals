import math
from abc import ABC, abstractmethod


class AbstractClassShapes(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(AbstractClassShapes):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(AbstractClassShapes):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * math.pow(self.__radius, 2)

    def circumference(self):
        return 2 * math.pi * self.__radius


rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())

circle = Circle(7)
print(circle.area())
print(circle.circumference())
