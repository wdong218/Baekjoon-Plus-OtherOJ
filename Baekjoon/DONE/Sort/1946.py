import sys
def input():
    return sys.stdin.readline().strip()
t = int(input())
for i in range(t):
    result = []
    count = 1
    n = int(input())
    for j in range(n):
        a,b = map(int,input().split())
        result.append((a,b,))
    result.sort()
    min_value = result[0][1]
    for l in range(1, n):
        if result[l][1] < min_value:
            count += 1
            min_value = result[l][1]
    print(count)