import sys
def input():
    return sys.stdin.readline()
n = int(input())
stack = list(map(int, input().split()))
stack_temp = []
i = 1
while stack_temp != [] or stack != []:
    if stack != [] and stack[0] == i:
        stack.pop(0)
        i += 1
    elif stack_temp != [] and stack_temp[-1] == i:
        stack_temp.pop()
        i += 1
    elif stack != []:
        stack_temp.append(stack.pop(0))
    else:
        break
if stack_temp == []:
    print("Nice")
else:
    print("Sad")