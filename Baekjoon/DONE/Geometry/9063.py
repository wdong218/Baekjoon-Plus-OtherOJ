n = int(input())
x_dos = list()
y_dos = list()
for _ in range(n):
    x,y = map(int,input().split())
    x_dos.append(x)
    y_dos.append(y)
x_dos_distance = max(x_dos) - min(x_dos)
y_dos_distance = max(y_dos) - min(y_dos)
print(x_dos_distance*y_dos_distance)
