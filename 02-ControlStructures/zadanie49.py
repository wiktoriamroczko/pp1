print ('| PN | WT | SR | CZ | PT | SB | ND |')
nrDniaTygodnia =3
print ('|    '*nrDniaTygodnia, end='')

for i in range(1, 31):
    if i < 10:
        print ('|', i, end='  ')
    elif i >=10:
        print ('|', i, end=' ')
    if i == 7-nrDniaTygodnia:
        print ('|')
    if i == 14-nrDniaTygodnia:
        print ('|')
    if i == 21-nrDniaTygodnia:
        print ('|')
    if i == 28-nrDniaTygodnia:
        print ('|')
    if i==30:
        print ('|')
        
