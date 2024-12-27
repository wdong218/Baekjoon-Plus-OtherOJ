from collections import deque
n = int(input())
a = list(map(int, input().strip().split()))
b = deque(map(int, input().strip().split()))
queues = deque()
for i in range(n):
    if a[i] == 0:
        queues.append(b.popleft())
    else:
        b.popleft()
m = int(input())
c = deque(map(int, input().strip().split()))
result = []
for i in range(m):
    if queues:
        result.append(queues.pop())
    else:
        result.append(c.popleft())


print(" ".join(map(str, result)))