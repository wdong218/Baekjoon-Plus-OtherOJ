import sys
n = int(input())
a = set(map(int,sys.stdin.readline().split()))
m = int(input())
b = set(map(int,sys.stdin.readline().split()))
print(b-a)