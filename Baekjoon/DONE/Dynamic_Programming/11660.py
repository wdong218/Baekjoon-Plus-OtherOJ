import sys
n,m = map(int,sys.stdin.readline().split())
graph = []
dp = [[0] *(n+1) for _ in range(n+1)]
for _ in range(n):
    k = list(map(int,sys.stdin.readline().split()))
    graph.append(k)
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + graph[i-1][j-1]
for i in range(m):
    x_1,y_1,x_2,y_2 = map(int,sys.stdin.readline().split())
    result = dp[x_2][y_2] -dp[x_2][y_1-1] - dp[x_1-1][y_2] + dp[x_1-1][y_1-1]
    print(result)
