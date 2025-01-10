import sys
n = int(input())
a = set(map(int,sys.stdin.readline().split()))
m = int(input())
result = [1] * m
b = list(map(int,sys.stdin.readline().split()))
q = set(b)
temp = q-a
for i in range(len(b)):
    if b[i] in temp:
        result[i] = 0
    print(result[i])
