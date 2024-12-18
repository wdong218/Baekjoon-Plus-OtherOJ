import math

def is_prime(k):
    count = 0
    if k < 2:
        return 1
    for i in range(2, int(math.sqrt(k)) + 1):  # 2부터 sqrt(k)까지 검사해도 소수를 판별 가능하다는 사실을 알게됨
        if k % i == 0:
            return 1
    return False
n = int(input())
for i in range(n):
    k = int(input())
    while is_prime(k):
        k += 1
    print(k)
