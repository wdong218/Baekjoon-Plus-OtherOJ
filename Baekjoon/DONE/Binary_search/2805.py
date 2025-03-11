import sys
n,m = map(int,sys.stdin.readline().split())
tree_h = list(map(int,sys.stdin.readline().split()))
s = 1
e = max(tree_h)
result = 0
while s <= e:
    mid = (s+e)//2
    total = 0
    for i in tree_h:
        if i > mid:
            total += i - mid
    if total < m:
        e = mid-1
    else:
        result = mid
        s = mid + 1
print(result)

