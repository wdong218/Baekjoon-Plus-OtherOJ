import sys
import heapq
n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    for num in a:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

print(heap[0])
