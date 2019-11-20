import math

def czytajWspolczynniki():
    tab = []
    for _ in range(3):
        x = float(input('Podaj współczynnik:'))
        tab.append(x)
    return tab

def obliczDelte(tab):
    a = tab[0]
    b = tab[1]
    c = tab[2]
    delta = b**2 - 4*a*c
    return delta
    
def pierwiastki(tab):
    a = tab[0]
    b = tab[1]
    p = []
    delta = obliczDelte(tab)
    if delta < 0:
        return p
    elif delta == 0:
        x=(-b)/(2*a)
        p.append(x)
        return p
    else:
        pw = math.sqrt(delta)
        x1 = (-b-pw)/(2*a)
        x2 = (-b+pw)/(2*a)
        p.append(x1)
        p.append(x2)
        return p

    
def wyswietlPierwiastki(p):
    print (f'Pierwiastki równania: {p}')
    return ''