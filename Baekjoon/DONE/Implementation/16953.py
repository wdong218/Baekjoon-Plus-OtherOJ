import sys
a,b = map(int,sys.stdin.readline().split())
count = 0
while 1:
    if b < a:
        count = -1
        print(count)
        break
    if a == b:
        print(count + 1)
        break
    if b % 2 == 0:
        b = b//2
        count += 1
    else:
        k = str(b)
        if int(k[-1]) != 1:
            count = -1
            print(count)
            break
        else:
            b = b//10
            count += 1
