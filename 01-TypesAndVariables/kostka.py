import secrets

suma = 0
i=0
while i < 3:
    num = secrets.randbelow(6) + 1
    print(num)
    i += 1
    suma += num
    
    
print(f"razem: {suma}")