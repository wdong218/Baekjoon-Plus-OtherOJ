from itertools import permutations
import sys
# 입력 처리
n = int(sys.stdin.readline().strip())  # 배열 길이
k = list(map(int, sys.stdin.readline().strip().split()))  # 배열
add, sub, mul, div = map(int, sys.stdin.readline().strip().split())  # 연산자 개수
cul_list = "+" * add + "-" * sub + "*" * mul + "/" * div
# 모든 순열 생성
perm = list(permutations(cul_list, len(cul_list)))  # 순열을 리스트로 변환
result = []
for i in range(len(perm)):
    temp = k[0]
    for j in range(len(perm[i])):
        if perm[i][j] == "+":
            temp += k[j+1]
        elif perm[i][j] == "-":
            temp -= k[j+1]
        elif perm[i][j] == "*":
            temp *= k[j+1]
        elif perm[i][j] == "/":
            if temp < 0:
                o = -temp
                g = o // k[j+1]
                temp = -g
            else:
                temp //= k[j+1]
    result.append(temp)

print(max(result))
print(min(result))

