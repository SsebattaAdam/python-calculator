names = ["John", "Emily", "Michael", "Sarah", "David"]
names = ["John", "Emily", "Michael", "Sarah", "David"]
print(names[1])  # Outputs "Emily"


names = ["John", "Emily", "Michael", "Sarah", "David"]
names[0] = "Robert"
print(names)  # Outputs ["Robert", "Emily", "Michael", "Sarah", "David"]

names = ["John", "Emily", "Michael", "Sarah", "David"]
names.append("Olivia")
print(names)  # Outputs ["John", "Emily", "Michael", "Sarah", "David", "Olivia"]


names = ["John", "Emily", "Michael", "Sarah", "David"]
names.insert(2, "Bathel")
print(names)  # Outputs ["John", "Emily", "Bathel", "Michael", "Sarah", "David"]

names = ["John", "Emily", "Michael", "Sarah", "David"]
del names[3]
print(names)  # Outputs ["John", "Emily", "Michael", "David"]

#Use negative indexing to print the last item in your list
names = ["John", "Emily", "Michael", "Sarah", "David"]
print(names[-1])  # Outputs "David"

#Creating a new list with 7 items and printing the 3rd, 4th, and 5th items
new_list = ["Apple", "Banana", "Orange", "Grape", "Mango", "Pineapple", "Cherry"]
print(new_list[2:5])  # Outputs ["Orange", "Grape", "Mango"]



countries = ["USA", "Canada", "France", "Germany", "Japan"]
countries_copy = countries.copy()

print(countries)        # Original list: ["USA", "Canada", "France", "Germany", "Japan"]
print(countries_copy)   # Copied list: ["USA", "Canada", "France", "Germany", "Japan"]


countries = ["USA", "Canada", "France", "Germany", "Japan"]
for country in countries:
    print(country)

#Write a list of animal names and sort them in both descending and ascending order.

animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Zebra"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)

print(ascending_order)   # Outputs ["Elephant", "Giraffe", "Lion", "Tiger", "Zebra"]
print(descending_order)  # Outputs ["Zebra", "Tiger", "Lion", "Giraffe", "Elephant"]


animal_names = ['lion', 'elephant', 'tiger', 'giraffe', 'zebra']
names_with_a = [name for name in animal_names if 'a' in name]

print("Animal names with the letter 'a':", names_with_a)


first_names = ['John', 'Jane', 'David']
second_names = ['Doe', 'Smith', 'Johnson']

full_names = [first + ' ' + second for first, second in zip(first_names, second_names)]

print("Full Names:", full_names)


#exercise no 2

x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])  # Outputs "iphone"


my_tuple = (1, 2, 3, 4, 5)


print( my_tuple[-2])

#  Update "iphone" to "itel"
x = list(x)  # Convert tuple to a list to modify it
index = x.index("iphone")
x[index] = "itel"
x = tuple(x)  # Convert the list back to a tuple
print("Updated tuple:", x)

x = ("samsung", "iphone", "tecno", "redmi")
new_tuple = x + ("Huawei",)

print("Updated tuple:", new_tuple)

# Task 4: Loop through the tuple
x = ("samsung", "iphone", "tecno", "redmi")

print("Looping through the tuple:")
for item in x:
    print(item)

# Task 6: Remove the first item in the tuple
x = x[1:]
print("Tuple after removing the first item:", x)

# Task 7: Create a tuple of cities in Uganda using the tuple() constructor
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print("Tuple of cities in Uganda:", uganda_cities)


# Unpacking the tuple
x = ("samsung", "iphone", "tecno", "redmi")

# Unpack the tuple into separate variables
brand1, brand2, brand3, brand4 = x

# Print the unpacked variables
print("Unpacked brands:")
print("Brand 1:", brand1)
print("Brand 2:", brand2)
print("Brand 3:", brand3)
print("Brand 4:", brand4)


# Task 8: Print the 2nd, 3rd, and 4th cities using a range of indexes
uganda_cities = ("Kampala", "Entebbe", "Jinja", "Gulu")
cities_range = uganda_cities[1:4]

print("Cities:", cities_range)

# Task 9: Join two tuples containing first names and second names
first_names = ("John", "Jane", "David")
second_names = ("Doe", "Smith", "Johnson")
full_names = first_names + second_names

print("Full names:", full_names)

# Task 10: Create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
multiplied_colors = colors * 3

print("Multiplied colors:", multiplied_colors)

# Task 11: Count the number of times 8 appears in a tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_eight = thistuple.count(8)

print("Number of times 8 appears:", count_eight)



#sets
#  1: Create a set of 3 favorite beverages using the set() constructor
beverages = set(("coffee", "tea", "juice"))

print("Favorite beverages:", beverages)

# 2: Add 2 more items to the beverages set
beverages.add("water")
beverages.update(["soda", "milk"])

print("Updated beverages:", beverages)

#  3: Check if "microwave" is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_microwave_present = "microwave" in mySet

print("Is 'microwave' present?", is_microwave_present)

# 3: Remove "kettle" from the set
mySet.remove("kettle")

print("Updated set:", mySet)

# Task 5: Loop through the set
print("Elements in the set:")
for item in mySet:
    print(item)

# 6: Add elements from a list to a set
mySet2 = {"chair", "table", "lamp", "oscar"}
myList = ["pen", "paper"]
mySet2.update(myList)

print("Updated set with list elements:", mySet2)

#  7: Join two sets containing ages and first names
ages = {20, 30, 40}
first_names = {"John", "Jane", "David"}
joined_set = ages.union(first_names)

print("Joined set:", joined_set)


#string
# 1: Concatenate an integer and a string
num = 10
text = " years old"
concatenated = str(num) + text

print("Concatenated string:", concatenated)

#  2: Output the string without spaces at the beginning, in the middle, and at the end
txt = " Hello, Uganda! "
stripped = txt.strip()

print("Stripped string:", stripped)

#  3: Convert the value of 'txt' to uppercase
uppercase_txt = txt.upper()

print("Uppercase string:", uppercase_txt)

#  4: Replace character 'U' with 'V' in the string
replaced_txt = txt.replace('U', 'V')

print("Replaced string:", replaced_txt)

#  5: Return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
range_of_chars = y[1:4]

print("Range of characters:", range_of_chars)

#  6: Correct the code that gives an error
x = 'All "Data Scientists" are cool!'

print("Corrected string:", x)


# 1: Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print("Shoe size:", Shoes["size"])

#  2: Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

print("Updated brand:", Shoes["brand"])

#  3: Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"

print("Updated dictionary:", Shoes)

#  4: Return a list of all the keys in the dictionary
keys_list = list(Shoes.keys())

print("Keys:", keys_list)

#  5: Return a list of all the values in the dictionary
values_list = list(Shoes.values())

print("Values:", values_list)

#  6: Check if the key "size" exists in the dictionary
is_size_key_present = "size" in Shoes

print("Is 'size' key present?", is_size_key_present)

#  7: Loop through the dictionary
print("Dictionary items:")
for key, value in Shoes.items():
    print(key, ":", value)

#  8: Remove "color" from the dictionary
Shoes.pop("color")

print("Updated dictionary:", Shoes)

#  9: Empty the dictionary
Shoes.clear()

print("Empty dictionary:", Shoes)

#  10: Make a copy of a dictionary
original_dict = {"a": 1, "b": 2, "c": 3}
copy_dict = dict(original_dict)

print("Original dictionary:", original_dict)
print("Copy dictionary:", copy_dict)

#  11: Nested dictionaries
nested_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
}

print("Nested dictionary:", nested_dict)
