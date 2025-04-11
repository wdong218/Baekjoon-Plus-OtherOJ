import sys
n = int(sys.stdin.readline())
num_list = [sys.stdin.readline().strip() for _ in range(n)]

len_num = len(num_list[0])

for i in range(1, len_num + 1):
    check_list = [s[-i:] for s in num_list]
    if len(set(check_list)) == n:
        print(i)
        break
