
v,e = map(int,input().split())
k = int(input())
MAX_VALUE = 9999999999
node = [[MAX_VALUE]*v for _ in range(v)]
for i in range(v):
    u,s_v,w = map(int,input().split())
    node[u-1][s_v-1] = w
    node[i][i] = 0

chek_node = [False] * v
while 1:
    min_value = 100000
    small_index = -1
    # 최소값 찾기
    for i in range(v):
        if not chek_node[i] and node[k][i] < min_value and node[k][i] != 0:
            min_value = node[k][i]
            small_index = i
    if small_index == -1:
        break
    # 거리 업데이트
    for i in range(v):
        if node[k-1][i] > node[k-1][small_index-1] + node[small_index-1][i]:
            node[k-1][i] = node[k-1][small_index-1] + node[small_index-1][i]
    # 노드 방문 처리
    chek_node[small_index] = True


for i in range(v):
    if node[k-1][i] ==MAX_VALUE:
        print("INF")
    else:
        print(node[k-1][i])