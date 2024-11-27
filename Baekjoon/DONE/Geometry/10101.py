result = 0
k = list()
for i in range(3):
    k.append(int(input()))
    result += k[i]

if result != 180:
    print("Error")
else:
    if k[0] == k[1] == k[2] == 60:
     print("Equilateral")
    elif k[0] == k[1] or k[1] == k[2] or k[0] == k[2]:
     print("Isosceles")
    elif k[0] != k[1] and k[1] != k[2] and k[0] != k[2]:
     print("Scalene")