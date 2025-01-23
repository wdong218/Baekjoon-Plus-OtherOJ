n,k = map(int,input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
if n % 2 == 0: # n이 짝수 인 경우
    if k % 2 != 0 or n**2//2 < k: #n이 짝수 인 경우 무조건 k도 짝수여야 격자판 채우기 가능 or 격자판의 갯수 // 2 보다 k가 크거나 같아야 채우기 가능
        print("-1")
    else: # 그외의 경우는 무조건 격자판 채우기 가능
        #기본 격자판 구성 짝수의 경우 1가지 격자판만 고려해도 됨
        for i in range(n):
            for j in range(n):
                if j % 2 == 0 and i % 2 == 0:
                    grid[i][j] = 1
                if i % 2 != 0 and j % 2 != 0:
                    grid[i][j] = 1
        k -= n**2//2
        while k > 0:



        print(grid)

else: #n이 홀수 인 경우
    if n**2//2 < k: #n이 홀수라면 이 경우만 따지면 됨 나머지는 다 가능
        print("-1")
    else:
        pass