def wspak(txt):
    return(txt[::-1])

def szeroko(txt):
    for i in txt:
        print(i, end=' ')
    return ''

def form(txt):
    m = txt.lower()
    x = m.split(" ")
    for i in x:
        print (i.capitalize(), end=' ')
    return ''