from collections import defaultdict
n = int(input())
result = list()
ave = 0
k = defaultdict(list)
for i in range(n):
    a = int(input())
    k[a].append(i)
    ave += a
    result.append(a)
max_len = max(len(v) for v in k.values())
filtered = {k: v for k, v in k.items() if len(v) == max_len}
print(round(ave/len(result))) #산술 평균
result.sort()
print(result[round(len(result)/2)]) #중앙값
max_freq = max(len(v) for v in k.values())
modes = [key for key, value in k.items() if len(value) == max_freq]
modes.sort()  # 최빈값이 여러 개면 가장 작은 값 다음 값 선택
if
print(max(result)-min(result)) #범위