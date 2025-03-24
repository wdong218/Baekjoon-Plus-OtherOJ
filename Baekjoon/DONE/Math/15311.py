result = [2000]
for i in range(1,1000):
    result.append(1)
for i in range(1,1001):
    result.append(1000)
print(len(result))
print(*result)