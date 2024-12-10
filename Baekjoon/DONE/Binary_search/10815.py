def binary_search(w, a, left, right):
    if left > right:  # 종료 조건
        return 0
    mid = (left + right) // 2
    if w[mid] == a:
        return 1
    elif w[mid] < a:
        return binary_search(w, a, mid + 1, right)
    else:
        return binary_search(w, a, left, mid - 1)

n = int(input())
k = list(input().split())
m = int(input())
g = list(input().split())
k.sort()
for i in range(len(g)):
    g[i] = binary_search(k,g[i],0,len(k)-1 )
for i in range(len(g)):
    print(g[i],end=" ")