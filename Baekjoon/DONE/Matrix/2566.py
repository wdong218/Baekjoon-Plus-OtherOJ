a = []
result = list()
row_index = list()
col_index = 0
for i in range(9):
    elements = list(map(int, input().split()))
    a.append(elements)

for i in range(9):
    result.append(max(a[i]))
    row_index.append(a[i].index(result[i]))
col_index = result.index(max(result))
print(max(result))
print(col_index+1,row_index[col_index]+1)