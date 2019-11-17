def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

f=0
for i in range(20):
    print(fibo(f), end=' ')
    f+=1