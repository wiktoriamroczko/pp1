a = int(input('Podaj długość boku a: '))
b = int(input('Podaj długość boku b: '))
print(b* '*')
for i in range(0, (a-2)):
    if a!=1:
        print ('*' + ' '*(b-2) + '*')
print(b* '*')