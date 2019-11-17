def transpozycja(macierz):
    n=0
    for s in range(len(macierz)):
        for i in macierz:
            print(i[n], end=' ',)
        print ('')
        n+=1
    return ''
        
macierz = [[1,2,0],[0,0,3],[5,1,1]]

print('macierz:')
for i in macierz:
    for j in i:
        print(j,end=' ')
    print('')
        
print('macierz transponowana:')
print(transpozycja(macierz))