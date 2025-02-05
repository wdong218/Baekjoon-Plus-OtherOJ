import sys
s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
dp = [[0] * (len(s) + 1) for _ in range(26)]

for j in range(1, len(s) + 1):
    char_index = ord(s[j - 1]) - ord('a')
    for i in range(26):
        dp[i][j] = dp[i][j - 1]
    dp[char_index][j] += 1

for _ in range(q):
    a, l, r = sys.stdin.readline().split()
    char_index = ord(a) - ord('a')
    l, r = int(l), int(r)
    print(dp[char_index][r + 1] - dp[char_index][l])