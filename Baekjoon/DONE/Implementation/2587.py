a = list()
k = 0
for i in range(5):
    a.append(int(input()))
    k += a[i]
a = sorted(a)
print(k//5)
print(a[2])