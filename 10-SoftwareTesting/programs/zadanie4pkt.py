class Zbiory():
        
    @staticmethod
    def iloczyn(zbior1,zbior2):
        tab = []
        for i in zbior1:
            if i in zbior1 and i in zbior2:
                tab.append(i)
        return tab
    
    @staticmethod
    def suma(zbior1,zbior2):
        tab = []
        for i in zbior1:
            tab.append(i)
        for i in zbior2:
            if i not in tab:
                tab.append(i)
        tab.sort()
        return tab
    
    @staticmethod
    def roznica(zbior1,zbior2):
        tab = []
        for i in zbior1:
            if i not in zbior2:
                tab.append(i)
        return tab
        
    
