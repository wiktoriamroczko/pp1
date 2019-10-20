import random
x= (random.randint(1,6))

i= int(input("Podaj, ile oczek kostki wyrzucił komputer:"))

print(f"Komputer wyrzucił:{x}")

if i==x:
    print ("zgadłeś")
else:
    print ("nie zgadłeś")