S = input()
result = ""
for i in range(26):
    result += str(S.find(chr(97+i))) + " "
print(result)