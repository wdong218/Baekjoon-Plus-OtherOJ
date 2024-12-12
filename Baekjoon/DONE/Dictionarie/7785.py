n = int(input())
s = {}
result = list()
for i in range(n):
    a,b = input().split()
    s[a] = b
for key,value in s.items():
    if value == 'enter':
        result.append(key)
for name in sorted(result, reverse=True):
    print(name)