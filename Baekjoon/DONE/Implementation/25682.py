import sys
n,m,k = map(int,sys.stdin.readline().split())
board = []
for _ in range(n):
    a = sys.stdin.readline().strip()
    # 'B'를 '1', 'W'를 '0'으로 치환한 후 각 문자를 int로 변환
    a = [int(x) for x in a.replace("B", "1").replace("W", "0")]
    board.append(a)
#검정,흰색으로 시작하는 정답 보드 만들기
black_start = [[0 if (i+j) % 2 == 1 else 1 for j in range(m)] for i in range(n)]
white_start = [[1 if (i+j) % 2 == 1 else 0 for j in range(m)] for i in range(n)]
#보드를 각 정답보드와 비교해 누적합을 구해서 최소인 경우 출력
black_prefix = [[0]*(m+1) for _ in range(n+1)]
white_prefix = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if board[i-1][j-1] != black_start[i-1][j-1]:
            black_prefix[i][j] = 1 + black_prefix[i][j-1] + black_prefix[i-1][j] - black_prefix[i-1][j-1]
        else:
            black_prefix[i][j] = black_prefix[i][j - 1] + black_prefix[i - 1][j] - black_prefix[i - 1][j - 1]
        if board[i-1][j-1] != white_start[i-1][j-1]:
            white_prefix[i][j] = 1 + white_prefix[i][j - 1] + white_prefix[i - 1][j] - white_prefix[i - 1][j - 1]
        else:
            white_prefix[i][j] = white_prefix[i][j - 1] + white_prefix[i - 1][j] - white_prefix[i - 1][j - 1]
result = []
for i in range(n-k+1):
    for j in range(m-k+1):
        white = white_prefix[i+k][j+k] - white_prefix[i][j+k] - white_prefix[i+k][j] + white_prefix[i][j]
        black = black_prefix[i + k][j + k] - black_prefix[i][j + k] - black_prefix[i + k][j] + black_prefix[i][j]
        result.append(min(white,black))
print(min(result))
