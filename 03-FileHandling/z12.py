i = input('nazwa produktu: ')
f = open("shoppinlist.txt", "a")
f.write(f'{i}\n')
f.close()

f = open("shoppinlist.txt", "r")
print(f.read())
