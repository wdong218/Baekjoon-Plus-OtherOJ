list_music = list(map(int,input().split()))
check_list = list(range(1, 9))

if list_music == check_list:
    print("ascending")
elif list(reversed(list_music)) == check_list:
    print("descending")
else:
    print("mixed")