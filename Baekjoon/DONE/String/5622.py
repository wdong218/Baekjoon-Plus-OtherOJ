k = input()
count = 0
for i in range(len(k)):
    if k[i] in "ABC":
        count += 3
    elif k[i] in "DEF":
        count += 4
    elif k[i] in "GHI":
        count += 5
    elif k[i] in "JKL":
        count += 6
    elif k[i] in "MNO":
        count += 7
    elif k[i] in "PQRS":
        count += 8
    elif k[i] in "TUV":
        count += 9
    elif k[i] in "WXYZ":
        count += 10

print(count)