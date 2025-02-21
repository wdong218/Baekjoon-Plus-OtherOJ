import math
n = int(input())
factor = math.factorial(n)
count = 0
for i in range(len(str(factor))):
    if str(factor)[len(str(factor))-i-1] == '0':
        count += 1
    else:
        break
print(count)
