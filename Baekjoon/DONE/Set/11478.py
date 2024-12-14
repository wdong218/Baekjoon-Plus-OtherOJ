k = input()
result = set()
for i in range(len(k)):
    for j in range(len(k)):
        result.add(k[i:j+1])
print(len(result)-1)