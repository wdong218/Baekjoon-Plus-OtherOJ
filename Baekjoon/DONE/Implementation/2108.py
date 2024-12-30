from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
result = list()
ave = 0
i = 0
for _ in range(n):
    a = int(input())
    ave += a
    result.append(a)

print(round(ave/len(result))) #산술 평균
result.sort()
print(result[len(result) // 2]) #중앙값

counter = Counter(result)
max_freq = max(counter.values())
max_freq_list = [key for key, value in counter.items() if value == max_freq]
if len(max_freq_list) == 1:
    print(max_freq_list[0])
else:
    print(max_freq_list[1])

print(max(result)-min(result)) #범위