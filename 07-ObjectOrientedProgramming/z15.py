class Book():
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f'''Tytuł: {self.title}
Autor: {self.author}'''
        
class Ebook(Book):
    
    def __init__(self, title, author, file):
        Book.__init__(self, title, author)
        self.file = file
        
    def __str__(self):
        return 'Ebook \n' + super().__str__() + f'\nNazwa pliku, w którym książka jest zapisana: {self.file}'

class PaperBook(Book):
    
    def __init__(self, title, author, pp):
        Book.__init__(self, title, author)
        self.pp = pp
        
    def __str__(self):
        return 'Książka papierowa \n' + super().__str__() + f'\nLiczba stron: {self.pp}'
        
e = Ebook('Alchemik',' Paulo Coelho','Nowy folder')
print(e)
p = PaperBook('Alchemik',' Paulo Coelho',212)
print(p)