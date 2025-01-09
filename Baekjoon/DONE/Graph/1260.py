import sys
from collections import deque
n,m,v = list(map(int,sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)): # 동시 접근 노드 존재시 작은 노드부터 탐색
    graph[i].sort()

def DFS(graph, start, visited):
    visited.append(start)
    for i in graph[start]: # 연결된 노드 순회
        if i not in visited:
            DFS(graph, i, visited)
    return visited


def BFS(graph, start,visited):
    visited.append(start)
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited


def print_result(result):
    print(" ".join(map(str, result)))

# DFS 결과 출력
dfs_result = DFS(graph, v, [])
print_result(dfs_result)

# BFS 결과 출력
bfs_result = BFS(graph, v, [])
print_result(bfs_result)