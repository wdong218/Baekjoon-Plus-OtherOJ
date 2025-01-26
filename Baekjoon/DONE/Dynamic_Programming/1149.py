import sys
n = int(sys.stdin.readline())
rgb = list()
for _ in range(n):
    line = sys.stdin.readline().strip().split()
    row = list(map(int, line))
    rgb.append(row)
for i in range(1,n):
    rgb[i][0] = min((rgb[i-1][1]+rgb[i][0]),(rgb[i-1][2]+rgb[i][0]))
    rgb[i][1] = min((rgb[i-1][0]+rgb[i][1]),(rgb[i-1][2]+rgb[i][1]))
    rgb[i][2] = min((rgb[i-1][0]+rgb[i][2]),(rgb[i-1][1]+rgb[i][2]))
print(min(rgb[n-1]))