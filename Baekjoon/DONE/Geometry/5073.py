while 1:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if max(a,b,c) >= a+b+c - max(a,b,c):
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a== b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")