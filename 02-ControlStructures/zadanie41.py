i=0
j=0
while True:
    x = (int(input('Podaj liczbę: ')))
    i += x
    j += 1
    if x == 0:
        break
print(f'liczb: {j-1}, suma: {i}, średnia: {i/j}')