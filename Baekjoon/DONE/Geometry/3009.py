x_dos = [0] * 3
y_dos = [0] * 3
for i in range(3):
    x_dos[i],y_dos[i] = map(int,input().split())
x_unique_elements = [x for x in x_dos if x_dos.count(x) == 1]
y_unique_elements = [y for y in y_dos if y_dos.count(y) == 1]
print(x_unique_elements[0],y_unique_elements[0])