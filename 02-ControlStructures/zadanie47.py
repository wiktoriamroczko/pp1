k = int(input('Podaj kwotę w zł: '))

while True:
    x = k//5
    k = k - x*5
    y = k//2
    k = k - y*2
    z = k//1
    k = k - z*1
    if k == 0:
        break
    
print (f'''5 zł: {x} szt
2 zł: {y} szt
1 zł: {z} szt''')