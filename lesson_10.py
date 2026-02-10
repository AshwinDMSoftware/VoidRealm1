#Dictionary {k:v,k:v}
#Indexed by keys which can be any immutable type

#Create a dictionary
d = {'pet':'dog','age':5,'name':'star'}
print(d)
d = dict(pet='dog',age=5,name='star')
print(d)

#Get keys and values
print(f'Items: {d.items()}')
print(f'Keys: {d.keys()}')
print(f'Values: {d.values()}')

#Getting a value from the key
print(f'Name: {d["name"]}')
#print(f'Test: {d["nope"]}') Throws key error

#Adding an item
d['trick'] = 'sit'
print(d)
d['trick'] = 'rollover'
print(d)

#Removing an item
del d['trick']
print(d)

#Testing for existence (covered in a future video)
if 'name' in d:
    print(d['name'])

#Looping
for key in d.keys():
    print(f'{key}: {d[key]}')