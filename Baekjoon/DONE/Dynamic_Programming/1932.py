import sys
n = int(input())
tri = []
for _ in range(n):
    k = list(map(int,sys.stdin.readline().split()))
    tri.append(k)
for i in range(n-1,0,-1):
    for j in range(len(tri[i])-1):
        tri[i-1][j] += max(tri[i][j],tri[i][j+1])
print(tri[0][0])
