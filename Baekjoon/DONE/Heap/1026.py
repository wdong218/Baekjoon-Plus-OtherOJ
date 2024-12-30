import heapq
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
heapq.heapify(b)
a.sort(reverse=True)
result = 0
for i in range(n):
    result += a[i]*heapq.heappop(b)
print(result)
