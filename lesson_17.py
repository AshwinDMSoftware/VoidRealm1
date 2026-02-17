#Functions in depth

#No arguments
def test():
    print('Normal function')

print('\r\n------ No Arguments')
test()

#Positional and keyword Arguments
def message(name,msg,age):
    print(f'Hello {name}, {msg}, you are {age} years old')

print('\r\n------ Positional and Keyword Arguments')
message('Ashwin','Sup Nerd',32) #Positional
message('Ashwin',22,'This is wrong idiot') #Positional (wrong order)
message(msg='Good if you don\'t know the order', age=32,name='Ashwin') #Keywords
message('Ashwin', age=32, msg='This works as well') #Both


#Internal functions
def counter():
    def display(count = 0): #Function in a function
        print(f'Internal: {count}')
    for x in range(5): display(x)

print('\r\n------ Internal functions')
counter()
#display(15) Function is not defined in the global scope

#*args - positional variable length arguments
def multiply(*args):
    z = 1
    for num in args:
        print(f'Num = {num}')
        z*= num
    print(f'Multiply: {z}')
print('\r\n------ *args')
multiply(1,2,3,4)

# **kwargs is used to pass a keyworded, variable length arguments
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    display('name')
    display('age')
    display('pet')
    display('Something')

print('\r\n------ **kwargs')
profile(name='Ashwin',age=32)
profile(name='Ashwin',age=32,pet='cat')
profile(name='Ashwin',age=32,pet='cat',food='Sushi')

#Lamda functions (anonymous functions)
print('\r\n------ Lamda')
#normal
def makesqft(width=0, height=0):
    return width*height
print(makesqft(width=10, height=8))
print(makesqft(24,8))

#lambda
#z = lambda x: x*y
sqft = lambda width=0,height=0: width * height
print(sqft(width=10, height=8))
print(sqft(24,8))
