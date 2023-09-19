class Customers:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def intro(self):
        print('Hi, my name is ', self.name , ' and I am ', self.age , ' years old')
c1= Customers('Abhimanyu', 24)
c2 = Customers('Fahar', 21)
c3 = Customers('US', 100)
L= [c1, c2, c3]
for i in L:
    i.intro()