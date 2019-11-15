def nwz(n, x, y):
    tab = []
    for i in range(x, y+1):
        tab.append(i)
    if n in tab:
        return True
    else:
        return False
    
print (nwz(5,1,4))