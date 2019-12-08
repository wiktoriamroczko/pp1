class Samolot():
    
    def __init__(self, rodzaj, numer, st, doc):
        self.rodzaj = rodzaj
        self.numer = numer
        self.wysokosc = 0
        self.st = st
        self.doc = doc
        self.lot = False
        
    def start(self, wysokosc):
        if wysokosc >= 1000 and wysokosc <= 2000:
            self.wysokosc = wysokosc
            self.lot = True
            
    def zwieksz_wysokosc(self, x):
        if self.lot == True:
            if self.wysokosc + x <= 11000:
                self.wysokosc += x
            else:
                print('Samolot może zmienić wysokość lotu tylko w zakresie od 300m do 11000m!')
            
    def zmniejsz_wysokosc(self, x):
        if self.lot == True:
            if self.wysokosc - x >= 300:
                self.wysokosc -= x
            else:
                print('Samolot może zmienić wysokość lotu tylko w zakresie od 300m do 11000m!')
                
    def wyladuj(self):
        if self.lot == True:
            if self.wysokosc < 500:
                self.wysokosc = 0
                self.lot = False
            else:
                print('Zbyt duża wysokość dla lądowania. Obniż lot.')
                
    def info(self):
        print(f'Z: {self.st} do: {self.doc} \nTu {self.numer}, moja wysokość lotu to {self.wysokosc}m')
            
s = Samolot('Embraer', 'LOT881', 'VIENNA', 'WARSAW')
s.start(1500)
s.info()
s.zwieksz_wysokosc(7400)
s.info()
s.zmniejsz_wysokosc(8700)
s.zmniejsz_wysokosc(8600)
s.info()
s.wyladuj()
s.info()