def samogloski(txt):
    import re
    from collections import Counter
    x = re.findall('[aeiouy]', txt)
    return Counter(x)
    


txt = '''Nam strzelać nie kazano. Wstąpiłem na działo.
I spojrzałem na pole, dwieście armat grzmiało.
Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'''

print(samogloski(txt))