class arrays():
    
    x = ','
         
    @staticmethod
    def set_sep(z):
        arrays.x = z
    
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def with_comma(array):
        p = 0
        for c in array:
            if p == len(array)-1:
                print(c)
            else:
                print(c, end=f'{arrays.x}')
                p+=1
                
                
    @staticmethod
    def arr1(liczba_elementow_tablicy,wartosc_elementow_tablicy):
        array = []
        for _ in range(liczba_elementow_tablicy):
            array.append(wartosc_elementow_tablicy)
        return array
    
    @staticmethod
    def arr2(liczba_elementow_tablicy,wartosc_od,wartosc_do):
        import random
        array = []
        for _ in range(liczba_elementow_tablicy):
            array.append(random.randint(wartosc_od,wartosc_do))
        return array
    
    @staticmethod
    def szukaj(tablica,wartość_od,wartość_do):
        array = []
        for i in tablica:
            if i >= wartość_od and i <= wartość_do:
                array.append(i)
        return array