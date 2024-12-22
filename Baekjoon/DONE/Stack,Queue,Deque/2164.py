from collections import deque
n = int(input())
range_list = list(range(1, n+1))
queue = deque(range_list)
while len(queue) != 1:

    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)
print(queue.popleft())