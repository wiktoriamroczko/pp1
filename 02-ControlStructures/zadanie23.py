tab=["niedostateczny", "mierny", "dostateczny", "dobry", "bardzo dobry", "celujący"]
x=int(input("Podaj ocenę: "))
if x-1<=len(tab):
    x-=1
    print (f"Ocena słownie: {tab[x]}")
    
    