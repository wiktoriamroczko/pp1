class statystyka():
    
    def __init__(self):
        self.tab = []
        self.m = None
        self.n = None
        self.sr = None
        self.med = None
        
    def tab_add(self, x):
        tab = self.tab
        tab.append(x)
        
    def najwieksza(self):
        self.m = max(self.tab)
        
    def najmniejsza(self):
        self.n = min(self.tab)
        
    def srednia(self):
        import statistics
        self.sr = statistics.mean(self.tab)
        
    def mediana(self):
        import statistics
        tab = self.tab
        tab.sort()
        self.med = statistics.median_grouped(tab)
        
    def show_tab(self):
        for i in self.tab:
            print(i, end=' ')
        print('')
    
    def show_value(self):
        if self.m is not None:
            print(f'Wartość największa: {self.m}')
        if self.n is not None:
            print(f'Wartość najmniejsza: {self.n}')
        if self.sr is not None:
            print(f'Średnia arytmetyczna: {self.sr}')
        if self.med is not None:
            print(f'Mediana: {self.med}')
        
nums = statystyka()
nums.tab_add(12)
nums.tab_add(37)
nums.tab_add(6)
nums.tab_add(9)
nums.tab_add(17)
nums.show_tab()
nums.mediana()
nums.srednia()
nums.najmniejsza()
nums.najwieksza()
nums.show_value()