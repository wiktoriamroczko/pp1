tab = []
with open ('./universitiess.txt') as file:
    for uni in file:
        tab.append(uni)
        
tab.sort()
print(tab)

with open ('./universitiess.txt', 'w') as file:
    for i in tab:
        file.write(i)