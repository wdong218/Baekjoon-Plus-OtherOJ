N = int(input())
a = 0
result = list()
while a <= N:
    k = list()
    m = 0
    for i in str(a):
        k.append(i)
    for i in range(len(k)):
        m += int(k[i])
    m = m+a

    if m == N:
        result.append(k)
    a += 1
real = [''.join(item) for item in result]
if real != []:
    print(min(real))
else:
    print("0")