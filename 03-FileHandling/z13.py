x=0
with open ('tab.txt', 'a') as file:
    tab = ['32', '16', '5', '8', '24', '7']
    while True:
        file.write(f'{tab[x]}\n')
        x+=1
        if x>5:
            break
file.close()

file = open("tab.txt", "r")
print(file.read())