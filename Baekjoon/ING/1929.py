import math
import sys
def input():
    return sys.stdin.readline()
m,n = map(int,input().split())
result = [i for i in range(n, m+1)]
sosu = [2]
for i in range(2,int(math.sqrt(n))+1):
    p = 0
    for j in range(i+1):
        if i