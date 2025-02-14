import sys
import heapq
n,k = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
arr = num_list[k:]
for i in range(k):
    heapq.heappush(arr, num_list[i])
print(*arr)