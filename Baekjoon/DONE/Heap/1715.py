import sys
import heapq
n = int(sys.stdin.readline())
card = []
for _ in range(n):
    a = int(sys.stdin.readline())
    heapq.heappush(card,a)
result = 0
while 1:
    if len(card) == 1:
        break
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    result += a+b
    heapq.heappush(card,a+b)
print(result)