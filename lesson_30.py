#Introduction to classes

#OOP - Object Oriented Programming
#Blue prints for creating objects
#Classes are a big topic

#Create the class

#Import the class
import sub30.cat
from sub30.cat import Cat

#Use the class
def test():
    b = Cat('Kai',2,'Brown')
    c = Cat('Luna', 8, 'Grey')
    print(b)
    print(c)
    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

if __name__ == "__main__":
    x = Cat('test')
    print(x)
    test()