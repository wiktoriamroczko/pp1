x = int(input('wprowadź liczbę: '))
if x % 2 == 0 and x >= 0:
    print (f'{x} jest liczbą parzystą i dodatnią')
elif x % 2 == 0 and x < 0:
    print (f'{x} jest liczbą parzystą i ujemną')
elif x % 2 != 0 and x >= 0:
    print (f'{x} jest liczbą nieparzystą i dodatnią')
else :
    print (f'{x} jest liczbą nieparzystą i ujemną')
    