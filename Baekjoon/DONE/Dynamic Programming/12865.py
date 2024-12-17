import sys
def input():
    return sys.stdin.readline()
l = tuple()
n,k = map(int,input().split())
for i in range(n):
    a,b = map(int,input().split())
    if a <= k:
        l += ((a, b),)
A = [[0 for x in range(k + 1)] for x in range(n + 1)]
# DP 테이블 채우기
for i in range(1, len(l) + 1):  # i번째 아이템까지 고려
    for j in range(1, k + 1):   # 배낭 용량 j까지
        if l[i-1][0] > j:  # 현재 아이템의 무게가 j를 초과하면 넣을 수 없음
            A[i][j] = A[i-1][j]
        else:  # 현재 아이템을 넣는 경우와 넣지 않는 경우 중 최대값 선택
            valWith = l[i-1][1] + A[i-1][j - l[i-1][0]]  # 아이템을 넣는 경우
            valWithout = A[i-1][j]  # 아이템을 넣지 않는 경우
            A[i][j] = max(valWith, valWithout)

print(A[len(l)][k])
