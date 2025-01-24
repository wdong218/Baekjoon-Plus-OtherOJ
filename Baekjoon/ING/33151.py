import sys
input = sys.stdin.readline
n, k = map(int, input().split())
grid = [[0] * n for _ in range(n)]  # numpy 대신 파이썬 2차원 리스트

if n % 2 == 0:  # n이 짝수인 경우
    if k % 2 != 0 or (n ** 2) // 2 > k:
        print("-1")
    else:
        # 기본 격자판 구성 갯수
        base = k // (6 * n)

        for i in range(n):
            for j in range(n):
                if j % 2 == 0 and i % 2 == 0:
                    grid[i][j] = base
                    k -= base
                if i % 2 == 0 and j % 2 != 0:
                    grid[i][j] = base + 1
                    k -= (base + 1)
                if i % 2 != 0 and j % 2 != 0:
                    grid[i][j] = base
                    k -= base
                if i % 2 != 0 and j % 2 == 0:
                    grid[i][j] = base + 1
                    k -= (base + 1)

        y = 0
        x = 0
        print(grid)
        print(k)
        while k > 0:
            if y > n - 1:
                y = 0
                x = 0
            # x+1이 범위를 넘지 않고, grid[y][x] > grid[y][x+1] 이면 오른쪽 칸에 +2
            if x + 1 < n and grid[y][x] > grid[y][x + 1]:
                grid[y][x + 1] += 2
                k -= 2
            else:
                grid[y][x] += 2
                k -= 2
            x += 2
            if x > n - 2:
                x = 0
                y += 1

# 홀수가 제일 문제 !!!@!@!@ 나중에 다시 풀기 ~~@~@~!@~!2₩
else:  # n이 홀수인 경우
    if (n ** 2) // 2 > k:
        print("-1")
    else:
        a = (n ** 2) // 2
        b = a + 1
        base = k // (a + 2 * b)

        if k % 2 == 0:  # k가 짝수인 경우
            for i in range(n):
                for j in range(n):
                    if i % 2 == 0 and j % 2 != 0:
                        if base == 0:
                            grid[i][j] = 1
                            k -= 1
                        else:
                            grid[i][j] = base
                            k -= base

                    if i % 2 == 0 and j % 2 == 0 and base != 0:
                        grid[i][j] = base + 1
                        k -= (base + 1)

                    if i % 2 != 0 and j % 2 == 0:
                        if base == 0:
                            grid[i][j] = 1
                            k -= 1
                        else:
                            grid[i][j] = base
                            k -= base

                    if i % 2 != 0 and j % 2 != 0 and base != 0:
                        grid[i][j] = base + 1
                        k -= (base + 1)


            q = min(grid[0][0], grid[0][1])
            for i in range(n):
                if k <= 0:
                    break
                for j in range(n):
                    if k <= 0:
                        break
                    if grid[i][j] == q:
                        grid[i][j] += 2
                        k -= 2

        else:  # k가 홀수인 경우
            a = (n ** 2) // 2 + 1
            b = a - 1
            base = k // (a + 2 * b)
            print(base)

            for i in range(n):
                for j in range(n):
                    if i % 2 == 0 and j % 2 == 0:
                        if base == 0:
                            grid[i][j] = 1
                            k -= 1
                        else:
                            grid[i][j] = base
                            k -= base

                    if i % 2 == 0 and j % 2 != 0 and base != 0:
                        grid[i][j] = base + 1
                        k -= base + 1

                    if i % 2 != 0 and j % 2 != 0:
                        if base == 0:
                            grid[i][j] = 1
                            k -= 1
                        else:
                            grid[i][j] = base
                            k -= base

                    if i % 2 != 0 and j % 2 == 0 and base != 0:
                        grid[i][j] = base + 1
                        k -= base + 1
            print(k)

            q = min(grid[0][0],grid[0][1])
            for i in range(n):
                if k <= 0:
                    break
                for j in range(n):
                    if k <= 0:
                        break
                    if grid[i][j] == q:
                        grid[i][j] += 2
                        k -= 2

# 결과 출력
for row in grid:
    print(*row)
