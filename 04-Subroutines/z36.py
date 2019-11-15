tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def suma(tab):
    s = 0
    for i in tab:
        o = isinstance(i, int)
        if o == True:
            s+=i
        else:
            s+=(suma(i))
    return s

print(suma(tab))