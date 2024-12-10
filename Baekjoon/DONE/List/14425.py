n,m = map(int,input().split())
s = list()
count = 0
for i in range(n):
    s.append(input())
for i in range(m):
    w = input()
    if w in s:
        count += 1
print(count)