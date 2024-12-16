import sys
def input():
    return sys.stdin.readline()
l = tuple()
result = list()
memo = []
n,k = map(int,input().split())
for i in range(n):
    a,b = map(int,input().split())
    if a < k:
        l += ((a, b),)
for i in range(n):

print(l)