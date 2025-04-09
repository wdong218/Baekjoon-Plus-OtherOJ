import sys
n,m = map(int,sys.stdin.readline().split())
n_num = list(map(int,sys.stdin.readline().split()))
m_num = list(map(int,sys.stdin.readline().split()))

result = []
for i in range(n):
    result.append(n_num[i])
for i in range(m):
    result.append(m_num[i])
result.sort()
print(*result)
