ld = int(input('Podaj liczbę: '))
bin = []

while True:
    if ld%2 == 0:
        print (f'{int(ld)}|0')
        ld = ld - (ld//2)
        bin.append(0)
    elif ld%2 == 1:
        print (f'{int(ld)}|1')
        ld = ld - (ld//2) - 1
        bin.append(1)
    if ld == 0:
        break
    
bin.reverse()
for i in bin:
    print (i, end=' ')