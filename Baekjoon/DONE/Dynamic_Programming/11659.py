import sys
n,m = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
dp = [0]*(n+1)
dp[1] = num_list[0]
for i in range(2,n+1):
    dp[i] = dp[i-1] + num_list[i-1]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(dp[b]-dp[a-1])
