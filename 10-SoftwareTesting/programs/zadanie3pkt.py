class Prostokat():
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def obliczPole(self):
        self.pole = self.a*self.b
        
    def __add__(self,other):
        self.pole += other.pole
        return self
        
    def __str__(self):
        return f"{self.pole}"

