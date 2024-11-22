k = int(input())
n = 1
count = 1
while n<k:
    count += 1
    n += 6*(count-1)
print(count)

"""
1
6 7
12 19
18 37
24 61

"""