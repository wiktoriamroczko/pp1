class Rachunek():
    
    def __init__(self, numer):
        
        self.numer = numer
        self.saldo = 0
        if len(str(self.numer)) != 26:
            print('Nieprawidłowy numer!')
            
        s = str(self.numer)
        self.p = s[:2]
        
        for i in range(2,23,4):
            self.p += f' {s[i:i+4]}'
        
    def wplata(self, kwota):
        
        self.saldo += kwota
        
    def wyplata(self, kwota):
        
        if kwota <= self.saldo:
            self.saldo -= kwota
        else:
            print('Niewystarczająca ilość środków na rachunku')
            
    def inf(self):
        
        print(f'Rachunek nr: {self.p} \nSaldo: {self.saldo} zł \n')