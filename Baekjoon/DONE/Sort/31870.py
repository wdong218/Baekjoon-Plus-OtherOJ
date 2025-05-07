import sys
import copy
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
count_up = 1
count_down = 0
a_up = a.copy()
a_down = a.copy()
target_up = sorted(a, reverse=True)
while a_up != target_up:
    for i in range(n-1):
        if a_up[i] < a_up[i+1]:
            temp = a_up[i+1]
            a_up[i+1] = a_up[i]
            a_up[i] = temp
            count_up += 1
target_down = sorted(a)
while a_down != target_down:
    for i in range(n-1):
        if a_down[i] > a_down[i+1]:
            temp = a_down[i+1]
            a_down[i+1] = a_down[i]
            a_down[i] = temp
            count_down += 1
print(min(count_up,count_down))