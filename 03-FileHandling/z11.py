with open ('DanePersonalne.txt', 'w') as file :
    file.write('Wiktoria Mroczko\nUEK\nInformatyka Stosowana')
    file.close()
    
z = open ('DanePersonalne.txt')
print (z.read())