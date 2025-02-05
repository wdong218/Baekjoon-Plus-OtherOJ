import sys
n,k = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))
max_value = [0]*(n-k+1)
for i in range(k):
    max_value[0] += num_list[i]
one_point = 1
two_point = k
for i in range(1,n-k+1):
    value = max_value[i-1] - num_list[one_point-1]+num_list[two_point]
    max_value[i] = value
    one_point += 1
    two_point += 1
print(max(max_value))



