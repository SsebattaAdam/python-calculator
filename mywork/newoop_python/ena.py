
# THE TRY, EXCEPT AND FINALLY BLOCKS IN PYTHON
"""

try: The try block is used to enclose the code that might raise an exception. 
It allows you to test a block of code for exceptions.

except: The except block is used to handle specific exceptions that
 may occur within the try block. It allows you to define the actions to be 
 taken when a particular exception is raised.

finally: The finally block is used to define a piece of code that will be 
executed regardless of whether an exception occurred or not. It allows you 
to specify cleanup or resource release operations that should always be performed.
"""


def main():
    try:
        x = int(input())
        y = int(input())
        z = int(input())
        print(x + y + z)
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except Exception as e:
        print(e)
    finally:
        print("Finally")

        # EXMAPLES


def validate_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            raise ValueError("You must be at least 18 years old.")
        else:
            print("Age validation successful.")
    except ValueError as e:
        print("Invalid age:", str(e))


# calling the method defined above
validate_age("25")  # Age validation successful.
validate_age("-5")  # Invalid age: Age cannot be negative.
validate_age("15")  # Invalid age: You must be at least 18 years old.


def login(username, password):
    try:
        # Simulating authentication logic
        if username == "admin" and password == "password":
            print("Login successful.")
        else:
            raise ValueError("Invalid username or password.")
    except ValueError as e:
        print("Login failed:", str(e))


# calling the method defined above
login("admin", "password")    # Login successful.
login("guest", "123456")      # Login failed: Invalid username or password.
login("admin", "wrongpass")   # Login failed: Invalid username or password.


# User-defined exceptions are created to force certain constraints on the values of the variables.
# To create a User-defined Exception, we have to create a class that implements the Exception class.


# Base class
class PercentageError(Exception):
    pass

# Exception class for percentage > 100


class InvalidPercentageError(PercentageError):
    def __init__(self):
        super().__init__("Percentage is invalid")

# Exception class for percentage < 80


class LessPercentageError(PercentageError):
    def __init__(self):
        super().__init__("The Percentage is lesser than the Cut-off, Please try again!")

# class to check percentage range


class checkPercentage(PercentageError):
    def __init__(self, per):
        if per < 80:
            raise LessPercentageError
        if per > 100:
            raise InvalidPercentageError
        print("Congrats you're Enrolled")


# different cases and output for the defined method
try:
    print("For Percenatge: 93")
    checkPercentage(93)
except Exception as e:
    print(e)

try:
    print("\nFor Percenatge: 102")
    checkPercentage(102)
except Exception as e:
    print(e)

try:
    print("\nFor Percenatge: 58")
    checkPercentage(58)
except Exception as e:
    print(e)


