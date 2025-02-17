import heapq
import sys
h = []
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print("0")
    else:
        heapq.heappush(h,a)