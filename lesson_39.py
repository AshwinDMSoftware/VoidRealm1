#Map
#Looping without a loop
#Maps function calls to a collection of items
#maps(func, iterables)
#Basic usage - Count len
people = ['Matt', 'Bryan', 'Tammy', 'Markus']

#old way
count = []
for x in people:
    count.append(len(x))
print(f'Old Way: {count}')

#modern way
print(f'Mapped: {list(map(len,people))}')

#More complex - Combine elements
#Notice different lens, we are also passing multiple args

firstnames = {'Apple','Choclate','Fudge','Pizza'}
lastnames = {'Pie','Cake', 'Brown'}

def merg(a,b):
    return a + ' ' + b

x = map(merg,firstnames,lastnames)
print(list(x))

#Multiplle functions - combine functions
#Call multiple functions in one map call

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def doall(func,num):
    return func(num[0],num[1])

f = (add,subtract,multiply,divide)
v = [[5,3]]
n = list(v) * len(f)
print(f'f:{f}, n{n}')

m = map(doall,f,n)
print(list(m))