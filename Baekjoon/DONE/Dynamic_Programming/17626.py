import sys
import math
n = int(sys.stdin.readline().strip())
dp = [10 for _ in range(n+4)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n+1):
    if  math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
    else:
        for j in range(1,int(math.sqrt(i))+1):
            dp[i] = min(dp[i],dp[i-j*j] + dp[j*j])
print(dp[n])
# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 1
# 5 4+1,3+2 = 2 (4,1)
# 6 5+1,4+2 3+3 = 3 (5,1), (4,2)
# 7 6+1 5+2 4+3 = 4 (5,2)(6,1)
# 8 71,62,53,44 = 2
# 9             = 1
# 10 19 28 37 46 55 = 2
# 11 110 29 38 47 56 = 3
# 12 - 2
# 13 - 3