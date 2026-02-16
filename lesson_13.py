#For loop and range


#For loop on lists, typles, sets
x = [1,2,3,4] #List
y = (5,6,7,8) #Tuple
z = {9,10,11,12} #Set

for i in x:
    print(f'i = {i}')

#For loop on dictionaries
a = dict(Ashwin=32,Harold=31,John=25,Sarah=30)
print(a)

for k in a.keys():
    print(f'Keys: {k} = {a[k]}')

for k,v in a.items():
    print(f'Values: {k} = {v}')

#Range
x = range(5)
print(x)
for i in x:
    print(f'Range: {i}')

#Range start, stop and step
x = range(5,20,3)

print(x)
for i in x:
    print(f'Stepped: {i}')