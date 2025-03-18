import sys
m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    a,*b = sys.stdin.readline().split()
    if b:
        b[0] = int(b[0])
    if a == "add" and b[0] not in s:
        s.add(b[0])
    elif a == "check":
        if b[0] in s:
            print("1")
        else:
            print("0")
    elif a == "remove" and b[0] in s:
        s.remove(b[0])
    elif a == "toggle":
        if b[0] in s:
            s.remove(b[0])
        else:
            s.add(b[0])
    elif a == "all":
        s = set()
        for i in range(1,21):
            s.add(i)
    elif a == "empty":
        s = set()




