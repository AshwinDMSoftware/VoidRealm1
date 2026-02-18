#Global

#Global keyword which allows code to modify a variable
#outside of the current scope
x = 1
def test():
    x = 6
    print(x)

test()
print(x)