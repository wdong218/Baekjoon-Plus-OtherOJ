from collections import deque
"""메모리 초과로 다른 로직으로 짜기로 함"""
# n, k = map(int, input().split())
# visited = set()
#
# graph = [[] for _ in range(2)] # 그래프는 2개의 층만 존재해도 가능
# floor = 1
# graph[0] = [n]
# if n == k:
#     print("0")
# else:
#     visited = set()
#     queue = deque([n])  # BFS를 위한 큐
#     visited.add(n)
#     floor = 0
#     while queue:
#         for _ in range(len(queue)):  # 현재 층의 모든 노드 탐색
#             current = queue.popleft()
#             for next_pos in (current - 1, current + 1, current * 2):
#                 if next_pos == k:  # 목표 위치에 도달하면 종료
#                     print(floor + 1)
#                     exit()
#                 if next_pos not in visited:
#                     queue.append(next_pos)
#                     visited.add(next_pos)
#         floor += 1
#
#     print(floor)

n, k = map(int, input().split())
max_num = 100000
visited = [0] * (max_num+1)
count = 0
q = deque([n])

while 1:
    c = q.popleft()
    if c == k:
        break
    for i in (c-1,c+1,c*2):
        if 0 <= i <= max_num and visited[i] == 0:
            visited[i] = visited[c]+1
            q.append(i)


print(visited[c])