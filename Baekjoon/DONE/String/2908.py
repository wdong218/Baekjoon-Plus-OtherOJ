a, b = input().split()
# a와 b의 첫 번째와 마지막 문자를 교환
a = a[::-1]  # 문자열 뒤집기
b = b[::-1]
a,b = int(a),int(b)
if a > b:
    print(a)
else:
    print(b)