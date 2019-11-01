tab = []

with open ('./numbersinrows.txt') as file:
    for num in file:
        x = num.split(',')
        for i in x:
            tab.append(int(i))
        
suma = 0
for l in tab:
    suma += l
    
print(f'liczb w pliku: {len(tab)}, suma: {suma}')