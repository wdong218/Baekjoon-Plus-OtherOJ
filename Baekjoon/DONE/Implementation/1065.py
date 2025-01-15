n = int(input())
count = 0
for i in range(1,n+1):
    i = str(i)
    if len(i) == 1:
        first_num = int(i[0])
        count += 1
    elif len(i) == 2:
        first_num = int(i[0])
        second_num = int(i[1])
        count += 1
    else:
        first_num = int(i[0])
        second_num = int(i[1])
        third_num = int(i[2])
        if second_num - first_num == third_num - second_num:
            count += 1

print(count)