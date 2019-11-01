tab = []
with open ('./numbers.txt') as file:
    for i in file:
        tab.append(int(i))
 
tab.sort()
for liczba in tab:
    print(liczba, end=' ')