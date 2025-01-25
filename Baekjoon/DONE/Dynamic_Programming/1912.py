n = int(input())
q = list(map(int, input().split()))
result = []
result.append(q[0])
for i in range(1,n):
    k = q[i] + result[i-1]
    if k > q[i]:
        result.append(k)
    else:
        result.append(q[i])
print(max(result))