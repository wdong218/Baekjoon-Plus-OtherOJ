import sys
n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
fuel = list(map(int,sys.stdin.readline().split()))
fuel.pop()
min_fuel = fuel[0]
k = 0
result = fuel[0] * road[0]
for i in range(1,n-1):
    k += road[i]
    if min_fuel > fuel[i]:
        result += min_fuel * (k-road[i])
        min_fuel = fuel[i]
        k = road[i]
result += k*min_fuel
print(result)

# 30,10+8,10+6+4
# 6 4 1
