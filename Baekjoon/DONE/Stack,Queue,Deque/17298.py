import sys

n = int(sys.stdin.readline())
nge = list(map(int,sys.stdin.readline().split()))
result = [-1] * n
stack = []
for i in range(n):
    while stack and nge[stack[-1]] < nge[i]:
        idx = stack.pop()
        result[idx] = nge[i]
    stack.append(i)
print(*result)
