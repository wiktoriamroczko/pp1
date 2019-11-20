import re
import statistics

f = open('employees.csv', 'r')
txt = (f.read())
wiek = re.findall('\d\d', txt)

tab = []
for i in wiek:
    i = int(i)
    tab.append(i)

print('średnia arytmetyczna: ', statistics.mean(tab))
print('mediana: ', statistics.median_grouped(tab))
print('odchylenie standardowe: ', statistics.pstdev(tab))
