import sys
n = int(sys.stdin.readline())
a = []
b = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    a.append([x,y,1])
result = []
for i in range(n):
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            a[i][2] += 1
    result.append(a[i][2])
print(*result)
