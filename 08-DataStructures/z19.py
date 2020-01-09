import json

with open("euro.json") as file:
    data = json.load(file)

print(f'%-10s' % 'DATA', f'%-7s' % 'KUPNO', 'SPRZEDAŻ')

n=0
for i in range(10):
    print (f'%-10s' % data['rates'][n]['effectiveDate'], f'%-7s' % data['rates'][n]['bid'], data['rates'][n]['ask'])
    n+=1