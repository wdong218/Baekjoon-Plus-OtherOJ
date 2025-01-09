n = int(input())
bottom_up = [0] * (n + 1)  # 리스트 크기를 n+1로 초기화

for i in range(2, n + 1):
    # 이전 값에서 +1
    candidates = [bottom_up[i - 1] + 1]
    # 2로 나누어지는 경우
    if i % 2 == 0:
        candidates.append(bottom_up[i // 2] + 1)
    # 3으로 나누어지는 경우
    if i % 3 == 0:
        candidates.append(bottom_up[i // 3] + 1)
    # 최소값을 선택
    bottom_up[i] = min(candidates)  # append 대신 직접 대입

print(bottom_up.pop())
