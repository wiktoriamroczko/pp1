imiona = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']

dl = imiona[0]

for i in imiona:
    if len(dl) < len(i):
        dl = i
        
print (f'Najdłuższe imię: {dl}')