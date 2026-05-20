#Test class

class Person:
    #Weak Private
    _name = 'No Name'
    def setName(self,name):
        self._name = name

    #Strong Private
    def __think(self):
        print('Thinking to my self')

    def work(self):
        self.__think()
    #Before and After
    def __init__(self):
        print('Contructor')

    def __call__():
        print('call someone')
class Child(Person):
    def testDouble(self):
        self.__think(self)