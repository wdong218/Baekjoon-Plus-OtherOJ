import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))

# 숫자 개수 세기
count_dict = Counter(have)
m = int(input())
result = list(map(int, input().split()))
for i in range(m):
    if result[i] in count_dict:
        result[i] = count_dict[result[i]]
    else:
        result[i] = 0
print(' '.join(map(str, result)))