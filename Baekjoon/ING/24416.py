n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def dp_fib(n):
    f = list(range(n))
    f[0] = 1
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1]+f[i-2]
    return f[n-1]
print(dp_fib(n),n-2)