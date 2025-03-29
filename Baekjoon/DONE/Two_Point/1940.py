import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
num.sort()
start = 0
end = n-1
count = 0
while start < end:
    a = num[start] + num[end]
    if a > m:
        end -= 1
    elif a < m:
        start += 1
    else:
        count += 1
        start += 1
        end -= 1
print(count)