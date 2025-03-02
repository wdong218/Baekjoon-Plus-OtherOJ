import sys
from itertools import combinations
n = int(sys.stdin.readline())
result = []
for i in range(1,11):
    for j in combinations(range(10),i):
        num = ''.join(list(map(str, reversed(j))))
        result.append(int(num))
result.sort()
if n >= len(result):
	print(-1)
else:
	print(result[n])