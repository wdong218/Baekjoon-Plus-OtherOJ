
from collections import deque
import sys
def input():
    return sys.stdin.readline().strip()
deque = deque()
n = int(input())
for _ in range(n):
    a,*m = input().split()
    if a == "push":
        deque.append(m[0])
    elif a == "pop":
        if deque:
            print(deque.popleft())
        else:
            print("-1")
    elif a == "size":
        print(len(deque))
    elif a == "empty":
        if deque:
            print("0")
        else:
            print("1")
    elif a == "front":
        if deque:
            print(deque[0])
        else:
            print("-1")
    elif a == "back":
        if deque:
            print(deque[-1])
        else:
            print("-1")