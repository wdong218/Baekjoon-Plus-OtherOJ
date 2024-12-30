n = int(input())
result = set()
count = 0
for _ in range(n):
    a = input().strip()
    if a == "ENTER":
        result.clear()
    elif a not in result:
        result.add(a)
        count += 1

print(count)