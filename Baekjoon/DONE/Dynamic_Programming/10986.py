import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = a[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + a[i]

# prefix[j]는 a[0]부터 a[j-1]까지의 합을 의미 (j=0이면 0)
prefix = [0] + dp
# 각 누적합을 m으로 나눈 나머지의 등장 횟수를 센다.
freq = {}
for x in prefix:
    r = x % m
    freq[r] = freq.get(r, 0) + 1
# 같은 나머지를 가진 누적합 쌍의 개수를 모두 더함.
# 만약 어떤 나머지가 f번 등장하면, 그 중 두 점을 선택하는 방법은 f*(f-1)//2 가지이다.
count = 0
for r in freq:
    f = freq[r]
    count += f * (f - 1) // 2

print(count)
# 1 3 6 7 9
# 0 2 5 6 8
# 0 0 3 4 6
# 0 0 0 1 3
# 0 0 0 0 2
