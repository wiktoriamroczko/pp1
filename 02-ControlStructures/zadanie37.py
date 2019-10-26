x = int(input('Podaj pierwszą liczbę: '))
y = int(input('Podaj drugą liczbę: '))
z = int(input('Podaj trzecią liczbę: '))

o=0
lista = [x, y, z]

for liczba in lista:
    if lista[o] > lista[o+1] or lista[o] > lista[o-1]:
        if lista[o] < lista[o+1] or lista[o] < lista[o-1]:
            break
    else:
        o+=1
        
print (f'mediana: {lista[o]}')