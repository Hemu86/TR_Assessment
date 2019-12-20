def fibonacci(n):
    i = 0
    a=0
    b=1
    fib=[0]
    while(i<=n-1):
        j = a+b
        a=b
        b=j
        fib.append(j)
        i += 1
    return fib


n = int(input("Enter a number: "))

s = fibonacci(n)
print(s)
