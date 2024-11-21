n = int(input())

for i in range(n):
    result = [0, 0, 0, 0]
    k = int(input())
    while k > 0:
        if k >= 25:
            result[0] += 1
            k -= 25
        elif k >= 10:
            result[1] += 1
            k-= 10
        elif k >= 5:
            result[2] += 1
            k -= 5
        else:
            result[3] += 1
            k -= 1
    print(" ".join(map(str, result)))