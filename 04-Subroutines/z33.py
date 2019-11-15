def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a

n = 0
for i in range(20):
    print (fib(n))
    n+=1