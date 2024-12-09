# 시간초과 뜬 코드 for 문 이중중첩 O(n^2)
"""
n = int(input())
k = input().split()
result = []
count = 0
for i in range(len(k)):
    temp = []
    count = 0
    for j in range(len(k)):
        if (int(k[i]) > int(k[j]) and k[j] not in temp):
            temp.append(k[j])
            count += 1
    result.append(count)

for i in range(len(result)):
    print(result[i],end=" ") """
def binary_search(w, a, left, right):
    mid = (left + right) // 2
    if w[mid] == a:
        return mid
    elif w[mid] < a:
        return binary_search(w, a, mid + 1, right)
    else:
        return binary_search(w, a, left, mid - 1)

n = int(input())
k = list(map(int,input().split()))
w = sorted(set(map(int, k)))
result = [0]*n
for i in range(n):
    result[i] = binary_search(w,k[i],0,len(w)-1)
for i in range(len(result)):
    print(result[i],end=" ")