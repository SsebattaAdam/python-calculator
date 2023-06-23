"""
Arithmetic Operators:

Addition: + (e.g., 2 + 3)
Subtraction: - (e.g., 5 - 2)
Multiplication: * (e.g., 4 * 3)
Division: / (e.g., 10 / 2)
Floor Division: // (e.g., 10 // 3 returns 3)
Modulus (Remainder): % (e.g., 10 % 3 returns 1)
Exponentiation: ** (e.g., 2 ** 3 returns 8)
"""




a = 5
b = 2
sum = a + b
print(sum)
product = a * b
print(product)

division = a / b

"""

Assignment Operators:

Assign: = (e.g., x = 5)
Add and Assign: += (e.g., x += 3 is equivalent to x = x + 3)
Subtract and Assign: -= (e.g., x -= 2 is equivalent to x = x - 2)
Multiply and Assign: *= (e.g., x *= 4 is equivalent to x = x * 4)
Divide and Assign: /= (e.g., x /= 2 is equivalent to x = x / 2)
"""

x = 5
print(x)
x += 3  # x is now 8
print(x)
x *= 2  # x is now 16
print(x)

"""
Comparison Operators:

Equal to: == (e.g., 3 == 3 returns True)
Not equal to: != (e.g., 4 != 3 returns True)
Greater than: > (e.g., 5 > 3 returns True)
Less than: < (e.g., 2 < 4 returns True)
Greater than or equal to: >= (e.g., 4 >= 4 returns True)
Less than or equal to: <= (e.g., 3 <= 3 returns True)
"""
a = 5
b = 3
is_equal = a == b
is_greater = a > b
print(is_equal) # false
print(is_greater) #true
"""

Bitwise AND (&):
The bitwise AND operator performs a
 bitwise AND operation on the binary representations 
 of two numbers. It compares the corresponding bits of the operands 
 and produces a result 
where each bit is set to 1 only if both corresponding bits are 1.
"""

a = 12    # binary: 1100
b = 10    # binary: 1010

result = a & b
print(result)   # Output: 8 (binary: 1000)

"""
Bitwise OR (|):
The bitwise OR operator performs a bitwise OR
operation on the binary representations of two numbers. 
It compares the corresponding bits of the operands and
produces a result where 
each bit is set to 1 if at least one of the corresponding bits is 1.
"""

a = 12    # binary: 1100
b = 10    # binary: 1010

result = a | b
print(result)   # Output: 14 (binary: 1110)


"""
Equal to (==):
The equal to operator compares two values and
returns True if they are equal, and False otherwise.
"""
a = 3
b = 3

result = a == b
print(result)   # Output: True
"""
Not equal to (!=):
The not equal to operator compares two values and 
returns True if they are not equal, and False if they are equal."""

a = 3
b = 4

result = a != b
print(result)   # Output: True

"""
Greater than (>):
The greater than operator compares two values and 
returns True if the first value is greater than the second, and False otherwise.
"""
a = 3
b = 4

result = a > b
print(result)   # Output: False

a = 5
b = 3

result = a > b
print(result)   # Output: True

"""
Less than (<):
The less than operator compares two values and 
returns True if the first value is less than the second, and False otherwise.
"""
a = 3
b = 4

result = a < b
print(result)   # Output: True
a = 2
b = 4

result = a < b
print(result)   # Output: True

"""
Greater than or equal to (>=):
The greater than or equal to operator compares two values and returns True if the left operand is greater
than or equal to the right operand, and False otherwise"""
a = 3
b = 4

result = a >= b
print(result)   # Output: False
a = 5
 
 
"""
Less than or equal to (<=):
The less than or equal to operator compares 
two values and returns True if the left operand is less than or equal to the right operand, and False otherwise.

"""
a = 3
b = 4

result = a <= b
print(result)   # Output: True
a = 2


result = a <= b
print(result)   # Output: False


"""
Bitwise XOR (^):
The bitwise XOR operator performs a bitwise XOR operation on the binary representations of two numbers. 
It compares the corresponding bits of the operands and produces a result where each bit is set to 1 
if both corresponding bits are different.
"""

a = 12    # binary: 1100
b = 10    # binary: 1010

result = a ^ b
print(result)   # Output: 8 (binary: 1000)

"""
Bitwise OR (|):
The bitwise OR operator performs a bitwise OR operation on the binary representations of two numbers. 
It compares the corresponding bits of the operands and produces a result where each bit is set to 1 
if at least one of the corresponding bits is 1.
"""

a = 12    # binary: 1100
b = 10    # binary: 1010

result = a | b
print(result)   # Output: 14 (binary: 1110)

"""
Bitwise AND (&):
The bitwise AND operator performs a bitwise AND operation on the binary representations of two numbers. 
It compares the corresponding bits of the operands and produces a result where each bit is set to 1 
if both corresponding bits are 1.
"""

a = 12    # binary: 1100
b = 10    # binary: 1010

result = a & b
print(result)   # Output: 8 (binary: 1000)
