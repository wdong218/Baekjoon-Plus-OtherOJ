import sys
s = sys.stdin.readline()
zero_one = [0,0]

for i in range(1,len(s)):
    if s[i] != s[i-1] and s[i-1] == "0":
        zero_one[0] += 1
    elif s[i] != s[i-1] and s[i-1] == "1":
        zero_one[1] += 1

print(min(zero_one))

