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
