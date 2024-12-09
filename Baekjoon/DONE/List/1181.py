n = int(input())
result = []
for i in range(n):
    x = input()
    if x not in [word for _, word in result]:
        result.append((len(x), x))
result.sort()

for i in range(len(result)):
    print(result[i][1])
