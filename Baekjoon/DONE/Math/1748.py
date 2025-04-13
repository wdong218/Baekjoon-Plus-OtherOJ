import sys
n = sys.stdin.readline().strip()
k = len(n)
result = 0

for i in range(1, k):
    result += 9 * (10 ** (i - 1)) * i

q = int(n) - (10 ** (k - 1)) + 1
q *= k

print(result + q)
