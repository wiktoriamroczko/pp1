def rzucKostka():
    import random
    return (int(random.randint(1, 6)))


rzuty = []
for i in range(3):
    rzuty.append(rzucKostka())
    
suma = 0
for i in rzuty:
    print (i, end = ' ')
    suma += i
    
print (f'suma: {suma}')