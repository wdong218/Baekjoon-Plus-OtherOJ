# n, b = input().split()
# result = 0
# b = int(b)
# length = len(n)
#
# for i in range(length):
#     char = n[i]
#
#     if '0' <= char <= '9':
#         value = ord(char) - ord('0')
#     else:
#         value = ord(char) - ord('A') + 10
#
#     result = result * b + value
#
# print(result)
 """내 처음 의도한 코드가 위쪽 코드인데 일단 숫자와 문자를 만나는 경우를 나눠서 계산한 뒤 마지막에 b와 함께 곱해준다
그러나 파이썬에서는 밑 처럼 아주 간단하게 10진수 문제를 해결 할 수 있었다.
int(n,b) 라는 함수는 진법 변환을 간단하게 해주는 함수로 n에는 변환하려는 숫자 문자열을 넣고 b에는 해당하는 진법을 지정해주면
코드 한줄로 진법이 10진법으로 바뀌어서 출력된다. 더 부끄러운 점은 내가 머리 써서 만든 코드보다 파이썬에 내장된 코드의 실행 시간이 더 빠르다는 사실..."""

n, b = input().split()
b = int(b)
result = int(n, b)
print(result)
