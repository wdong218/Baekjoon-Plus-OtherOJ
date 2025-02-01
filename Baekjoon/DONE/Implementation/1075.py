n = int(input())
k = int(input())

temp = (n // 100) * 100

candidate = None
for i in range(100):
    x = temp + i
    if x % k == 0:
        candidate = i
        break

print(f"{candidate:02d}")
