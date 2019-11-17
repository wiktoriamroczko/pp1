def wielkieL(string):
    import re
    d = re.findall('[A-Z]', string)
    for i in d:
        print(i, end='')
    return ''
        
txt = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
print(wielkieL(txt))