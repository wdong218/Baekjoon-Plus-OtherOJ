import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
dp[1] = 1
for i in range(2,n+1):
    if i % 2 == 0:
        dp[i] = (dp[i-1] + dp[i//2])%1000000000
    else:
        dp[i] = dp[i-1] % 1000000000
print(dp[-1])