class car:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):  # Added self parameter
        print("Hello, my name is " + self.name)
        print("My age is " + str(self.age))  # Converted age to string


myCar = car("Adams", 12)
myCar.greeting()


class student:
    def __init__(self, name, yearOfStudy, courseName):
        self.name = name
        self.yearOfStudy = yearOfStudy
        self.courseName = courseName
        self.id = 23  # Add the missing ID attribute or initialize it with a specific value

    def displayDetails(self):
        print("ID: %d\nName: %s\nYear of Study: %d\nCourse Name: %s" %
              (self.id, self.name, self.yearOfStudy, self.courseName))


stu1 = student("Adam Oscar", 2, "BSSE")

stu1.displayDetails()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


mycircles = Circle(12)

mycircles.area()
mycircles.circumference()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height*self.width

    def perimeter(self):
        return 2*(self.height+self.width)


myrectangles = Rectangle(10, 20)

myrectangles.area()
myrectangles.perimeter()


class EmployeeBonus:
    def __init__(self, bonus, salary):
        self.bonus_percentage = bonus
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * self.bonus_percentage

    def print_bonus(self):
        # Convert bonus to string
        print("The actual bonus amount is: " +
              str(self.salary + (self.calculate_bonus())))


# Create an instance of EmployeeBonus
emp = EmployeeBonus(0.15, 5000)

# Call the print_bonus method to print the bonus amount
emp.print_bonus()


# encapsulation
# goals of encapsulation
"""
1. To hide the implementation details of a class
2. To protect the integrity of a class
3. To protect the integrity of an object
"""


class TemperatureConverter:
    def __init__(self):
        self.celsius = 0.0
        self.fahrenheit = 0.0

    def set_celsius(self, celsius):
        self.celsius = celsius

    def get_celsius(self):
        return self.celsius

    def convert_to_fahrenheit(self):
        self.fahrenheit = (self.celsius * 9/5) + 32

    def get_fahrenheit(self):
        return self.fahrenheit


# Create an instance of the TemperatureConverter class
converter = TemperatureConverter()

# Set the temperature in Celsius
celsius = float(input("Enter temperature in degrees Celsius: "))
converter.set_celsius(celsius)

# Convert Celsius to Fahrenheit
converter.convert_to_fahrenheit()

# Get the converted temperature in Fahrenheit
fahrenheit = converter.get_fahrenheit()

# Display the result
print("Temperature in degrees Fahrenheit: ", fahrenheit)


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def increment_pay(self, increment_amount):
        self.__salary += increment_amount


# Create an employee object
employee = Employee("John Doe", 850000)

# Display the initial salary
print("Initial Salary:", employee.get_salary())

# Increment the pay by 150000
employee.increment_pay(150000)

# Display the new salary
print("New Salary:", employee.get_salary())
