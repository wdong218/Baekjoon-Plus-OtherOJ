import sys
import itertools
l,c = map(int,input().split())
a = sys.stdin.readline().split()
a = sorted(a)
q = ['a','e','i','o','u']
q_set = set(q)
filtered_combinations = [
    comb
    for comb in itertools.combinations(a, l)
    if 1 <= sum(char in q_set for char in comb) <= l-2
]

for i in range(len(filtered_combinations)):
    print("".join(sorted(filtered_combinations[i])))