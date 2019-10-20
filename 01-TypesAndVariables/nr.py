x= input("Podaj nr rachunku bankowego:")

while len(x) != 26:
    x= input("Podaj nr rachunku bankowego:")
    if len(x) == 26:
        break
    
v= x[:2]

for i in range(2, 23, 4) :
    v += f" {x[i : i + 4]}"
print(f"numer rachunku: {v}")