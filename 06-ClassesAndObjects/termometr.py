class thermometer():
    
    def __init__(self):
        self.is_on = False
        self.temperature = 0
        
    def temp_on(self):
        self.is_on = True
        
    def temp_off(self):
        self.is_on = False
        
    def check_temp(self):
        if self.is_on == True:
            import random
            x = round(random.uniform(34,42), 1)
            self.temperature = x
        
    def show_temp(self):
        if self.is_on == True:
            if self.temperature < 37:
                print (f'Zmierzona temperatura: {self.temperature} C')
            elif self.temperature > 41:
                print (f'Zmierzona temperatura: {self.temperature} C, Stan zagrożenia życia!!!')
            else:
                print (f'Zmierzona temperatura: {self.temperature} C, (gorączka)')

