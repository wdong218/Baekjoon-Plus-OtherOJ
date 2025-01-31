n = int(input())
grape = []
for _ in range(n):
    a = int(input())
    grape.append(a)
if n == 1:
    print(grape[0])
elif n == 2:
    print(sum(grape))
elif n == 3:
    print(max(grape[0]+grape[1],grape[0]+grape[2]))
else:
    dp = [0] * n
    dp[0] = grape[0]
    dp[1] = grape[1] + grape[0]
    dp[2] = max(grape[0]+grape[2],grape[1]+grape[2],dp[1])
    for i in range(3,n):
        dp[i] = max(dp[i-2]+grape[i],grape[i]+grape[i-1]+dp[i-3],dp[i-1]) # 핵심 팁 !! 자기 자신을 제외하는 경우도 포함해야됨 !!
    print(dp[n-1])