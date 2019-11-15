def miesiac(n):
    slownie = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    
    while n >= 1:
        return slownie[n-1]
        n+=1
        
print (miesiac(7))
print (miesiac(9))