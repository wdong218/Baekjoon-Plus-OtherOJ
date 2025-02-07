import sys
a = sys.stdin.readline().strip()
num_list_plus = []
num_list_min = []
num = ''
check = False
for i in range(len(a)):
    if a[i] == '+':
        if check == False:
            num_list_plus.append(int(num))
        else:
            num_list_min.append(int(num))
        num = ''
    elif a[i] == '-':
        if check == False:
            num_list_plus.append(int(num))
            check = True
        else:
            num_list_min.append(int(num))
            check = True
        num = ''
    else:
        num += a[i]
if check == True:
    num_list_min.append(int(num))
else:
    num_list_plus.append(int(num))
# print(num_list_plus,num_list_min)
print(sum(num_list_plus)-sum(num_list_min))

