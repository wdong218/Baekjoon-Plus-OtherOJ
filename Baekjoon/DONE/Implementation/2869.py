import math
A, B, V = map(int, input().split())
up_tree = A-B
goal_tree = V - A
count = 0
count = math.ceil(goal_tree/up_tree) +1
print(count)