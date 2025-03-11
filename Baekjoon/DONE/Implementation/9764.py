import sys
t = int(sys.stdin.readline())


n = 2000
# dp 테이블 초기화: (n+1) x (n+1) 크기의 2차원 리스트
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 0을 만드는 경우, 어떤 j값이더라도 경우의 수는 1 (공집합)
for j in range(n + 1):
    dp[0][j] = 1

# 1부터 n까지 채워나가기
for j in range(1, n + 1):  # 사용할 수 있는 최대 숫자
    for i in range(1, n + 1):  # 목표 합
        if i < j:
            # i가 j보다 작으면 j를 사용할 수 없으므로 이전 값만 사용
            dp[i][j] = dp[i][j - 1]
        else:
            # j를 사용하지 않는 경우와 j를 사용하는 경우를 합산
            dp[i][j] = dp[i][j - 1] + dp[i - j][j - 1]


for _ in range(t):
    x = int(sys.stdin.readline())
    print(dp[x][x]%100999)



