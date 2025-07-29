import sys
input = sys.stdin.readline
t = int(input())
dp = [[] for _ in range(15)]
dp[0] = list(range(1,15))
for i in range(14):
    dp[i+1].append(dp[i][0])
    for j in range(1,14):
        dp[i+1].append(dp[i][j]+dp[i+1][j-1])
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])

