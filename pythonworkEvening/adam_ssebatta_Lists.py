#Lists are used to store multiple items
#Lists are ordered,changeable,and allows duplicate values
Afternoon=["Adam","Belar","Titi","Weti","Oscar"]
print(Afternoon)

#Duplicates in Lists
Morning=["Adam","Tracy","Titi","Adam","Oscar","Titi"]
print(Morning)

#List Length
print(len(Morning))

#List Type
print(type(Afternoon))

#Acess List items
print(Afternoon[2])
print(Afternoon[1])

#negative indexing,there is no zero,we start from -1
print(Afternoon[-1])

Afternoon.append("Plau")
print(Afternoon)
#Acessing rage of items
print(Afternoon[3:5])
#this means all beginning items excluding that at position 4
print(Afternoon[:4])
 
print(Afternoon[1:])

#Adding at a specific index
Afternoon.insert(0,"livi")
print(Afternoon)
#Removing list items
Afternoon.remove("livi")
print(Afternoon)
#remove list items using an index
Afternoon.pop(3)