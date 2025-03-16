import sys
n = list(sys.stdin.readline().strip())
boom = list(sys.stdin.readline().strip())
result = []
a = len(boom)
for i in n:
    result.append(i)
    if result[len(result)-a:] == boom:
        for _ in range(a):
            result.pop()
if result:
    print(''.join(result))
else:
    print("FRULA")

