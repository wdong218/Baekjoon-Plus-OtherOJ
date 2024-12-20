import math
import sys
def input():
    return sys.stdin.readline()
def sosu_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님\

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime
def Goldbach(k,is_prime):
    count = 0
    for i in range(2,k//2+1):
        part_value = k-i
        if is_prime[i] == True and is_prime[part_value] == True:
            count += 1
    return count

q = int(input())
d = list()
for _ in range(q):
    n = int(input())
    d.append(n)
is_prime = sosu_list(max(d))
for i in range(q):
    print(Goldbach(d[i], is_prime))