import sys
from collections import deque

result = [0 for _ in range(201)]
for i in range(1,201):
    queue = deque([1])
    while 1:
        curr = queue.popleft()
        curr *= 10
        if curr % i == 0:
            result[i] = curr
            break
        queue.append(curr)
        curr += 1
        if curr % i ==0:
            result[i] = curr
            break
        queue.append(curr)


while 1:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    print(result[a])


