n, k = map(int, input().split())
visited = set()

graph = [[] for _ in range(2)] # 그래프는 2개의 층만 존재해도 가능
floor = 1
graph[0] = [n]
if n == k:
    print("0")
else:
    while 1:
        next_floor = set()
        for i in graph[0]:
            if i-1 not in visited:
                next_floor.add(i - 1)
                visited.add(i - 1)
            if i * 2 not in visited:
                next_floor.add(i * 2)
                visited.add(i * 2)
            if i + 1 not in visited:
                next_floor.add(i + 1)
                visited.add(i + 1)
        graph[1] = list(next_floor)

        if k in graph[1]:  # k에 도달하면 종료
            break
        graph[0] = graph[1]
        graph[1] = []
        floor += 1

    print(floor)