def sumaCyfr(n):
    if n<10:
        return n
    else:
        return n%10 + sumaCyfr(n//10)

print(sumaCyfr(5433))