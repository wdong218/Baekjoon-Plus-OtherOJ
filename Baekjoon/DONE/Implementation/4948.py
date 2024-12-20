import math


def sosu_count(n):
    limit = 2 * n
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i*i,limit+1,i):
                is_prime[j] = False

    # n+1부터 2n까지의 소수 개수 세기
    return sum(is_prime[n + 1:limit + 1])




while 1:
    n = int(input())
    if n == 0:
        break
    print(sosu_count(n))
