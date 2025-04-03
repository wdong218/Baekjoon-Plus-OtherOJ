import sys
import math
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    num = int(input())
    s = 0.0
    for i in range(num,1,-1):
        s += math.log10(i)

    print(int(s)+1)