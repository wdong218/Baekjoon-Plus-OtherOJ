import sys
n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().split()))
dp = [1] * n
for i in range(1,n):
    for j in range(0,i):
        if k[i] > k[j]:
            dp[i] = max(dp[i], dp[j] + 1)
dp_dec = [1] * n
for i in range(n - 2, -1, -1):  # n-2부터 0까지
    for j in range(i + 1, n):
        if k[i] > k[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
real_dp =[0] * n
for i in range(n):
    real_dp[i] = dp_dec[i] + dp[i] - 1
print(max(real_dp))