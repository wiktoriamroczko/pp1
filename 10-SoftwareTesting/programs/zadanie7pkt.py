class Stos:
    
    def __init__(self):
        self.tab = []
        
    def zdejmij(self):
        return self.tab.pop()
    
    def wstaw(self,nazwa_karty):
        self.tab.append(nazwa_karty)
    
    def is_empty(self):
        return len(self.tab) == 0
        