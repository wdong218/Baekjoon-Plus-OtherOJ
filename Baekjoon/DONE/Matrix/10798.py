a = [[] for _ in range(15)]
for i in range(5):
    elements = list(input().rstrip())
    for j in range(len(elements)):
        a[j].append(elements[j])
result = "".join("".join(column) for column in a) # 이중 join()을 사용하여 2차원 리스트 a의 모든 요소를 하나의 문자열로 합치는 방식
print(result)