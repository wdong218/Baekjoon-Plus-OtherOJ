import sys
n,b = map(int,sys.stdin.readline().split())
matrix = []
c = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    matrix.append(a)
    c.append(a)

def power(a,b):
    if b == 0:
        return identity(len(a))
    if b == 1:
        return a
    x = power(a,b//2)
    x = mul(x,x)
    if b % 2 == 1:
        x = mul(x,a)
    return x
#항등 행렬
def identity(n):
    I = [[0] * n for _ in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I
#행렬 곱
def mul(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % 1000
    return result
matrix = power(matrix,b)
for i in range(n):
    for j in range(n):
        matrix[i][j] = matrix[i][j]%1000
for i in range(n):
    print(*matrix[i])