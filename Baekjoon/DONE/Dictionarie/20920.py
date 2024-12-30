import sys
read  = sys.stdin.readline
n,m = map(int,read().split())
result = {}
for i in range(n):
    a = read().rstrip()
    if len(a) >= m:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1
""" 
(1)-x[1]: 값(value)의 내림차순
x[1]은 딕셔너리 값(value)을 나타냅니다.
음수(-)를 붙여 내림차순 정렬.
예: 값이 [5, 5, 2, 2]인 경우, 내림차순으로 [5, 5, 2, 2].
(2) -len(x[0]): 키(key) 길이의 내림차순
x[0]은 딕셔너리 키(key)를 나타냅니다.
len(x[0])은 문자열의 길이를 계산.
음수(-)를 붙여 내림차순 정렬.
예: 키 길이가 [5, 6, 6, 4]인 경우, 내림차순으로 [6, 6, 5, 4].
(3) x[0]: 키(key)의 사전순 오름차순
앞의 두 기준이 동일한 경우, 키(key)를 **사전 순(알파벳 순)**으로 정렬.
예: ['apple', 'banana']는 ['apple', 'banana'].
"""
result = sorted(result.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for key, value in result:
    print(key)