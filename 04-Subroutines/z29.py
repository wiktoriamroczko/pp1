def mediana(tab):
    tab.sort()
    return tab[int(len(tab)/2)]

def moda(tab):
    from collections import Counter
    s = Counter(tab)
    m = max(s, key=s.get)
    return m
    

tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

print(tab)
print(mediana(tab),'mediana')
print(moda(tab), 'dominanta')
