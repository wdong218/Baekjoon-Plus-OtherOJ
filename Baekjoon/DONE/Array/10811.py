#10811
N ,M = map(int,input().split())
list_1 = list(range(1,N+1))
for k in range(M):
    i,j = map(int,input().split())
    for _ in range (j):
        if i >= j:
            break
        temp = list_1[i-1]
        list_1[i-1] = list_1[j-1]
        list_1[j-1] = temp
        i += 1
        j -= 1

for i in range(len(list_1)):
    print(list_1[i],end=" ")
