# import numpy as np
# N,M = map(int,input().split())
# A = np.zeros((N, M),dtype=int)
# B = np.zeros((N, M),dtype=int)
# result = np.zeros((N, M),dtype=int)
# for i in range(N):
#     elements = list(map(int,input().split()))
#     A[i] = elements
#
# for i in range(N):
#     elements = list(map(int,input().split()))
#     B[i] = elements
#
# result = A+B
#
#
# for i in result:
#     print(*i)

#numpy를 사용한 코드 백준에선 지원을 안함

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    elements = list(map(int, input().split()))
    A.append(elements)

for i in range(N):
    elements = list(map(int, input().split()))
    B.append(elements)

result = [[0] * M for _ in range(N)]


for i in range(N):
    for j in range(M):
        result[i][j] = A[i][j] + B[i][j]


for row in result:
    print(*row)