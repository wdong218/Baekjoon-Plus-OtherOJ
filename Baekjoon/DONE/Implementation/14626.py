import sys
num = sys.stdin.readline().strip()
m = int(num[-1])
result = 0
for i in range(len(num)-1):
    if i % 2 == 0: #짝수일경우
        if num[i] == "*":
            x = 1
        else:
            result += int(num[i])
    else: #홀수
        if num[i] == "*":
            x = 3
        else:
            result += 3*int(num[i])

for i in range(10):
    k = i * x
    if m == (10-(result+k)%10)%10:
        print(i)
        break
    else:
        continue

