import sys
input = sys.stdin.readline
n,c = map(int,input().split())
house = []
result = []
for _ in range(n):
    a = int(input())
    house.append(a)
house.sort()

low = 0
high = house[-1]-house[0]
result = 0
while low <= high:
    count = 1
    mid = (high+low)//2
    k = 0
    for i in range(1,n):
        dif = house[i]-house[k]
        if dif >= mid:
            count += 1
            k = i
    if count >= c:
        result = mid
        low = mid + 1
    else:
        high = mid -1
print(result)


