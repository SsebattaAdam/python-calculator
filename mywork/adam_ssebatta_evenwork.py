#Creating and Accessing Dictionary Items:

myDic = {
    "phone": "iphone",
    "phonemodel": "iphone",
    "year": 2023,
    "Name": "SSEBATTA ADAM",
    "RegNO": "21/U/0534"
}
print(myDic)

# Length of a dictionary
print(len(myDic))

# Accessing dictionary items
z = myDic["year"]
print(z)

y = myDic.get("phonemodel")
print(y)

# Accessing dictionary keys
w = myDic.keys()
print(w)

#Using values() Method
Person = {
    "Country": "Ugandan",
    "Religion": "Catholic",
    "Date_Of_Birth": "2007"
}
x = Person.values()
print(x)

#Checking if a Key Exists
dict = {"a": 1, "b": 2, "c": 3}
if "a" in dict:
    print("Exists")
else:
    print("Does not exist")
#Changing and Updating Dictionary Items
Car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Changing an item
Car["year"] = 2018
print(Car)

Car_Stuff = {
    "brand": "Benz",
    "model": "Fordk",
    "year": 1964
}

# Updating an item
Car_Stuff.update({"year": 2023})
print(Car_Stuff)

#Adding and Removing Dictionary Items
# Adding an item
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict1["color"] = "red"
print(dict1)

# Removing an item
Fruits = {
    "color": "green",
    "size": "big",
    "amount": 2
}

if "model" in Fruits:
    Fruits.pop("model")
else:
    print("Key 'model' does not exist in the dictionary.")

print(Fruits)

#Looping Through a Dictionary and Nesting Dictionaries
# Looping through a dictionary
Car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for key, value in Car.items():
    print(key, value)

# Nesting dictionaries
Person = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

print(Person["address"]["city"])



#Booleans
print(10<5)
print(60==20)
print(40>10)
#Exercise use a condition to show how to use booleans

num = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is either zero or negative.")


name = ""

if bool(name):
    print("The name is not empty.")
else:
    print("The name is empty.")
    
    
    num = 12

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
fruits = ["apple", "banana", "cherry"]
search_fruit = "banana"

if search_fruit in fruits:
    print("The fruit is in the list.")
else:
    print("The fruit is not in the list.")

#Format string
#Works when you want to combine astring and a number
age=22
name="My name is Adam and my age is {} "

print(name.format(age))

#Strings
print("Fruits")
print('Fruits')

#Assiign string to a variable
w="Fruits"
print(w)
#Multiline strings
q="""I am a Software engineer,year 2
learning recess
    """
print(q)
#Strings as arrays
a="Adam"
print(a[1])#outpus r because it is at position 1

#Exercise 1:use thelen()function to determinr the length of the string
text = "Hello, World!"
print(len(text))  # Outputs 13

#Execise 2:Give an example of using a for loop in a string
text = "Hello"
for char in text:
    print(char)

#Exercise 3:Give an example of slicing in strings
text = "Hello, World!"
print(text[7:])  # Outputs "World!" by slicing from index 7 to the end of the string


#how to modify strings
a="Cars"
print(a.lower())
print(a.upper())

#Remove white space
b=" Afternoon "
print(b.strip())#removes spaces at the beginning and end
#String concantination
c="Class"
d="chair"
w=c+ " " + d
print(w)