import sys

def generate_cantor(n):
    if n == 0:
        return "-"
    prev = generate_cantor(n - 1)  # 이전 단계의 칸토어 집합
    middle = " " * len(prev)  # 중간 공백
    return prev + middle + prev  # 칸토어 집합 구성


for line in sys.stdin:
    if line.strip():
        n = int(line.strip())
        print(generate_cantor(n))
    else:
        break