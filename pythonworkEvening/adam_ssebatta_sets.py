#store multiple items  in the singlevariable
#unchangable
"""
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
"""


food={"rice","matooke","irish","potato"}
print(food)
#duplicates in sets
foodie={"rice","matooke","irish","potato","rice","rice"}
#Exercise:Length of the set,datatype,
"""
created a set called fruits with four elements. We use the len() function to calculate the length of the set, which is 4. 
The type() function is used to determine the data type of the set, which is set.
"""
fruits = {"apple", "banana", "orange", "mango"}
print(len(fruits))     # Output: 4
print(type(fruits))    # Output: <class 'set'>

# accessing items in a set,adding items ,add two sets together

fruits = {"apple", "banana", "orange", "mango"}
for fruit in fruits:
    print(fruit)
#we iterate over the fruits set using a for loop and print each item. The loop traverses the set and outputs each element on a separate line.

#length
food={"rice","matooke","irish","potato"}
print(len(food))
#finding the datatype
print(type(food))
#accessing elements in a set
"""Acess List items,we cant access but we can
#loop through the srt items using a for loop or ask
if a specific value is present using the in keyword
"""
food={"rice","matooke","irish","potato"}
for x in food:
    print(x)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
 #Checking if item is there
food={"rice","matooke","irish","potato"}
print("rice"in food)#outputs true

  #Adding items to the set
food={"rice","matooke","irish","potato"} 
food.add("Chicken")
print(food)

# #Adding multiple items we use update()
# food={"rice","matooke","irish","potato"}
# food.update(["kikomado","fish"])

#Joining two sets
set1={1,2,3,4}
set2={5,6}
set3=set1.union(set2)
print(set3)