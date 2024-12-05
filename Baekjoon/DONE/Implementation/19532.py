numbers = list(map(int, input().split()))
a,b,c,d,e,f = numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5]
x = -999
y = -999
k = True

while k and x != 1000:
    y = -999
    while y != 1000:
        if a*x + b*y == c and d*x + e*y == f:
            k = False
            break
        y += 1
    if k:
        x += 1
print(x,y)