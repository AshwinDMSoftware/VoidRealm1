#Multiple Inheritance

#Inherit from multiple classes at the same time

#Vehical class
class Vechical:
    speed = 0
    def drive(self, speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Driving')

    def display(self):
        print(f'Driving at {self.speed} speed')

#Freezer class
class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')

#FreezerTruck class
class FreezerTruck(Freezer,Vechical): #Here we define the Method Resolution Order
    def display(self):
        print(f'Is a freezer: {issubclass(FreezerTruck, Freezer)}')
        print(f'Is a vehical: {issubclass(FreezerTruck, Vechical)}')

        #super(Vechical,self).display() #Fails because of MRO
        #super(Freezer,self).display()  #Works because of MRO

        Freezer.display(self)
        Vechical.display(self)
t = FreezerTruck()
t.drive(80)
t.freeze(-5)
print('-'*20)
t.display()