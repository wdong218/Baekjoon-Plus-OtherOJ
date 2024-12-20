k = int(input())
stack = []
result = 0
for i in range(k):
    n = int(input())
    if n == 0:
        result -= stack.pop()
    else:
        stack.append(n)
        result += n
print(result)