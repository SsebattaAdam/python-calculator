import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and display area and perimeter of Circle
circle_area = circle.area()
circle_perimeter = circle.perimeter()
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)

# Calculate and display area and perimeter of Rectangle
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)
