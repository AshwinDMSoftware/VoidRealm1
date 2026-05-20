#The Cat class

#self is the first param
#It is equal to "this" in other languages
#Instance = created

class Cat:
    name = ''
    age = 0
    color = ''


    def __init__ (self,name, age=0,color='white'):
        self.name= name
        self.age = age
        self.color = color
        print(f'Contructor for {self.name}')

    def meow(self):
        print(f'{self.name} meow!')

    def sleep(self):
        print(f'{self.name} zzz')

    def hungry(self):
        for x in range(5):
            self.meow()

    def eat(self):
        print(f'{self.name} nom nom nom')

    def description(self):
        print(f'{self.name} is a {self.age} year old cat who is {self.color}')
