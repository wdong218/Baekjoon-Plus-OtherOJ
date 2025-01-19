from collections import deque

n = int(input())
bord = [[0]*(n+2) for _ in range(n+2)]  # 0..(n+1)

for i in range(n+2):  # 0..(n+1)
    bord[0][i] = 1      # 위쪽 벽
    bord[n+1][i] = 1    # 아래쪽 벽
    bord[i][0] = 1      # 왼쪽 벽
    bord[i][n+1] = 1    # 오른쪽 벽

k = int(input())  # 사과의 개수
for _ in range(k):
    a,b = map(int, input().split())  # 사과 위치
    bord[a][b] = 2  # 사과 표시

l = int(input())  # 뱀의 방향 변환 횟수
rotate_info = []
for _ in range(l):
    x,c = input().split()
    rotate_info.append((int(x), c))

time = 0
start_x, start_y = 1, 1
bord[start_y][start_x] = 3  # 뱀 머리(혹은 몸)를 보드에서 3으로 표현
snake = deque([(start_y, start_x)])  # 뱀의 좌표를 (y,x)로 저장

# 방향 정보: 우(0) / 하(1) / 좌(2) / 상(3)
directions = [(0,1), (1,0), (0,-1), (-1,0)]
current_dir = 0  # 초기 방향(오른쪽)
i = 0  # rotate_info 인덱스

while True:
    time += 1  # 초 증가
    dy, dx = directions[current_dir]
    next_y = start_y + dy
    next_x = start_x + dx

    # 1) 범위 벗어나면(벽 밖으로 나가면) 종료
    if not (0 <= next_y <= n and 0 <= next_x <= n):
        break
    # 2) '벽(1)' 또는 '뱀 몸통'과 충돌 체크
    if bord[next_y][next_x] == 1 or (next_y, next_x) in snake:
        break

    # 3) 사과 여부에 따라 꼬리 처리
    if bord[next_y][next_x] == 2:
        # 사과가 있으면 사과만 없애고, 꼬리는 그대로
        bord[next_y][next_x] = 3
        snake.appendleft((next_y, next_x))
    else:
        # 사과가 없으면 꼬리 제거 후, 머리 이동
        tail_y, tail_x = snake.pop()
        bord[tail_y][tail_x] = 0
        bord[next_y][next_x] = 3
        snake.appendleft((next_y, next_x))

    # 4) 시간이 맞으면 방향 전환
    if i < len(rotate_info) and rotate_info[i][0] == time:
        turn = rotate_info[i][1]
        if turn == 'L':
            current_dir = (current_dir - 1) % 4
        else:  # 'D'
            current_dir = (current_dir + 1) % 4
        i += 1

    # 5) 머리 위치 갱신
    start_y, start_x = next_y, next_x

print(time)
