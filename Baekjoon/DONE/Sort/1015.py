import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a_sort = sorted(a)
result = []
for i in range(n):
    k = a_sort.index(a[i])
    # 문제의 조건이 자연수이기 때문에 -1로 변환 시켜 중복되는 수를 카운트 하게 구현
    a_sort[int(k)] = -1
    result.append(k)
print(*result)