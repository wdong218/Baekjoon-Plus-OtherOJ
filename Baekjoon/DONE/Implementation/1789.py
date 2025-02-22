import sys
n = int(sys.stdin.readline())
if n == 1:
    print("1")
    exit(0)
count = 0
i = 1
while 1:
    if n > i:
        n -= i
        count += 1
        i += 1
    elif n == i:
        count += 1
        break
    else:
        break
print(count)