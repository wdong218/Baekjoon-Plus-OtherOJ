
array = [[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)]
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if array[a][b][c] != -1:
        return array[a][b][c]

    if a > 20 or b > 20 or c > 20:
        array[20][20][20] = w(20, 20, 20)
        return array[20][20][20]

    if a < b and b < c:
        array[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return array[a][b][c]
    array[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return array[a][b][c]

while 1:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    q = f"w({a}, {b}, {c}) ="
    print(q, w(a, b, c))