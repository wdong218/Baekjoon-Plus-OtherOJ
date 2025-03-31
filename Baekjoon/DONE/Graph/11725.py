import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
q = deque()
q.append(1)
visited[1] = True
while q:
    v = q.popleft()
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            result[i] = v

for j in range(2,n+1):
    print(result[j])