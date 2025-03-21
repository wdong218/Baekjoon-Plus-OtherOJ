import sys
import math
k = int(sys.stdin.readline())

a = int(math.sqrt(k))
num = 0
num_list = []
i = 2
while a >= i:
    if k % i == 0:
        k = k//i
        num += 1
        num_list.append(i)
    else:
        i += 1
if k != 1:
    num_list.append(k)
    num_list.sort()
    print(num+1)
    print(*num_list)
else:
    num_list.sort()
    print(num)
    print(*num_list)
