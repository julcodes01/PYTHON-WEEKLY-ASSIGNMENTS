# Shape Area Calculator
# This program demonstrates abstraction and polymorphism.

from abc import ABC, abstractmethod
import math


# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Main section
circle = Circle(7)
rectangle = Rectangle(10, 5)

# Display areas
print("--- Shape Areas ---")
print(f"Circle Area: {circle.area():.2f}")
print(f"Rectangle Area: {rectangle.area():.2f}")
