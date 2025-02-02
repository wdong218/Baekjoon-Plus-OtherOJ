import sys
n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().split()))
dp = [1] * n
for i in range(1,n):
    for j in range(0,i):
        if k[i] > k[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))