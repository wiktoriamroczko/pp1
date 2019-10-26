jeden = 0
dwa = 0
trzy = 0
cztery = 0
piec = 0
szesc = 0

for i in range(100):
    import random
    x= (random.randint(1,6))
    print (x)
    if x == 1:
        jeden+=1
    if x == 2:
        dwa+=1
    if x == 3:
        trzy+=1
    if x == 4:
        cztery+=1
    if x == 5:
        piec+=1
    if x == 6:
        szesc+=1
        
print(jeden)
print(dwa)
print(trzy)
print(cztery)
print(piec)
print(szesc)