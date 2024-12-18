import math
n = int(input())
positions = list()
for i in range(n):
    positions.append(int(input()))
gaps = list()
for i in range(0,n-1):
    gaps.append(abs(positions[i+1]-positions[i]))
gcd_of_gaps = gaps[0]
for i in range(1,len(gaps)):
    gcd_of_gaps = math.gcd(gcd_of_gaps,gaps[i])
count = 0
for i in range(len(positions)-1):
    if abs(positions[i+1]-positions[i]) != gcd_of_gaps:
        count += abs(positions[i+1]-positions[i])//gcd_of_gaps-1
print(count)