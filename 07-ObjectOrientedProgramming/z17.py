class Area():
    
    @staticmethod
    def triangle(a,h):
        p = (1/2)*a*h
        return p
    
    @staticmethod
    def rectangle(a,b):
        p = a*b
        return p
    
    @staticmethod
    def circle(r):
        from math import pi
        p = pi*r**2
        return p
    
t= Area()
print(t.circle(3))
print(t.rectangle(4,7))
print(t.triangle(6,2))