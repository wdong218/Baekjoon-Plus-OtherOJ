t = int(input())
num_list = [1,2,4]
for i in range(t):
    n = int(input())
    if len(num_list) > n:
        print(num_list[n-1])
    else:
        max_index = len(num_list)
        for j in range(max_index, n):
            num = num_list[j - 3] + num_list[j - 2] + num_list[j - 1]
            num_list.append(num)
        print(num_list[n - 1])
