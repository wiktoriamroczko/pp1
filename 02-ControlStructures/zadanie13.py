x = int(input('1. współtrzędna: '))
y = int(input('2. współtrzędna: '))

if x < 0 and y < 0:
    print (f'punkt P({x}, {y}) znajduje się w 3. ćwiartce układu współrzędnych')
elif x < 0 and y > 0:
    print (f'punkt P({x}, {y}) znajduje się w 2. ćwiartce układu współrzędnych')
elif x > 0 and y > 0:
    print (f'punkt P({x}, {y}) znajduje się w 1. ćwiartce układu współrzędnych')
elif x > 0 and y < 0:
    print (f'punkt P({x}, {y}) znajduje się w 4. ćwiartce układu współrzędnych')
elif x == 0 and y != 0:
    print (f'punkt P({x}, {y}) znajduje się na osi X')
elif x != 0 and y == 0:
    print (f'punkt P({x}, {y}) znajduje się na osi Y')
else:
    print (f'punkt P({x}, {y}) znajduje się na początku układu współrzędnych')
    