from collections import deque
import sys

input = sys.stdin.readline
q = deque()
n = int(input().strip())
for _ in range(n):
    a, *m = input().split()
    if a == "push":
        q.append(m[0])
    elif a == "pop":
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif a == "size":
        print(len(q))
    elif a == "empty":
        if q:
            print("0")
        else:
            print("1")
    elif a == "front":
        if q:
            print(q[0])
        else:
            print("-1")
    elif a == "back":
        if q:
            print(q[-1])
        else:
            print("-1")