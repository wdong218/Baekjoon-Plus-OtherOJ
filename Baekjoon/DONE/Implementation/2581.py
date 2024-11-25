M = int(input())
N = int(input())
min_s = 0
result = 0
for i in range(M,N+1):
    check = 0
    for j in range(1,i+1):
        if i % j == 0:
            check += 1
    if check == 2:
        result += i
        if min_s == 0:
            min_s = i

if result == 0:
    print(-1)
else:
    print(result)
    print(min_s)