import sys
input = sys.stdin.readline
temp = set()
result = list()
n,m = map(int,input().split())
for i in range(n+m):
    k = input().strip()
    if k in temp:
        result.append(k)
    else:
        temp.add(k)
result = sorted(result)
print(len(result))
for i in range(len(result)):
    print(result[i])