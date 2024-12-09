N = int(input())
result = list()
for i in range(N):
    result.append(int(input()))
result = sorted(result)
for i in range(len(result)):
    print(result[i])