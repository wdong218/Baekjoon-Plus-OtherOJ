import sys
n,k = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
time = 0
dp = [0 for _ in range(n)]

p = [(a[0],a[0])]
for i in range(1,n):
    g = a[i] - a[i-1]
    p.append((a[i],g))
sorted_data = sorted(p, key=lambda x: x[1])
for _ in range(k):
    sorted_data.pop()
count = 0
for i in range(len(sorted_data)):
    count += sorted_data[i][1]
print(count)