import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    k = list(map(int,sys.stdin.readline().split()))
    pri = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        pri[i] = pri[i-1] + k[i-1]
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for length in range(2,n+1):
        for i in range(1,n-length+2):
            j = i+length-1
            dp[i][j] = float('inf')
            a = pri[j]-pri[i-1]
            for m in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][m]+dp[m+1][j]+a)



    print(dp[1][-1])





