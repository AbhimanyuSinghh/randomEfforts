class customers:
    def __init__(self, name, gender: str, address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def editProfile(self, newName, newGender, newCity, newPincode, newState):
        self.name = newName
        self.gender = newGender
        self.address.changeAddress(newCity, newPincode, newState)
    
    
class address:
    def __init__(self, city, pinCode, state) -> None:
        self.city = city
        self.pinCode = pinCode
        self.state = state
        
    def changeAddress(self, newCity, newPinCode, newState):
        self.city = newCity
        self.pinCode = newPinCode
        self.state = newState
        
#creating the objects of address and customers class

add = address('Hamirpur', 210301, 'Uttar Pradeesh')
cust = customers('Abhimanyu', 'Male', add)

#using editProfile method of customers class to change the details

cust.editProfile('Abhimanyu Zigolo', 'Still Male', 'Noida', 780001, 'Uttar Pradesh')

#printing the details changed above to check validity of the aggregation topic

print(cust.name)
print(cust.address.city)