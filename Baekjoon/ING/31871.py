import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {}
for _ in range(m):
    u, v, w = map(int, input().split())
    if u not in graph:
        graph[u] = {}
    if v not in graph[u] or w > graph[u][v]: #최대 가중치만 남기기
        graph[u][v] = w

time = -1
def DFS(graph, start, visited):
    visited.append(start)
    for i in graph[start]: # 연결된 노드 순회
        if i not in visited:
            DFS(graph, i, visited)
    return visited

