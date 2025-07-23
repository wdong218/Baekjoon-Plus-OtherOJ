import sys
input = sys.stdin.readline
a = int(input())
s = input()
result = 0
start = 1
for i in range(a):
    k = ord(s[i])-96
    result += k*(start) % 1234567891
    start *= 31
print(result%1234567891)