k = int(input())
a = list()
count = 0
a = list(map(int, input().split()))

for i in range(len(a)):
    check = 0
    for j in range(1,a[i]+1):
        if a[i] % j == 0:
            check += 1
    if check == 2:
        count += 1
print(count)
