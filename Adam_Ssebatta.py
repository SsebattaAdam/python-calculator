#Running python sripts
print('Runnin python script')
#PEP8 python guidelines
  #indentation
  #characters dont ecxeed 79
  #use underscore to separate words 
  #Snake_case
  #CamelCase:This is a camel case version
  
  #comments
  #This is a single line comment
 
"""
This is a multiline comment Multiline comments
"""
 #Variables
name="Adam"
age=22
print(name)
print(age)

#specifying the datatype
x=str(22)
y=int(23)
z=float(3)
print(x)
print(y)
print(z)

#DataStructures(Data types)
"""
Numeric values are 1-10
Numeric takes two forms:
intergers(int)
float e.g pi=3.14

Strings can be represented using single qoutes or double qoutes, e.g 'Adam' and "Adam ssebatta",Numbers in form of string eg "10",'4'

Boolean values are logical values either True or False
Booleans represent one of two values: True or False.

Sequence Types
"""
"""
list  is a collection which is ordered and changeable. Allows duplicate members.
it is enclosed with square brackets"[]" represented in ordered collection
"""

alist= [2,4,6,7,8,9]
print(alist)
# you can accesss the members individually or by itterarting through
#eg
#accessing an a uniquie element
print(alist[1])
for x in alist:
    print(z)


"""

tuple
A tuple is a collection which is ordered and unchangeable. 
they enclosed with parentheses ()

"""

datuple = (2,4,5,6,7,8,9)
print(datuple)
"""
can access tuple items by referring to the index number 
eg
"""
print(datuple[1])
print(datuple[0])
"""
a tuple can be change or alltered depending on what is need
"""


"""

range-use iteration,loops
 the range() function is a built-in function used to generate a sequence of numbers from the start inclussive, to the last number not inclussive
 It returns an object that represents a sequence of numbers within a specified range. The range() function can be called with up to three arguments: range(start, stop, step).

Here's an explanation of each argument:

start (optional): The starting point of the range (inclusive). If not provided, it defaults to 0.
stop (required): The ending point of the range (exclusive). It generates numbers up to, but not including, this value.
step (optional): The increment or step size between the numbers. If not provided, it defaults to 1.
The range() function returns an iterable object that can be used in various ways, such as in loops or in combination with other functions
eg

"""
for num in range(5):
    print(num)
# the range(5) function generates a sequence of numbers from 0 to 4
my_list = list(range(1, 6))
print(my_list)


"""
Mapping types
dict-dictionary is enclosed with cury brackets {}
eg
"""
{ 
name: 'Adam',age:22
}
#or
{name:'Jeff',age:30}

item_dict = {"Apple": None, "Mango": None, "Banana": None}
# unordered collection type,unique

#None Types:None represents absence of a value
"""
"""

hey=True
print(hey)