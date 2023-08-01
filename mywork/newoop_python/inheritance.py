class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")


class Dog(Animal):
    def back(self):
        print(self.name + " is barking")


class Cat(Animal):
    def bark(self):
        print(self.name + " is barking")


# creating objects

animal = Animal("Generic")
dog = Dog("Hey")
cat = Cat("Mem")

animal.eat()
dog.back()
cat.bark()


# example 2


class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        # super().__init__(brand, color)

    def drive(self):
        print(self.brand + " is driving")


class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand, color)
        self.wheels = 4

    def drive(self):
        super().drive()
        print(self.brand + " has " + str(self.wheels) + " wheels")
        print(self.brand + " is driving")


# exmple 3
# multiple inheritance

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " has " + str(self.age) + "years older")


class MessageOfAnimal:
    def message(self):
        print("Am from anothere class")


class Bird(Animal, MessageOfAnimal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        MessageOfAnimal.message(self)

    def display(self):
        print(self.name + " is a bird")

        print("hey there")


mybird = Bird("Oscar", "hey there")

mybird.eat()
mybird.display()


# methde overriding

class Animal:
    def makeSound(self):
        print("Animal sound")


class Cat(Animal):
    def makeSound(self):
        print("Cat sound")


def makeSoynder(animal):
    animal.makeSound()


animal = Animal()
cat = Cat()
cat.makeSound()

makeSoynder(animal)


# polymorphism
# methodoverloading

# example
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


obj = Circle(33)
print("Circle Area:", obj.calculate_area())

obj1 = Rectangle(23, 22)
print("Rectangle Area:", obj1.calculate_area())
print("Rectangle Perimeter:", obj1.calculate_perimeter())


# methood overriding

class MathOperations:
    def calculate(self, a, b=None):
        if b is None:

            result = a * 2
        else:

            result = a + b

        return result


math_ops = MathOperations()


result1 = math_ops.calculate(5)
print("Result with one parameter:", result1)


result2 = math_ops.calculate(2, 3)
print("Result with two parameters:", result2)


# abstraction

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


# Create instances of Rectangle and Circle
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Calculate and print the area and perimeter of the rectangle
print("Rectangle Area:", rectangle.calculate_area())
print("Rectangle Perimeter:", rectangle.calculate_perimeter())

# Calculate and print the area and circumference of the circle
print("Circle Area:", circle.calculate_area())
print("Circle Perimeter:", circle.calculate_perimeter())
