def podatek(dochod):
    if dochod <= 5000:
        pod = dochod * 0.17
        return (f'Podatek należny: {int(pod)}zł')
    else:
        x = 5000 * 0.17
        roz = dochod - 5000
        pod = x + roz * 0.32
        return (f'Podatek należny: {int(pod)}zł')

x = (int(input('Podaj dochód: ')))
print (podatek(x))