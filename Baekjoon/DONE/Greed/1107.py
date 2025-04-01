import sys
num = int(sys.stdin.readline().strip())
if num == "100":
    print(0)
    exit(1)
a = int(sys.stdin.readline())
button = [True for i in range(10)]

if a != 0:
    b = list(map(int,sys.stdin.readline().split()))
    for i in b:
        button[i] = False
current_num = 0
count = 0
min_count = abs(100-int(num))
def check_num(i):
    check = True
    for j in i:
        if not button[int(j)]:
            check = False
    return check


for i in range(999999):

    if check_num(str(i)):
        min_count = min(min_count,len(str(i))+abs(i-int(num)))
print(min_count)