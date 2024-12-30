import sys
read  = sys.stdin.readline
n,m = map(int,read().split())
result = {}
for i in range(n):
    a = read().rstrip()
    if len(a) >= m:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1

result = sorted(result.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for key, value in result:
    print(key)