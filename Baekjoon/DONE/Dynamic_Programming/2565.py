import sys
n = int(sys.stdin.readline())
ele = []
dp = [1]*n
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    ele.append([a,b])
ele.sort()
for i in range(1,n):
    for j in range(i):
        if ele[j][1] < ele[i][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))