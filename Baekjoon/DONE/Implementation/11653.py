N = int(input())
result = list()
while N != 1:
    for i in range(2,N+1):
        if (N/i).is_integer():
            result.append(i)
            N = N//i
            break

for i in range(len(result)):
    print(result[i])