import sys
n,k,i = map(int,sys.stdin.readline().split())
result = [0 for _ in range(n)]
result[k-1] = 1
result[i-1] = 1
temp = []
floor = 0
check = True
while check:
    for i in range(0,len(result),2):
        if i == len(result)-1: #홀수 경우 예외처리
            temp.append(result[i])
            break
        if result[i] == 1 and result[i+1] == 1:
            check = False
            break
        elif result[i] == 1:
            temp.append(result[i])
        elif result[i+1] == 1:
            temp.append(result[i+1])
        else:
            temp.append(result[i])
    result = temp
    temp = []
    floor += 1
print(floor)