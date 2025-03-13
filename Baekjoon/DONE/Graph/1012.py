import sys
input = sys.stdin.readline
t = int(input())
def check_1(i,j,matrix):
    if matrix[i][j+1] == 1:
        matrix[i][j+1] = 0
        check_1(i,j+1,matrix)
    if matrix[i][j-1]:
        matrix[i][j - 1] = 0
        check_1(i, j - 1, matrix)
    if matrix[i-1][j]:
        matrix[i-1][j] = 0
        check_1(i-1, j, matrix)
    if matrix[i+1][j]:
        matrix[i+1][j] = 0
        check_1(i+1, j, matrix)

    return matrix
for _ in range(t):
    m,n,k = map(int,input().split())
    matrix = [[0 for i in range(m+2)] for j in range(n+2)]
    count = 0
    for _ in range(k):
        x,y = map(int,input().split())
        matrix[y+1][x+1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                count += 1
                check_1(i,j,matrix)
    print(count)




