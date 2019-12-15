class arrays():
    
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def with_comma(array):
        for c in array:
            if c == array[-1]:
                print(c)
            else:
                print(c, end=', ')
                
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