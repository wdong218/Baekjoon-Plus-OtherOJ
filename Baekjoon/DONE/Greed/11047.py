n, k = map(int,input().split())
coin = []
for i in range(n):
    a = int(input())
    if a <= k:
        coin.append(a)
count = 0
i = 0
while k != 0:
    if len(coin)-i < 0:
        break
    if k >= coin[len(coin)-i-1]:
        count += k // coin[len(coin)-i-1]
        k %= coin[len(coin)-i-1]
    else:
        i += 1
print(count)



