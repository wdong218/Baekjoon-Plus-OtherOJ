import sys

a,b = map(int, sys.stdin.readline().split())
k = 10**b
a = str(a)
if int(a) < k:
    if int(a) >= k//2:
        print(k)
        exit(0)
    else:
        print("0")
        exit(0)
if int(a[-b]) >= 5:
    print(int(a)+k-(int(a)%k))
else:
    print(int(a)-(int(a)%k))

