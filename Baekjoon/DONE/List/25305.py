n,k = map(int,input().split())
values = input().split()
result = list()
for i in range(len(values)):
    result.append(int(values[i]))
result = sorted(result)
print(result[len(result)-k])