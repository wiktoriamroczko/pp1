class E_book():
    
    def __init__(self, title, author, pp):
        
        self.title = title
        self.author = author
        self.pp = pp
        self.current_pp = 1
        self.is_open = False
        
    def open(self):
        self.is_open = True
        
    def close(self):
        self.is_open = False
        
    def next_p(self):
        if self.is_open == True:
            self.current_pp += 1
        else:
            print('Książka jest zamknięta!')
      
    def prev_pp(self):
        if self.is_open == True:
            self.current_pp -= 1
        else:
            print('Książka jest zamknięta!')
            
    def show_status(self):
        if self.is_open == True:
            print(f'Tytuł: {self.title}, autor: {self.author}, liczba stron: {self.pp}, nr bieżącej strony: {self.current_pp}')