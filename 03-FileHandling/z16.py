import re
txt = 'wtorek - 23C, środa - 21C, czwartek - 25C'
x = re.findall('\d{2}', txt)
r=0
for temp in x:
    r+=int(temp)
    
print(f'Średnia temperatura: {int(r/3)}')