x= int(input("Podaj długość boku a:"))

y= int(input("Podaj długość boku b:"))

z= int(input("Podaj długość boku c:"))

p= 1/2*(x+y+z)
p2= p*(p-x)*(p-y)*(p-z)

from math import sqrt
P= sqrt(p2)
pole=int(P)

print (f"Pole trójkąta wynosi: {pole}")
