X = lambda a : True if a % 2 == 0 else False

tab = [1,2,3,4,5,6,7,8]

parzyste = filter(X, tab)

for i in parzyste:
    print (i, end=', ')