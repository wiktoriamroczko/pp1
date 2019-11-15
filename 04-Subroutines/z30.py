def losowa():
    import random
    return random.randint(1, 50)

tab = []
sumap = 0
sumanp = 0

for i in range(1000):
    tab.append(losowa())
    
for i in tab:
    if i % 2 == 0:
        sumap +=1
    else:
        sumanp +=1
        
p = sumap*100/1000
n = sumanp*100/1000
   
print ('Dla 1000 liczb losowych z przedziału: <1,50>:')
print (f'Liczby parzyste: {p}%')
print (f'Liczby nieparzyste: {n}%')