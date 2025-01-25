def dp(n):
    f = [0 for _ in range(100)]
    f[0] = 1
    f[1] = 1
    f[2] = 1
    f[3] = 2
    for i in range(4,n):
        f[i] = f[i-3] + f[i-2]
    return f[n-1]


t = int(input())
for _ in range(t):
    n = int(input())
    print(dp(n))