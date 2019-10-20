height = int(input("Podaj wzrost w cm:"))
x = height/100

weight = int(input(("Podaj wagę w kg:")))

bmi = weight/x**2
print (f"wskaźnik BMI: {bmi}")

if bmi >= 18.5 and bmi <= 24.99:
    print ("waga prawidłowa")
elif bmi< 18.5:
    print ("niedowaga")
else:
    print ("nadwaga")
  