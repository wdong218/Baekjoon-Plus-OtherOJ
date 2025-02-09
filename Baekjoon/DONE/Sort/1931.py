import sys
n = int(sys.stdin.readline())
k = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    k.append((b,a))
count = 0
current_end = -float('inf')
k.sort()
for i in range(n):
    if k[i][1] >= current_end:
        current_end = k[i][0]
        count += 1
print(count)