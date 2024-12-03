from itertools import combinations
N,M = map(int,input().split())
k = list(map(int, input().split()))
k_combinations = list(combinations(k,3))
result = list()
for i in range(len(k_combinations)):
    l = 0
    for j in range(3):
        l += k_combinations[i][j]
    result.append(l)
real_result = [x for x in result if x <= M]
print(max(real_result))