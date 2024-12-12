import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k_list = []
k_dict = {}

for i in range(1, n+1):
    name = input().strip()  # 이름 입력받기
    k_dict[name] = i        # 이름 -> 인덱스 저장
    k_list.append(name)     # 인덱스 -> 이름 저장

# 쿼리 처리
output = []
for _ in range(m):
    b = input().strip()  # 쿼리 입력받기
    if b.isdigit():  # 숫자인 경우
        output.append(k_list[int(b) - 1])
    else:            # 이름인 경우
        output.append(str(k_dict[b]))

sys.stdout.write("\n".join(output) + "\n")
