from collections import deque
import sys
n = int(input())
dq = list(map(int, sys.stdin.readline().split()))
dq = deque(dq)
num_dq = deque(range(1,n+1))
result = list()
for _ in range(n):
    temp = dq.popleft()
    if temp < 0:
        dq.rotate(-temp)
        result.append(num_dq.popleft())
        num_dq.rotate(-temp)
    else:
        dq.rotate(-temp+1)
        result.append(num_dq.popleft())
        num_dq.rotate(-temp+1)
print(" ".join(map(str, result)))