def jestImie(imie, imiona):
    print (f'imie: {imie}')
    
    for i in imiona:
        print (i, end = ', ')

    for i in imiona:
        if i == imie:
            return ('rezultat: imie zawarte jest w wykazie imion')

    
imiona = ['Arek', 'Klaudia', 'Jakub', 'Patrycja']
print(jestImie('Jakub', imiona))
    