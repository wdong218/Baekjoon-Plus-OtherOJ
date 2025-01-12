n = int(input())
score_list = []
for _ in range(n):
    score_list.append(list(map(int, input().split())))

visited = [0] * n  # 방문 여부
result = float('inf')  # 최소 차이를 저장할 변수


# 점수 계산 함수
def calculate_score():
    global result
    start_team, link_team = [], []

    # 팀 나누기
    for i in range(n):
        if visited[i]:  # 방문한 곳은 스타트 팀
            start_team.append(i)
        else:  # 방문하지 않은 곳은 링크 팀
            link_team.append(i)

    # 스타트 팀 점수 계산
    start_score = 0
    for i in start_team:
        for j in start_team:
            start_score += score_list[i][j]

    # 링크 팀 점수 계산
    link_score = 0
    for i in link_team:
        for j in link_team:
            link_score += score_list[i][j]

    # 점수 차이 계산 및 최소값 갱신
    diff = abs(start_score - link_score)
    result = min(result, diff)


# 백트래킹 함수
def backtrack(depth, idx):
    if depth == n // 2:  # 스타트 팀이 완성되면
        calculate_score()  # 점수 계산
        return

    for i in range(idx, n):  # 조합 생성
        if not visited[i]:
            visited[i] = 1  # 방문 체크
            backtrack(depth + 1, i + 1)  # 다음 인덱스 탐색
            visited[i] = 0  # 백트래킹: 방문 해제


# 백트래킹 시작
backtrack(0, 0)
print(result)