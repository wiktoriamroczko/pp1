pin = '0805'
    
for i in range(3):
    p = (input('Podaj kod PIN: '))
    if p == pin:
        print ('Kod PIN poprawny')
        break
    else:
        print ('Kod PIN niepoprawny.')
else:
    print('Karta płatnicza zostaje zablokowana.')