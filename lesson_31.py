#Class Inheritance

#Feline class
class Feline:
    def __init__(self,name):
        self.name = name
        print('Creating a feline')

    def meow(self):
            print(f'{self.name}: meow')

    def setName(self, name):
            print(f'{self} setting name: {name}')
            self.name = name

#Lion class
class Lion(Feline):
    def roar(self):
        print(f'{self.name} ROAR!!!!')

#Tiger class
class Tiger(Feline):
    #Override the contructor is a bad idea!!!
    def __init__(self):
        #Super alows is to access the parent
        #If we forget this we will have a bad time later
        super().__init__('No Name')
        print('Creating a tiger')

    def stalk(self):
        #Have to make sure name is set in the parent
        #this is considered - LBYL (loop before you leap)
        #here we are dynamically adding the attribute

        #If we did not init the super we will have to be careful
        #If not hasattr(self,'name'): super().setName('No Name')
        print(f'{self.name}: stalking')

    def rename(self, name):
        super().setName(name)

c = Feline('kittycat')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.roar()

t = Tiger() #is a Feline, but with a different constructor
print(t)
t.stalk()
t.rename('Tony')
t.meow()
t.stalk()