n = int(input('podaj n: '))
pierwsze = []

for i in range(n):
    for x in range(2, i):
        if (i % x) == 0:
            break
        else:
            if( x == i-1):
                pierwsze.append(i)
                
        
print ('Liczby pierwsze: ')
print (pierwsze)