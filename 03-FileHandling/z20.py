tab = []

with open ('./numbers.txt') as file:
    for num in file:
        tab.append(int(num))
        
with open ('./evennumbers.txt', 'a') as file:
    for num in tab:
        if num%2 == 0:
            file.write(f'{num}\n')   