class Phone():
    
    def __init__(self, phone_number, brand, operating_system):
        self.phone_number = phone_number
        self.brand = brand
        self.operating_system = operating_system
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def __str__(self):
        if self.is_on == False:
            return f'''Phone number: {self.phone_number}
Brand: {self.brand}
Operating system: {self.operating_system}
Phone is off'''
        else:
            return f'''Phone number: {self.phone_number}
Brand: {self.brand}
Operating system: {self.operating_system}
Phone is on'''
        
p1 = Phone(987876765, 'Sony', 'Android')
p1.turn_on()
p2 = Phone(876098432, 'iPhone', 'iOS')

print(p1)
print(p2)