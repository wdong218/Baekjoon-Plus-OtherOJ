t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a == 10:
        print("10")
    else:
        check_list = []
        a = a % 10
        current = a

        while current not in check_list:
            check_list.append(current)
            current = (current * a) % 10
        cycle_length = len(check_list)
        position = (b - 1) % cycle_length
        if check_list[position] == 0:
            print("10")
        else:
            print(check_list[position])
