N = int(input())
for i in range(2 * N - 1):
    if i < N:
        # 피라미드 부분
        spaces = N - i - 1  # 공백 개수
        stars = 2 * i + 1  # 별 개수
    else:
        # 역피라미드 부분
        spaces = i - N + 1  # 공백 개수
        stars = 2 * (2 * N - i - 1) - 1  # 별 개수
    print(" " * spaces + "*" * stars)
