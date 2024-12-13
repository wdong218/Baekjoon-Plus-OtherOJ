import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = set()
b = set()
a.update(input().split())
b.update(input().split())
print(len(a-b)+len(b-a))