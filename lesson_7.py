#Lists []

x = ["Ashwin","Deen Masi",32] #Can mix data types!
print(f"List: {x}") #Print the list
print(f"Len: {len(x)}") #Print the list length

#Index and positioning - zero based
print(f"Zero: {x[0]}") #Print the first item
print(f"Slice: {x[1:2]}") #Slice the list

x.append("Sushi")   #Adds at the end
x.append("Cider")   #Adds at the end
x.insert(1,"Cats")  #Adds to specific position (Will not replace)
print(x)

x.remove("Cats") #Remove an item
print(x)

i = x.index("Sushi") #Will raise an error if not found
print(f"Food: {x.pop(i)}")
print(x)

i = x.index("Cider")    #Will raise an error if not found
del x[i]    #Delete a specific item without returning it
print(x)

#Extending - Adds elements from another list
y = ["Cats","Dogs","Birds"]
x.extend(y)
print(x)

#Sort - sort, reverse (ascending/descending)
x.remove(32)
x.sort() # Will throw an error if there mixed types
print(f"Sorted: {x}")
x.reverse()
print(f"Reverse: {x}")

#Copy
y = x.copy() #Copies the elements into a new list

y.reverse()
y.append("Oranges")
print(x)
print(y)

#Delete the whole thing
del y
#print(y)

#Clear
x.clear()
print(f"Cleared:{x}")
print(len(x))

#Lists can contrain other lists [[],[],[]]
x=[]
y=[1,2,3]
z=["Ashwin","Deen Masi"]
x.append(y)
print(f"List in Lists: {x}")
x.insert(0,z)
print(f"List in Lists: {x}")
print(f"Len: {len(x)}")
print(f"Zero: {x[0][0]}")
print(f"One: {x[1][2]}")

#Changing items - positional
x = [1,2,3,4,5]
x[2] = "Test"
print(x)


