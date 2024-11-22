while 1:
    result = ["factor","multiple","neither"]
    a,b = map(int,input().split())
    if a ==0 and b == 0:
        break
    if b % a == 0:
        print(result[0])
    elif a % b == 0:
        print(result[1])
    else:
        print(result[2])
