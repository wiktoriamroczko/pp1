x=int(input('Podaj wiek psa w ludzkich latach: '))

if x<=2:
    print (f'Wiek psa w psich latach to {x*10.5} lata.')
elif x>2:
    print (f'Wiek psa w psich latach to {2*10.5+(x-2)*4} lata.')
    