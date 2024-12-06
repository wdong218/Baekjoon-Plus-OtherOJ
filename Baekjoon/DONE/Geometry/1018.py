N, M = map(int, input().split())

# 체스판 패턴 생성 함수
def create_pattern(N, M):
    W_start = []
    B_start = []
    for i in range(N):  # 행 기준으로 패턴 생성
        if i % 2 == 0:
            W_start.append("WB" * (M // 2) + ("W" if M % 2 else ""))
            B_start.append("BW" * (M // 2) + ("B" if M % 2 else ""))
        else:
            W_start.append("BW" * (M // 2) + ("B" if M % 2 else ""))
            B_start.append("WB" * (M // 2) + ("W" if M % 2 else ""))
    return W_start, B_start

# 패턴 생성
W_start_pos, B_start_pos = create_pattern(N, M)

# 체스판 입력 받기
board = [input() for _ in range(N)]

# 최솟값 계산
min_changes = float('inf')

for i in range(N - 8 + 1):  # 가능한 시작 행
    for j in range(M - 8 + 1):  # 가능한 시작 열
        w_count, b_count = 0, 0
        for x in range(8):
            for y in range(8):
                # 현재 8x8 보드에서 (x, y) 위치의 문자
                current = board[i + x][j + y]
                if current != W_start_pos[i + x][j + y]:  # 패턴 1과 비교
                    w_count += 1
                if current != B_start_pos[i + x][j + y]:  # 패턴 2와 비교
                    b_count += 1
        # 두 패턴 중 최소 변경 횟수를 기록
        min_changes = min(min_changes, w_count, b_count)

print(min_changes)