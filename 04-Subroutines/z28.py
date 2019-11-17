def rysujWykres(jezyki, wartosci):
    tab = []
    for i in wartosci:
        x = i//3
        tab.append('#'*x)
    n = 0
    while n >= 0 and n < len(jezyki):
        print(f'{jezyki[n]}: {tab[n]}')
        n+=1
    return ''

jezyki = ['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosci = [61,47,37,32,26,18,14,14,9,7]
print (rysujWykres(jezyki, wartosci))

