import sys
n = int(sys.stdin.readline())
a = [[1,1],[1,0]]
def identity(n):
    I = [[0] * n for _ in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

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
def mul(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j])%1000000007
    return result
matrix = power(a,n)
for i in range(2):
    for j in range(2):
        matrix[i][j] = matrix[i][j]%1000000007
print(matrix[0][1])