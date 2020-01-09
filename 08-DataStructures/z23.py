import json

with open("notowania.json") as file:
    data = json.load(file)

pom = 0

for i in data[0]['rates']:
    for k,j in i.items():
        print(k,":",j,)
    print('')