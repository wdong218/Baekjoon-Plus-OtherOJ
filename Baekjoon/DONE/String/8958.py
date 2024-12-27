t = int(input())
for i in range(t):
    count = 0
    point = 0
    k = input()
    for j in range(len(k)):
        if k[j] == "O":
            point += 1
            count += point
        else:
            point = 0
    print(count)