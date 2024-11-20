k = int(input())
for i in range(k):
    a = ""
    n,m = input().split()
    n = int(n)
    for j in range(len(m)):
        a += m[j] * n
    print(a)