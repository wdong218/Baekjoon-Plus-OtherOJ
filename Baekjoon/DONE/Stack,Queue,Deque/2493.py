import sys
input = sys.stdin.readline
n = int(input())
top = list(map(int,input().split()))
stack =[]
result = [0 for _ in range(n)]
for i in range(n):
    t = top[i]
    while stack and top[stack[-1]] < t:
        stack.pop()
    if stack:
        result[i] = stack[-1] +1
    stack.append(i)
print(*result)
