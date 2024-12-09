N = int(input())
result = []
for i in range(N):
    x,y = map(int,input().split())
    result.append((x,y))
result = sorted(result)
for x, y in result:
    print(f"{x} {y}")