lp = int(input('Podaj limit prędkości (km/h): '))
v = int(input('Podaj prędkość pojazdu (km/h): '))

if v-lp <= 10:
    m=(v-lp)*5
elif v-lp > 10:
    m=(v-lp-10)*15 + 50
    
print(f'Mandat (zł): {m}')