class University():

    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Karkowie'

    # zachowania obiektu (metody)
    def print_name(self):  
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name
        
    def print_fullname(self):
        print(self.fullname)
    
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
    
        
n = University()
n.print_name()
n.print_fullname()

n2 = University()
n2.set_name('AGH')
n2.print_name()
n2.set_fullname('Akademia Górniczo Hutnicza')
n2.print_fullname()