class Fraction():
    
    def __init__(self, numerator, denominator):
        
        self.numerator = numerator
        self.denominator = denominator
        
    def create(self):
        self.fr = f'{self.numerator} / {self.denominator}'
    
    def reduce(self):
        import math
        x = math.gcd(self.numerator, self.denominator)
        self.numerator //= x
        self.denominator //= x
        self.fr = f'{self.numerator} / {self.denominator}'
        
    def show_fr(self):
        print(self.fr)
        
fraction1 = Fraction(1,2)
fraction2 = Fraction(12,21)
fraction1.create()
fraction2.create()
fraction1.show_fr()
fraction2.show_fr()
fraction2.reduce()
fraction2.show_fr()