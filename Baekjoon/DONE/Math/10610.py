import sys
n = list(map(int,sys.stdin.readline().strip()))
n.sort(reverse=True)
if n[-1] == 0 and sum(n)%3 == 0:
    print("".join(map(str, n)))
else:
    print(-1)