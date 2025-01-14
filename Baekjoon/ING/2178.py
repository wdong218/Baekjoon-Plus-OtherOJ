import sys
n,m = map(int,input().split())
mage = [[] for _ in range(n)]
for i in range(n):
    k = sys.stdin.readline().strip()
    mage[i] = k
print(mage)
visited = []
count = 0
def dfs(x,y):
    while 1:
        if x == n and y == m:
            return count
        if mage[y][x] == 1 and (x,y) not in visited :
            visited.append((x+1,y))
        else:
            dfs(x,y+1)

dfs(0,0)