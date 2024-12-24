import sys
from collections import deque
def input():
    return sys.stdin.readline()
dq = deque()
n = int(input())
for _ in range(n):
    a, *rest = map(int, input().split())
    if a == 1:
        b = rest[0]
        dq.appendleft(b)
    elif a == 2:
        b = rest[0]
        dq.append(b)
    elif a == 3:
        if dq:
            print(dq.popleft())
        else:
            print("-1")
    elif a == 4:
        if dq:
            print(dq.pop())
        else:
            print("-1")
    elif a == 5:
        print(len(dq))
    elif a == 6:
        if dq:
            print("0")
        else:
            print("1")
    elif a == 7:
        if dq:
            print(dq[0])
        else:
            print("-1")
    elif a == 8:
        if dq:
            print(dq[-1])
        else:
            print("-1")