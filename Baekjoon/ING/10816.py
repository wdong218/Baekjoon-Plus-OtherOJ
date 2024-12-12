import sys
input = sys.stdin.readline
n = int(input())
have = list(map(int, input().split()))
m = int(input())
comparison = {}
results = map(int, input().split())
for result in results:
    comparison[result] = 0
for value in have:
    if value in comparison:
        comparison[value] += 1
print(" ".join(map(str, comparison.values())))