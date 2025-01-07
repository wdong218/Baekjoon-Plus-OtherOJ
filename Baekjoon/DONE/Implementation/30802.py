import sys
n = int(input())
size = list(map(int,input().split()))
t,p = map(int,input().split())
result = 0
for i in range(len(size)):
    if size[i] % t == 0:
        result += size[i] // t
    else:
        result += (size[i] // t) + 1
print(result)
pen_result = []
pen_result.append(n//p)
pen_result.append(n % p)
for i in range(len(pen_result)):
    print(pen_result[i], end=" ")