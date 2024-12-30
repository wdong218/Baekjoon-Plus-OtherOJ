# 맞긴 한데 문제가 많은 코드 ChongChong 과 Chong 이 충돌 할 수 있음
n = int(input())
count = 1
check = "ChongChong"
for _ in range(n):
    a,b = input().split()
    if a in check and b not in check:
        count += 1
        check += b
    elif b in check and a not in check:
        count += 1
        check += a
print(count)

# set 을 이용한 풀이

n = int(input())
count = 1
connected = {"ChongChong"}  # 연결된 이름을 저장하는 집합

for _ in range(n):
    a, b = input().split()
    if a in connected or b in connected:  # 둘 중 하나가 연결되어 있으면
        connected.update([a, b])  # 둘 다 연결된 이름 집합에 추가
        count = len(connected)  # 집합 크기가 연결된 이름의 수와 동일

print(count)