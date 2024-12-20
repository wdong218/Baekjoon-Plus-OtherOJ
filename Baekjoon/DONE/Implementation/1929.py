import math
import sys
def input():
    return sys.stdin.readline()
m,n = map(int,input().split())
if m == 1:
    m += 1
result = [i for i in range(m, n+1)]
for i in range(2, int(math.sqrt(n))+1):
    result = [x for x in result if x % i != 0 or x == i]

for i in range(0,len(result)):
    print(result[i])