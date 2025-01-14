import sys
n = int(input())
k = list(map(int,sys.stdin.readline().split()))
k.sort()
time_k = [k[0]]
for i in range(len(k)-1):
    time_k.append(time_k[i]+k[i+1])
print(sum(time_k))