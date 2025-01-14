n = input()
if len(n) == 1:
    n = "0" + n

def second(k):
    if k // 10 == 0:
        return k
    return second(k%10)
count = 0
temp = n
while 1:
    first_num = temp[1]
    second_num = second(int(temp[1])+int(temp[0]))
    temp = str(first_num)+str(second_num)
    count += 1
    if temp == n:
        break


print(count)