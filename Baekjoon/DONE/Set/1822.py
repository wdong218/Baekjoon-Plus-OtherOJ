import sys
n_a,n_b = map(int,sys.stdin.readline().split())
a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))
result = list(a-b)
result.sort()
if result:
    print(len(result))
    print(*result)
else:
    print(0)