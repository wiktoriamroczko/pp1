import re
tab = []

with open ('C:/Users/Wiktoria/Desktop/students.txt') as file:
    for line in file:
        wiek = re.findall('\d\d', line)
        for w in wiek:
            if int(w) < 30:
                z = line.split(',')
                print(z[0], z[1], z[4])