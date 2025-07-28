import sys
while 1:
    a = list(map(int,sys.stdin.readline().strip()))
    if a[0] == 0:
        break
    length = len(a)
    if length % 2 == 0:
        first = a[:length//2]
        second = a[length//2:]
        second.reverse()
        if first == second:
            print("yes")
        else:
            print("no")
    else:

        first = a[:length//2]
        second = a[length//2+1:]
        second.reverse()
        if first == second:
            print("yes")
        else:
            print("no")

