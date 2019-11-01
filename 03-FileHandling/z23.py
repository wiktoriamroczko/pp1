import re
tab = []

with open ('./land.txt') as file:
    for line in file:
        cyfra = re.findall('\d', line)
        for i in cyfra:
            tab.append(int(i))
        
suma = 0
for l in tab:
    suma += l
    
print (f'suma cyfr: {suma}')