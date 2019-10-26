pesel = input('Podaj numer pesel: ')
    
if int(pesel[9]) % 2 == 0:
    print ('Płeć: Kobieta')
else:
    print ('Płeć: Mężczyzna')
    
    
if int(pesel[0:2]) <= 18:
    print (f'wiek: {18-int(pesel[0:2])}')
elif int(pesel[0:2]) > 18:
    print (f'wiek: {(100-int(pesel[0:2]))+18}')

