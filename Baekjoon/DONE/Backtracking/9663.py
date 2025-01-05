"""제출 pypy3으로 해야됨 파이썬3으로 할시 시간 초과 진짜 짜증나네 이거 때문에 시간을 얼마나 쓴거야.........................."""

def is_ok(x, row, used_x, diagonal1, diagonal2):
    """
    현재 (x, row)에 퀸을 배치할 수 있는지 확인.
    used_x: x 좌표 사용 여부 추적
    diagonal1: 주요 대각선 (x - row) 사용 여부 추적
    diagonal2: 부대각선 (x + row) 사용 여부 추적
    """
    if x in used_x or (x - row) in diagonal1 or (x + row) in diagonal2:
        return False
    return True


def backtrack(used_x, diagonal1, diagonal2, n, row):
    if row == n:  # 모든 퀸을 배치한 경우
        return 1

    count = 0
    for x in range(n):
        if is_ok(x, row, used_x, diagonal1, diagonal2):
            # 현재 위치에 퀸 배치
            used_x.add(x)
            diagonal1.add(x - row)
            diagonal2.add(x + row)

            # 다음 행으로 이동
            count += backtrack(used_x, diagonal1, diagonal2, n, row + 1)

            # 퀸 제거 (백트래킹)
            used_x.remove(x)
            diagonal1.remove(x - row)
            diagonal2.remove(x + row)

    return count



n = int(input())
queen = []
used_x = set()
diagonal1 = set()
diagonal2 = set()
print(backtrack(used_x, diagonal1, diagonal2, n, 0))
