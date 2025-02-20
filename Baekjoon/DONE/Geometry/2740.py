import sys
n,m = map(int,sys.stdin.readline().split())
a = []
b = []
for _ in range(n):
    x = list(map(int,sys.stdin.readline().split()))
    a.append(x)
m,k = map(int,sys.stdin.readline().split())
for _ in range(m):
    x = list(map(int,sys.stdin.readline().split()))
    b.append(x)
c = []
for i in range(n):
    row_result = []
    for j in range(k):
        s = 0
        for l in range(m):
            s += a[i][l] * b[l][j]
        row_result.append(s)
    c.append(row_result)

for row in c:
    print(*row)
