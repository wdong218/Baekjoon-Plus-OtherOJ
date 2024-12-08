N = int(input())
result = list()
x_5 = 0

while x_5*5 <= N:
    x_3 = (N - x_5 * 5) // 3
    if (x_3)*3 == N-(x_5 * 5):
        result.append(x_3+x_5)
        x_5 += 1
    else:
        x_5 += 1

if result == []:
    print("-1")
else:
    print(min(result))