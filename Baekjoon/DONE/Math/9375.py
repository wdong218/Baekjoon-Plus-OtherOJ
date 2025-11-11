import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    dir = {}
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().strip().split())
        if b in dir:
            dir[b] += 1
        else:
            dir[b] = 1
    result = 1
    for key, value in dir.items():
        result *= (value+1)
    print(result-1)