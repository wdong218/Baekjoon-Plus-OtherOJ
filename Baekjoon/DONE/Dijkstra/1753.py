"""2차원 배열을 선언해 다익스트라 알고리즘을 구현했지만 메모리 낭비가 너무 커져 실제 문제에서는 메모리초과로 실패 """

# v,e = map(int,input().split())
# k = int(input())
# MAX_VALUE = 9999999999
# node = [[MAX_VALUE]*v for _ in range(v)]
# for i in range(v):
#     u,s_v,w = map(int,input().split())
#     node[u-1][s_v-1] = w
#     node[i][i] = 0
#
# chek_node = [False] * v
# while 1:
#     min_value = 100000
#     small_index = -1
#     # 최소값 찾기
#     for i in range(v):
#         if not chek_node[i] and node[k][i] < min_value and node[k][i] != 0:
#             min_value = node[k][i]
#             small_index = i
#     if small_index == -1:
#         break
#     # 거리 업데이트
#     for i in range(v):
#         if node[k-1][i] > node[k-1][small_index-1] + node[small_index-1][i]:
#             node[k-1][i] = node[k-1][small_index-1] + node[small_index-1][i]
#     # 노드 방문 처리
#     chek_node[small_index] = True
#
#
# for i in range(v):
#     if node[k-1][i] ==MAX_VALUE:
#         print("INF")
#     else:
#         print(node[k-1][i])
import heapq
import sys
def input():
    return sys.stdin.readline()

v,e = map(int,input().split())
k = int(input())
MAX_VALUE = float('inf')
graph = {i: [] for i in range(1, v + 1)}
distance = [MAX_VALUE] * (v + 1)
for i in range(e):
    startNode, endNode, w = map(int, input().split())
    graph[startNode].append((endNode, w))

distance[k] = 0

def dijkstra(graph, start, distance):
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        current_dist, current_node = heapq.heappop(hq)
        # 이미 처리된 노드라면 무시
        if current_dist > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance_through_current = current_dist + weight

            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                heapq.heappush(hq, (distance_through_current, neighbor))




dijkstra(graph,k,distance)

for i in range(1, v + 1):
    if distance[i] == MAX_VALUE:
        print("INF")
    else:
        print(distance[i])