def cyfry():
    for i in range (1, 10, 3):
        for j in range (0, 3):
            print (f'{i+j}', end=' ')
        print ()

print('Cyfry: ')
cyfry()