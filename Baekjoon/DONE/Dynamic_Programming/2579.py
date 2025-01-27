import sys

input = sys.stdin.readline
n = int(input())
stairs = []
for i in range(n):
    a = int(input())
    stairs.append(a)
if n == 1:
    print(stairs[0])
elif n == 2:
    print(sum(stairs))
else:
    dp = list(0 for _ in range(n))
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for i in range(3,n):
        dp[i] = max(stairs[i-1]+dp[i-3]+stairs[i],dp[i-2]+stairs[i])

    print(dp[n-1])