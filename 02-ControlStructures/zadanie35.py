a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

from math import sqrt
delta = b**2 + (-4)*a*c
p_delty = sqrt(delta)

x1 = (-b -(p_delty))/2
x2 = (-b +(p_delty))/2

print(f'x1= {x1}')
print(f'x2= {x2}')