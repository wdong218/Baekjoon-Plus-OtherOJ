

l=sorted(set(i//10**j*10**(j+3)+666*10**j+i%10**j for i in range(9999) for j in range(6)))
print(l[int(input())-1])