# from itertools import combinations
# import math
# from functools import reduce
#
# def gcd_N(arr):
#     gcd = arr[0]
#     for item in arr:
#         gcd = math.gcd(gcd, item)
#     return gcd
#
# def lcm(a, b):
#     return abs(a * b) // math.gcd(a, b)
#
# def lcm_multiple(numbers):
#     return reduce(lcm, numbers)
#
# # 입력 받기
# A, B, K = map(int, input().split())
# q = []
# i = 0
# gcd_result = []
# result = []
#
#
# while True:
#     i += A
#     if i > B:
#         break
#     if math.gcd(i, A) == A and B % i == 0:
#         q.append(i)
#
#
# combs = list(combinations(q, K))
#
#
# for comb in combs:
#     if gcd_N(comb) == A:
#         gcd_result.append(comb)
#
#
#
# for comb in gcd_result:
#     if lcm_multiple(comb) == B:
#         result.append(comb)
#
# if result:
#     print(*result[0])  # 첫 번째 결과 출력
# else:
#     print("-1")


import math
from itertools import combinations
from functools import reduce

# 최소공배수 함수
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

# 입력 받기
A, B, K = map(int, input().split())

# 조건 확인
if B % A != 0:
    print(-1)
else:
    target_lcm = B // A  # 목표 최소공배수를 B / A로 설정
    # A의 배수 중 B/A의 약수 선택
    divisors = [A * i for i in range(1, target_lcm + 1) if target_lcm % i == 0]

    found = False
    # K개의 요소로 구성 가능한 조합에서 조건 만족하는 것 찾기
    for comb in combinations(divisors, K):
        if lcm_multiple(comb) == B:
            print(*comb)
            found = True
            break

    if not found:
        print(-1)