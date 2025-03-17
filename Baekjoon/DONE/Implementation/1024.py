import sys

n,l = map(int,sys.stdin.readline().split())
start = (n-(l*(l-1))//2)//l
while 1:
    if l > 100:
        print("-1")
        exit(0)
    if (n-(l*(l-1))//2) % l == 0:
        start = (n-(l*(l-1))//2)//l
        break
    else:
        l += 1
if start < 0:
    print("-1")
    exit(0)
for i in range(l):
    print(start+i,end=" ")