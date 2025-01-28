import heapq
import sys
k = []
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(k) != 0:
            print(-heapq.heappop(k))
        else:
            print("0")
    else:
        heapq.heappush(k,-a)
