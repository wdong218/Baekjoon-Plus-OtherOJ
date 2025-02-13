import sys
n = int(sys.stdin.readline())
graph = []

result = ""
for _ in range(n):
    a = list(map(int, sys.stdin.readline().strip()))
    graph.append(a)

def check_uniform(x, y, size):
    first = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != first:
                return False
    return True
def divide(x, y, size):
    global result
    if check_uniform(x, y, size):
        if graph[x][y] == 0:
            result += '0'
        else:
            result += '1'
        return
    result += "("
    new_size = size // 2  # 4등분이면 한 변의 길이는 전체의 절반
    divide(x, y, new_size)  # 왼쪽 위
    divide(x, y + new_size, new_size)              # 오른쪽 위
    divide(x + new_size, y, new_size)              # 왼쪽 아래
    divide(x + new_size, y + new_size, new_size)   # 오른쪽 아래
    result += ")"

divide(0, 0, n)
print(result)