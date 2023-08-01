#tuples
#A tuple is a collection which is ordered and unchangeable
#eg
tple = (2,34,5,6,7,8)
print(tple)


"""
Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets
eg
"""
print(tple[2])

"""
or you can use negative indices to acces the items in the tuple
Negative indexing means beginning from the end, -1 refers to the last item, -2
eg
"""
print(tple[-4])

#Allow duplicate values
phones=("samsag","Ipone","Techno","Iphone","Techo")
print(phones)
"""
To use the len() function with a tuple, you can create a tuple called phones and then use len() to determine its length.
In this example, the len() function is used to calculate the length of the phones tuple, which contains four elements. The result, 4, is then printed to the console.

"""
    
phones = ("iPhone", "Samsung", "Google Pixel", "Huawei")
print(len(phones))

#Tuples can have different datatypes
people=("adam","myname")
Number=(14,23,45,45)
print(type(Number))

#add items to a tuple(first convert the tuple to a list,then convert it back to the tuple)
Cars=("Rangerover","Benz","Ford")
z=list(Cars)
z.append("Tizi")
Cars=tuple(z)
print(Cars)


#putting 2 tuples in one tuple
#To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#looping through the tuples for loop
colors=("red","blue","orage")
for x in colors:
    print (x)


