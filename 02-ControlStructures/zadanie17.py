sp=0
snp=0
for i in range(1, 51):
    if i%2==0:
        sp+=1
    if i%2!=0:
        snp+=1
print (f'Suma liczb parzystych wynosi {sp}, a nieparzystych {snp}')
    