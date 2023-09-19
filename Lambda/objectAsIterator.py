class Customers:
    counter = 1
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.no = Customers.counter
        Customers.counter += 1
    def intro(self):
        print('Hi, my name is ', self.name , ' and I am ', self.age , ' years old and I am customer number ', self.counter)
    @staticmethod
    def getCounter():
        return Customers.counter
    @staticmethod
    def setCounter(newValue):
        if type(newValue) == int:
            Customers.counter = newValue
        else:
            print('pls enter integer value of counter')
c1= Customers('Abhimanyu', 24)
c2 = Customers('Fahar', 21)
c3 = Customers('US', 100)
L= [c1, c2, c3]
for i in L:
    i.intro()
