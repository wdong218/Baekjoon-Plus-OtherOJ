# k = int(input())
# array = []
# s_overlaps = []
# result = 0
#
# # 사각형 정보 입력
# for i in range(k):
#     x, y = map(int, input().split())
#     array.append((x, y))
#
# # 겹치는 부분 찾기
# for i in range(k):
#     for j in range(i + 1, k):
#         x1, y1 = array[i]
#         x2, y2 = array[j]
#
#         # 겹치는 x, y 좌표 범위 계산
#         x_start = max(x1, x2)
#         x_end = min(x1 + 10, x2 + 10)
#         y_start = max(y1, y2)
#         y_end = min(y1 + 10, y2 + 10)
#
#         # 겹치는 부분이 있는지 확인
#         if x_start < x_end and y_start < y_end:
#             new_overlap = [x_start, y_start, x_end, y_end]
#
#             # 기존 겹치는 부분과 비교하여 병합할지 결정
#             is_new_overlap = True
#             for overlap in s_overlaps:
#                 if (overlap[0] <= new_overlap[2] and overlap[2] >= new_overlap[0] and
#                         overlap[1] <= new_overlap[3] and overlap[3] >= new_overlap[1]):
#                     # 겹치는 부분 병합
#                     overlap[0] = min(overlap[0], new_overlap[0])
#                     overlap[1] = min(overlap[1], new_overlap[1])
#                     overlap[2] = max(overlap[2], new_overlap[2])
#                     overlap[3] = max(overlap[3], new_overlap[3])
#                     is_new_overlap = False
#                     break
#
#             # 새로운 겹치는 부분을 추가
#             if is_new_overlap:
#                 s_overlaps.append(new_overlap)
#
# # 겹치는 부분 면적 계산
# for overlap in s_overlaps:
#     result += (overlap[2] - overlap[0]) * (overlap[3] - overlap[1])
#
# # 최종 출력 (각 사각형이 10x10이므로, 전체 면적에서 겹치는 면적을 뺌)
# print(k * 100 - result)

#중첩 구조는 병합하는 부분이 너무 구현이 어려워 다른 방식으로 구현함

#먼저 grid의 100*100 크기의 격자를 만든뒤 좌표 범위 안에 해당하는 인덱스를 1로 지정
#1인 부분만 골라서 result에 더해줌
k = int(input())
grid = [[0] * 100 for _ in range(100)]
for i in range(k):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = 1
result = sum(sum(row) for row in grid)
print(result)