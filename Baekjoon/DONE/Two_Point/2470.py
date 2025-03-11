import sys
n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().split()))
k.sort()
r_start = 0
r_end = n-1
start = 0
end = n-1
min_value = float('inf')
while start != end:
    if k[start] + k[end] < 0:
        if abs(k[start] + k[end]) < abs(min_value):
            min_value =k[start]+k[end]
            r_start = start
            r_end = end
        start += 1
    elif k[start] + k[end] == 0:
        r_start = start
        r_end = end
        break
    else:
        if abs(k[start] + k[end]) < abs(min_value):
            min_value =k[start]+k[end]
            r_start = start
            r_end = end
        end -= 1

print(k[r_start],k[r_end])


