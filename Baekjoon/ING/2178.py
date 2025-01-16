import sys
from collections import deque
n,m = map(int,input().split())
mage = [[] for _ in range(n)]
for i in range(n):
    k = sys.stdin.readline().strip()
    mage[i] = k
print(mage)
"""다시 풀때 그림 그려보기 루트 노드는 0,0부터 시작해서 1로 연결돼 있는 곳이 연결 노드이며 연결 돼있는 부분은 자식 노드임"""
count = 0
def bfs(mage,x,y,visited):
    visited.append((x,y))
    q = deque()
    q.append((x,y))
    while 1:
        if x == n and y == m: # 목표 지점 도달 시 카운트 리턴
            return count
        if mage[y][x] == 1 and (x,y) not in visited : # 1이나 방문하지 않은 곳 만날시 좌표 이동
            visited.append((x+1,y)) #오른쪽으로 한칸 이동
        else:
            bfs(x-1,y+1) #만약 0을 만나거나 방문 했던 곳을 만날시 전 좌표로 이동 후 y좌표 변경

bfs(0,0,[])