import sys

# 입력
n, k = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))

# 전역 변수로 저장 횟수와 k번째 값을 추적
count = 0  # 저장 횟수
result = -1  # k번째 저장된 값


# 병합 정렬 함수
def merge_sort(a, p, r):
    if p < r:  # 배열의 크기가 1보다 클 때만 정렬
        q = (p + r) // 2  # 중간 지점 계산
        merge_sort(a, p, q)  # 전반부 정렬
        merge_sort(a, q + 1, r)  # 후반부 정렬
        merge(a, p, q, r)  # 병합


# 병합 함수
def merge(a, p, q, r):
    global count, result  # 전역 변수 사용
    temp = []  # 임시 배열
    i = p  # 전반부 시작 인덱스
    j = q + 1  # 후반부 시작 인덱스

    # 두 부분 배열 비교 및 병합
    while i <= q and j <= r:
        if a[i] <= a[j]:
            temp.append(a[i])
            count += 1  # 저장 횟수 증가
            if count == k:
                result = a[i]  # k번째 저장된 값 기록
            i += 1
        else:
            temp.append(a[j])
            count += 1  # 저장 횟수 증가
            if count == k:
                result = a[j]  # k번째 저장된 값 기록
            j += 1

    # 왼쪽 배열에 남은 요소 병합
    while i <= q:
        temp.append(a[i])
        count += 1  # 저장 횟수 증가
        if count == k:
            result = a[i]  # k번째 저장된 값 기록
        i += 1

    # 오른쪽 배열에 남은 요소 병합
    while j <= r:
        temp.append(a[j])
        count += 1  # 저장 횟수 증가
        if count == k:
            result = a[j]  # k번째 저장된 값 기록
        j += 1

    # 정렬된 결과를 원래 배열에 반영
    for t in range(len(temp)):
        a[p + t] = temp[t]


# 병합 정렬 실행
merge_sort(a, 0, n - 1)

# 결과 출력
print(result)  # k번째 저장된 값 출력