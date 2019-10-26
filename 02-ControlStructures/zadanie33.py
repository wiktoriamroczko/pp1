cyfry = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
liczba = input('Podaj liczbę: ')
ln = []

for i in liczba:
    z = int(i)
    ln.append(z)
    print (cyfry[z], end=' ')
    

    