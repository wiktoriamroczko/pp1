class Sala():
    
    def __init__(self,nazwa,liczba_miejsc):
        self.nazwa = nazwa
        self.liczba_miejsc = liczba_miejsc
        
    def __str__(self):
        return f"nazwa: {self.nazwa}, liczba miejsc: {self.liczba_miejsc}"
    
class Sale(Sala):
    
    def __init__(self):
        self.wykaz_sal = []
    
    def dodaj(self,Sala):
        self.wykaz_sal.append(Sala)
        
    def liczba_sal(self):
        return len(self.wykaz_sal)
    
    def razem_miejsc(self):
        x = 0
        for i in self.wykaz_sal:
            x += i.liczba_miejsc
        return x

    def liczbaMiejsc(self,nazwa_sali):
        for i in self.wykaz_sal:
            if i.nazwa == nazwa_sali:
                return i.liczba_miejsc
            else:
                return 0
            
    def liczba_sal_przedzial(self,od,do):
        self.tab = []
        for i in self.wykaz_sal:
            if i.liczba_miejsc >= od and i.liczba_miejsc <= do:
                self.tab.append(i)
        return len(self.tab)

    def print(self):
        for i in self.wykaz_sal:
            print(f"nazwa: {i.nazwa}, liczba miejsc: {i.liczba_miejsc}")
 
