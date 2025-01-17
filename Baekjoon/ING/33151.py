n,k = map(int,input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
if k < 2*n -1:
    print("-1")
else:
    k -= 2*n -1 # 기본적인 1 구성 후 남은 코인 갯수
    for i in range(n):  # 대각선 기본적인 1 구성
        for j in range(n):
            if i == j:  # 대각선
                grid[i][j] += 1
    if k % 2 != 0:
        result = -1
    else:
        count = k // 2



# 1 0 1
# 0 1 0
# 1 0 1


# # 2*n -1 개의 동전일 경우 무조건 가능 그 이하의 경우 불가능
# # 2 2 2 2 채우고
# 1 2 1
# 2 1 2
# 1 2 1
#
# #그 다음에도 2씩 늘어나야됨 만약 남은 동전이 홀수 개라면 -1 출력
# 3 2 1
# 2 1 2
# 1 2 1
