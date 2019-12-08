import kostka

k1 = kostka.Kostka()
k2 = kostka.Kostka()
k3 = kostka.Kostka()

tab1=[k1,k2,k3]

for i in range(3):
    tab2=[]
    for i in tab1:
        x = i.rzuc()
        print(x)
        tab2.append(x)
    
    print(f'suma oczek: {sum(tab2)}')
    del tab2