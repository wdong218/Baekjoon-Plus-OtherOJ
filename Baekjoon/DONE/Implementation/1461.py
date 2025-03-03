import sys
n,m = map(int,sys.stdin.readline().split())
k = list(map(int,sys.stdin.readline().split()))
k = sorted(k, key=abs, reverse=True)
postive = []
nagative = []
result = 0
for i in range(n):
    if k[i] > 0:
        postive.append(k[i])
    else:
        nagative.append(abs(k[i]))
max_value = 0
for i in range(len(postive)):
    if i % m == 0:
        result += 2*postive[i]
        if postive[i] >max_value:
            max_value = postive[i]
for i in range(len(nagative)):
    if i % m == 0:
        result += 2*nagative[i]
        if nagative[i] >max_value:
            max_value = nagative[i]
print(result-max_value)