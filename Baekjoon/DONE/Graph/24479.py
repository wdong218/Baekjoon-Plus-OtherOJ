import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
order = [0]*(n+1)
cnt = 1
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(len(graph)): # 동시 접근 노드 존재시 작은 노드부터 탐색
    graph[i].sort()
def dfs(x):
    global cnt
    visited[x] = True
    order[x] = cnt
    cnt += 1
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

dfs(r)
for i in range(1, n+1):
    print(order[i])