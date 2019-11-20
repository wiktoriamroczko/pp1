import QuadraticEquation

t = QuadraticEquation.czytajWspolczynniki()
delta = QuadraticEquation.obliczDelte(t)
p = QuadraticEquation.pierwiastki(t)

print(f'Równanie kwadratowe postaci: {int(t[0])}x2+{int(t[1])}x+{int(t[2])}')
print(QuadraticEquation.wyswietlPierwiastki(p))