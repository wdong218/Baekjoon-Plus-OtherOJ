while 1:
    k = []
    q = input().split()
    if max(q) == "0":
        break
    result = 0
    for i in range(3):
        k.append(int(q[i])**2)
        result += int(q[i])**2
    if 2*max(k) == result:
        print("right")
    else:
        print("wrong")
