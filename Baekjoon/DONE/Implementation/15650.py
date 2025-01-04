from itertools import combinations
n,m = map(int,input().split())
k = list(range(1,n+1))
for combo in combinations(k, m):
    print(" ".join(map(str,combo)))