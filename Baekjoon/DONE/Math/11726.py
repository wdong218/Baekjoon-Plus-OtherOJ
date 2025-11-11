import math
import sys
n = int(sys.stdin.readline().strip())
result = 0
for i in range(n // 2 + 1):
    result += (math.factorial(n-i) // (math.factorial(i) * math.factorial(n-2 * i))) % 10007
print(result%10007)
