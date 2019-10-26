suma=0
tab=(15,8,31,47,2,19)
n=0
for i in tab:
    if i%2!=0:
      suma+=i
      n+=1
print(f"Średnia arytmetyczna wynosi {suma/n}")