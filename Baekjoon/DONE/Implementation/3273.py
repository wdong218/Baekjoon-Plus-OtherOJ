import sys
n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())
k_set = set(k)
result = 0

for num in k:
    target = x - num
    if target in k_set and num != target:
        result += 1

print(result // 2)