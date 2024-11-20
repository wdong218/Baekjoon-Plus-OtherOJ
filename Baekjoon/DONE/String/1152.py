k = input()
count = 1
s_blank = 0
e_blank = 0
for i in range(len(k)):
    if k[0] == " ":
        s_blank = 1
    if k[len(k)-1] == " ":
        e_blank = 1
    if k[i] == " ":
       count += 1

print(count-s_blank-e_blank)