class Macierz():
    
    def __init__(self,m,n):
        self.m = m
        self.n = n
    
    def stworzMacierz(self):
        self.macierz = [[0 for a in range(self.m)]for b in range(self.n)]
        return self.macierz
    
    def rand(self):
        import random
        for i in self.macierz:
            for j in range(len(i)):
                i[j]=random.randint(0,9)

    def __add__(self,other):
        pom1 = 0
        pom2 = 0
        for _ in range(len(self.macierz)):
            for _ in range(len(self.macierz[0])):
                self.macierz[pom1][pom2] += other.macierz[pom1][pom2]
                pom2 += 1
            pom1 += 1
        return self.macierz
            
    def print(self):
        for i in self.macierz:
            print(i)
    
macierz = Macierz(3,4)
macierz.stworzMacierz()
Macierz.rand(macierz)
Macierz.print(macierz)

macierz2 = Macierz(3,4)
macierz2.stworzMacierz()
Macierz.rand(macierz2)
Macierz.print(macierz2)
print(macierz+macierz2)