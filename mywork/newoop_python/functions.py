
# group of peice of code
# def function_name():
#     print("Hello World")


# Defining a function, we start with a def keyword
# followed by the function name

"eg"


def afterNoon():
    print("t always starts at 2pm")

# calling a function by writing the function name

afterNoon()

#arguments and parameters

# parameters are the placeholder
# s or variables defined in a 
# function's definition, while 
# arguments are the actual values
#  or expressions passed into the
#  function during its invocation.
#  Parameters define the input
#  requirements, while arguments 
# provide the specific values for
#  those requirements.


#ge of parameters

def greeting(name):
    print("Hello " + name)

greeting("John")

def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")


#eg of arguments

def greet(name, age):
    print("Hello, " + name + "!")
    print("You are " + str(age) + " years old.")

greet("John", 35)

def add_numbers(a, b):
    sum = a + b
    print("The sum is:", sum)

add_numbers(5, 7)
add_numbers(10, 3)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")





