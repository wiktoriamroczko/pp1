def bezPowtorzen(n):
    from collections import Counter
    s = Counter(n)
    for x, y in s.items():
        if y == 1:
            print (x, end=', ')
    return ''
        

n = [3,3,5,6,7,4,2,2,4,5,9,0]
print (n)
print (f'{bezPowtorzen(n)} nie powtarzają się')