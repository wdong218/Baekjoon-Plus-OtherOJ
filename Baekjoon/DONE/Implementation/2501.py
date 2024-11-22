N,K = map(int,input().split())
w =[]
for i in range(1,N+1):
    if N % i == 0:
        w.append(i)
if len(w) < K:
    print(0)
else:
    print(w[K-1])