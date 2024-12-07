#코드 작성은 금방 끝나고 답도 맞췄지만 numbers 값이 동적이지 못하고 마음에 안듬
N = int(input())
numbers = list(range(2700000))
k = 666
result = []
for num in numbers:
    if "666" in str(num):
        result.append(num)
print(result[N-1])


#시간도 휠씬 빨라지고,범위도 유동적,확장성도 높아짐
def find_number(N,target):
    count = 0
    current = 0
    result = []
    while count < N:
        if target in str(current):
            count += 1
            result.append(current)
        current += 1

    return result[N-1]

N = int(input())
print(find_number(N,"666"))

