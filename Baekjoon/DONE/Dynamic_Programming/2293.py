import sys
n,k = map(int,sys.stdin.readline().split())
coin = []
dp = [0 for _ in range(k+1)]
for _ in range(n):
    a = int(sys.stdin.readline())
    coin.append(a)
coin.sort()
dp[0] = 1
for i in coin:
    for j in range(i,k+1):
        dp[j] = dp[j] + dp[j-i]
print(dp[-1])


