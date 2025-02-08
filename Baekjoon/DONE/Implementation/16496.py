import functools
import sys
def compare(x, y):
    # x+y 와 y+x 를 비교
    if x + y > y + x:
        return -1  # x를 앞에 두기
    elif x + y < y + x:
        return 1   # y를 앞에 두기
    else:
        return 0

n = int(sys.stdin.readline().strip())
num_list = sys.stdin.readline().split()

# 모든 수가 0인지 체크
if all(x == '0' for x in num_list):
    print(0)
else:
    # 커스텀 비교 함수로 정렬
    sorted_list = sorted(num_list, key=functools.cmp_to_key(compare))
    print("".join(sorted_list))
