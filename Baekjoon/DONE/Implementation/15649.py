from itertools import permutations
n,m = map(int,input().split())
k = list(range(1,n+1))
for combo in permutations(k, m):
    print(" ".join(map(str,combo)))