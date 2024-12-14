t = int(input())
for i in range(t):
    result = []
    a,b = map(int,input().split())
    if a > b:
        for i in range(1,b+1):
            if b % i == 0 and i*a % b ==0:
                result.append(i*a)
    elif b > a:
        for i in range(1,a+1):
            if a % i == 0 and i*b % a == 0:
                result.append(i*b)
    else:
        result.append(a)
    print(min(result))