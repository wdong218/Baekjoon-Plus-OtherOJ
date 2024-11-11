#1316

k = int(input())
count = 0

for i in range(k):
    check = 0

    q = input()
    l = list(set(q)) #q 리스트 중복 제거
    for i in range(len(l)): #중복 제거된 리스트만큼 반복
        rest_list = list(filter(lambda x: q[x] == l[i], range(len(q)))) #이 함수가 중복된 인덱스를 가져와주는 함수 ex) happy 면 l[i] 즉 중복 제거된 리스트의 요소를 가져와 원래 배열에서 요소의 위치를 반환
        if len(rest_list) > 1: #만약 반환된 위치의 크기가 1보다 작다는건 그 요소가 하나뿐이라는 뜻이기에 비교안해도 그룹단어
            for j in range(len(rest_list)-1): #
                if rest_list[j+1] - rest_list[j] != 1: #[1,2,3] 이렇게 인덱스가 존재했을때 연속성 확인 후 연속하지 않을 경우 check에 1을 더한뒤 break
                    check += 1
                    break

    if check == 0: #for 문이 종료되고 check가 0이 아니라는건 문자열이 그룹 단어가 아니라는 뜻이기에 count += 1
        count += 1


print(count)
