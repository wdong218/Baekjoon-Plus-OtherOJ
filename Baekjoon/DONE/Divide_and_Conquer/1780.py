import sys
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    graph.append(a)
num_count =[0 for i in range(3)]
def divide(x,y,size):
    global num_count
    if is_ok(x,y,size):
        if graph[x][y] == -1:
            num_count[0] += 1
        elif graph[x][y] == 0:
            num_count[1] += 1
        else:
            num_count[2] += 1
        return
    new_size = size//3
    for i in range(3):
        for j in range(3):
            divide(x + i * new_size, y + j * new_size, new_size)


def is_ok(x,y,size):
    first = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != first:
                return False
    return True

divide(0,0,n)
for i in range(3):
    print(num_count[i])