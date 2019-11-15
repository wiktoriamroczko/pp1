def suma(tablica):
    suma = 0
    for i in tablica:
        print (i, end=' ')
        suma += i
    print (f'suma: {suma}')
    
tablica = [4, 3, 7, 1, 3]
suma(tablica)
    