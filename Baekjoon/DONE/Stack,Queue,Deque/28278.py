import sys
def input():
    return sys.stdin.readline()
stack= []
n = int(input())
for _ in range(n):
    a, *rest = map(int, input().split())
    if a == 1:
        b = rest[0]
        stack.append(b)
    elif a == 2:
        if stack != []:
            print(stack.pop())
        else:
            print("-1")
    elif a == 3:
        print(len(stack))
    elif a == 4:
        if stack != []:
            print("0")
        else:
            print("1")
    elif a == 5:
        if stack != []:
            temp = stack[-1]
            print(temp)
        else:
            print("-1")
