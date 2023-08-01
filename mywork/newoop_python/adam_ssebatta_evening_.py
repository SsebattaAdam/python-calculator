

# Defining a function which returns reciprocal of a number
def reciprocal(num1):
    try:
        reci = 1 / num1
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print(reci)


# Calling the function and passing values
reciprocal(4)
reciprocal(0)


# the Finally Keyword in Python

try:
    div = 4 // 0
    print(div)
# this block will handle the exception raised
except ZeroDivisionError:
    print("Atepting to divide by zero")
# this will always be executed no matter exception is raised or not
finally:
    print('This is code of finally clause')

# the above are Built-in Exceptions
# Built-in Exceptions - Python Documentation

# User-Defined Exceptions

#  they are used and create represent specific error
# conditions or exceptional situations in your code
# In Python, it is common to inherit from the built-in
#  Exception class when creating custom exceptions.
#  However, it is also possible to inherit from other exception classes,
# such as RuntimeError, depending on your specific use case.


class LoginError(Exception):
    pass


def login(username, password):
    if username != "oscar" or password != "mine":
        raise LoginError("Invalid username or password")
    else:
        print("Login successful")


try:
    login("guest", "12345")
except LoginError as e:
    print("LoginError caught:", str(e))

try:
    login("oscar", "mine")
except LoginError as e:
    print("LoginError caught:", str(e))
else:
    print("No exception occurred.")


# another example

class AgeError(Exception):
    pass


def process_age(age):
    if age < 0:
        raise AgeError("Invalid age: age cannot be negative.")
    elif age < 18:
        raise AgeError("Invalid age: person must be at least 18 years old.")
    else:
        print("Age is valid.")


try:
    process_age(-5)
except AgeError as e:
    print("AgeError caught:", str(e))

try:
    process_age(16)
except AgeError as e:
    print("AgeError caught:", str(e))
else:
    print("No exception occurred.")


# Another one
class CustomException(Exception):
    pass


class ValueTooLargeError(CustomException):
    pass


class ValueTooSmallError(CustomException):
    pass


def check_value(value):
    if value > 100:
        raise ValueTooLargeError("Value is too large.")
    elif value < 0:
        raise ValueTooSmallError("Value is too small.")
    else:
        print("Value is within the acceptable range.")


try:
    check_value(150)
except CustomException as e:
    print("Custom Exception caught:", str(e))

try:
    check_value(-10)
except CustomException as e:
    print("Custom Exception caught:", str(e))

try:
    check_value(50)
except CustomException as e:
    print("Custom Exception caught:", str(e))
else:
    print("No exception occurred.")


# another example
# Python also lets us design our customized exceptions.


class EmptyStringError(Exception):
    pass


class InvalidInputError(Exception):
    pass


def process_input(data):
    if not data:
        raise EmptyStringError("Input string is empty.")
    elif not data.isnumeric():
        raise InvalidInputError("Input is not a valid number.")
    else:
        num = int(data)
        print("Processed input:", num)


try:
    process_input("")
except EmptyStringError as e:
    print("EmptyStringError caught:", str(e))

try:
    process_input("Hello")
except InvalidInputError as e:
    print("InvalidInputError caught:", str(e))

try:
    process_input("42")
except (EmptyStringError, InvalidInputError) as e:
    print("Custom exception caught:", str(e))
else:
    print("No exception occurred.")


file_path = "example.txt"

# Open the file in read mode
file_object = open(file_path, "r")

# Read the entire content of the file
content = file_object.read()

# Print a message along with the file's content
print("File content:")
print(content)

# Close the file
file_object.close()


# Writing to a File:
file_path = "example.txt"

# Open the file in write mode
file_object = open(file_path, "w")

# Write data to the file
file_object.write("Hello, world!")

# Close the file
file_object.close()

# Open the file in read mode
file_object = open(file_path, "r")

# Read and print the file's content
file_content = file_object.read()
print(file_content)

# Close the file
file_object.close()


# appending to a file
file_path = "example.txt"

# Open the file in append mode
file_object = open(file_path, "a")

# Append data to the file
file_object.write("\nThis is an appended line.")

# Close the file
file_object.close()

# Print a message
print("Data appended to the file:", file_path)


# Exception Handling with Files

file_path = "nonexistent_file.txt"
file_object = None

try:
    # Open the file
    file_object = open(file_path, "r")

    # Read the content
    content = file_object.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the file (executes regardless of exceptions)
    if file_object is not None:
        file_object.close()
