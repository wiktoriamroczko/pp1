class Kontakt():
    
    def __init__(self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon

class ListaKontaktow():
    
    def __init__(self):
        self.tab = []
        
    def nowy_kontakt(self,Kontakt):
        self.tab.append(Kontakt)
        
    def wyswietl_kontakty(self):
        for i in self.tab:
            print(i.nazwa, i.email, i.telefon)
        
k1 = Kontakt('Kowalski Jan', 'jank@onet.pl', 555234000)
k2 = Kontakt('Borek Patrycja', 'bp@o2.pl', 232000199)
k3 = Kontakt('Maj Piotr', 'maj@google.pl', 222999100)
k4 = Kontakt('Adamczyk Anna', 'ada@poczta.pl', 100200300)
l = ListaKontaktow()
l.nowy_kontakt(k1)
l.nowy_kontakt(k2)
l.nowy_kontakt(k3)
l.nowy_kontakt(k4)
l.wyswietl_kontakty()