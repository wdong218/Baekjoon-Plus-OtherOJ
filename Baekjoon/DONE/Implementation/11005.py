N,B = map(int,input().split())
#55
k = []
while N > 0:
    remainder = N % B
    if remainder >= 10:  # 10 이상인 경우 문자로 변환 (예: 10 -> 'A')
        k.append(chr(remainder + 55))
    else:  # 10 미만은 그대로 숫자로 추가
        k.append(str(remainder))
    N = N // B

print(''.join(k[::-1]))