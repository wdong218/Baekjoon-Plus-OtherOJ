import sys
input = sys.stdin.readline
n = int(input())
num_list = []
for _ in range(n):
    a = int(input())
    num_list.append(a)
num_list.sort()
max_count = 0
for i in range(n):
    temp = 0
    for j in range(1,5):
        if num_list[i]+j in num_list:
            temp += 1
    max_count = max(max_count,temp)
result = 5-(max_count+1)
if result < 0:
    print(0)
else:
    print(result)