from itertools import combinations_with_replacement
n,m = map(int,input().split())
k = list(range(1,n+1))
for combo in combinations_with_replacement(k, m):
    print(" ".join(map(str,combo)))