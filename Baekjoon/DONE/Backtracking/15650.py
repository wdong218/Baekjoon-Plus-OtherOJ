# from itertools import combinations
# n,m = map(int,input().split())
# k = list(range(1,n+1))
# for combo in combinations(k, m):
#     print(" ".join(map(str,combo)))
n,m = map(int,input().split())

def backtrack(path,check):
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    for i in range(check, n + 1):  # 현재 숫자 이상만 탐색
        path.append(i)  # 숫자 추가
        backtrack(path, i + 1)  # 다음 단계 탐색
        path.pop()

backtrack([],1)