def wystepuje(liczba, tablica):
    print (f'liczba: {liczba}')
    print (f'tablica: {tablica}')
    if liczba in tablica:
        print ('Podana liczba występuje w tablicy.')
    else:
        print ('Podana liczba nie występuje w tablicy.')
    
tablica = [15, 38, 7, 23, 14]
wystepuje(23, tablica)