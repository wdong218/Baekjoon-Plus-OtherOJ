k = int(input())
n = 1
while k>n:
    k -= n
    n += 1

if n % 2 == 0:
    x_dos = k
    y_dos = n - k + 1
else:
    x_dos= n - k + 1
    y_dos = k

print(str(x_dos) + "/" + str(y_dos))

