while True:
    k = int(input())
    a = []
    result = 0
    per_output = ""
    if k == -1:
        break
    for i in range(1,k+1):
        if k % i == 0:
            a.append(i)

    for i in range(len(a)-1):
        result += a[i]
    if k == result:
        for i in range(len(a)-1):
            per_output += str(a[i])+" + "
        print(k,"=",per_output[:len(per_output)-2])
    else:
        print(k,"is NOT perfect.")