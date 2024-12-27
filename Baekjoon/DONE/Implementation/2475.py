k = input().split()
result = 0
for i in range(len(k)):
    result += int(k[i])**2
print(result%10)