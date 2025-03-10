import sys
k,n = map(int,sys.stdin.readline().split())
result = []
for i in range(k):
    a = int(sys.stdin.readline())
    result.append(a)
s = 1
e = max(result)

while s <= e:
    mid = (s+e)//2
    lan = 0
    for i in result:
        lan += i//mid
    if lan >= n:
        s = mid + 1
    else:
        e = mid - 1
print(e)