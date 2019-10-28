tab = []
with open ('./numbers.txt') as file:
    for l in file:
        z=int(l)
        tab.append(z)
        
suma = (sum(tab))
print(suma)
        
      