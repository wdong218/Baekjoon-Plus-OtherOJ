import heapq
import sys
n = int(sys.stdin.readline())
plus_heap = []
minus_heap = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if minus_heap == [] and plus_heap == []:
            print("0")
        elif minus_heap == [] and plus_heap != []:
            print(heapq.heappop(plus_heap))
        elif minus_heap != [] and plus_heap == []:
            print(-heapq.heappop(minus_heap))
        elif minus_heap[0] > plus_heap[0]:
            print(heapq.heappop(plus_heap))
        elif minus_heap[0] < plus_heap[0]:
            print(-heapq.heappop(minus_heap))
        elif minus_heap[0] == plus_heap[0]:
            print(-heapq.heappop(minus_heap))

    elif a < 0:
        heapq.heappush(minus_heap,-a)
    elif a > 0:
        heapq.heappush(plus_heap,a)

