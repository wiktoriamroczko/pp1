class Student():
    
    uczelnia = 'UEK Kraków'
    numer = 100000
    
    def __init__(self,imie,nazwisko,kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.album = Student.numer
        Student.numer += 1
        
    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({self.album}), {self.kierunek}, {Student.uczelnia}'
        
s = Student('Wiktoria', 'Mroczko', 'Informatyka stosowana')
s1 = Student('Patrycja', 'Żółkiewska', 'Informatyka stosowana')
print(s)
print(s1)