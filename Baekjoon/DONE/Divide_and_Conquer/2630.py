import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이가 깊어질 경우를 대비

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0

def check_uniform(x, y, size):
    first = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != first:
                return False
    return True

def divide(x, y, size):
    global white, blue
    if check_uniform(x, y, size):
        if graph[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    new_size = size // 2  # 4등분이면 한 변의 길이는 전체의 절반
    divide(x, y, new_size)                         # 왼쪽 위
    divide(x, y + new_size, new_size)              # 오른쪽 위
    divide(x + new_size, y, new_size)              # 왼쪽 아래
    divide(x + new_size, y + new_size, new_size)   # 오른쪽 아래

divide(0, 0, n)

print(white)
print(blue)
