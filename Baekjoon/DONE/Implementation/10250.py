t = int(input())
for i in range(t):
    h, w, s = map(int, input().split())

    if s % h == 0:  # 방 번호가 층 수의 배수일 때
        floor = h  # 마지막 층
        room = s // h
    else:  # 일반적인 경우
        floor = s % h  # 층 번호 계산
        room = s // h + 1  # 호수 번호 계산

    # 호수 번호가 한 자릿수일 경우 앞에 0을 붙여 출력
    if room > 9:
        print(f"{floor}{room}")
    else:
        print(f"{floor}0{room}")