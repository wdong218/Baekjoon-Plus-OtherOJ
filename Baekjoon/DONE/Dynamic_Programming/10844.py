n = int(input())
a = [[0] * 10 for _ in range(n)]
a[0] = [0,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    for j in range(10):
        if j == 0:
            a[i][j] += a[i-1][j+1]
        elif j == 9:
            a[i][j] += a[i-1][j-1]
        else:
            a[i][j] += a[i-1][j-1] + a[i-1][j+1]
print(sum(a[n-1])%1000000000)