import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]  # 0부터 n까지 사용
for _ in range(m):
    u, v, w = map(int, input().split())
    if u == v:
        continue
    arr[u][v] = max(arr[u][v], w)

ans = -1
visited = [False] * (n + 1)

def dfs(state, dis, cnt):
    global ans
    if cnt == n:
        if arr[state][0] > 0:
            ans = max(ans, dis + arr[state][0])
        return
    for i in range(1, n + 1):
        if not visited[i] and arr[state][i] > 0:
            visited[i] = True
            dfs(i, dis + arr[state][i], cnt + 1)
            visited[i] = False

dfs(0, 0, 0)
print(ans)
