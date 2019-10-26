x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
z = int(input('Podaj trzecią liczbę: '))
lista = [x, y, z]

lista.sort()
for i in lista:
    print (i, end=' ')
    
    