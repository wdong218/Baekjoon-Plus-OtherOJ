import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    k = [0] + list(map(int,sys.stdin.readline().split()))
    pri = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        pri[i] = pri[i-1] + k[i-1]
    dp = [[0 for i in range(n+1)] for j in range(n+1)]



