n = int(input())

if n == 1:
    print(1 % 15746)
elif n == 2:
    print(2 % 15746)
else:
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 2
    for i in range(3, n + 1):
        f[i] = (f[i-1] + f[i-2]) % 15746
    print(f[n])