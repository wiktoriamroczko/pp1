class Student():
    
    def __init__(self, name, surname, album):
        self.name = name
        self.surname = surname
        self.album = album
        
    def __str__(self):
        return f'{self.name} {self.surname} {self.album}'
    
    def __eq__(self,other):
        return self.album == other.album
        
    def __it__(self,other):
        return self.album < other.album
            
s1= Student('Anna','Tomaszewska',141820)
s2= Student('Wojciech','Zbych',201003)
s3= Student('Maja','Kowalska',153202)
s4= Student('Marek','Migiel',138600)

lista = [s1,s2,s3,s4]

for i in lista:
    print(i)
    
print()
    
s = sorted(lista, key = lambda Student: Student.album)
for i in s:
    print(i)