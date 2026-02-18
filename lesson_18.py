#Packing and unpacking data

#Problem with *arg and **kwarg is we can not use lists and dictionaries
#Instead we have to pack and unpack the data

#Packing Data
def pack(*nums):
    print(f'Packed: {nums}')
    for x in nums:
        print(f'Packed: {x}')

pack(1,2,3)

#Unpacking Data
def unpack(a,b,c):
    print('Unpack')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

num = [1,2,3]
unpack(*num)

#Dictionary Issue
d = dict(name="Ashwin",age=32,pet='Cat')
print('Packing dictionary')
pack(*d)

print('Unpacking dictionary')
unpack(*d)

#Packing a dictionary
def packdict(**nums):
    print(f'nums = {nums}')
    for k in nums:
        print(f'Packed: {k} = {nums[k]}')
packdict(name="Ashwin",age=32,pet='Cat')

#Unpacking a dictionary
def unpackdict(name,age,pet):
    print('Unpacking a dictionary')
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'pet = {pet}')

d = dict(name="Ashwin",age=32,pet='Cat')
unpackdict(**d)