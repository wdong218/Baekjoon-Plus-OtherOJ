import sys
def find_num(sudoku_pan,x,y):
    num_list = set(range(1, 10))
    # 가로 체크
    row_nums = set(sudoku_pan[y])
    # 세로 체크
    col_nums = set(sudoku_pan[i][x] for i in range(9))
    # 3x3 박스 체크
    x_check = (x // 3) * 3
    y_check = (y // 3) * 3
    three_check_result = []
    for i in range(x_check, x_check + 3):  # 3x3 박스의 행 순회
        for j in range(y_check, y_check + 3):  # 3x3 박스의 열 순회
            three_check_result.append(sudoku_pan[j][i])
    # 사용 가능한 숫자 계산
    candidates = num_list - row_nums - col_nums - set(three_check_result)
    return list(candidates)

def backtrack(sudoku_pan):
    # 빈 칸 찾기
    for y in range(9):
        for x in range(9):
            if sudoku_pan[y][x] == 0:  # 빈 칸 발견
                candidates = find_num(sudoku_pan, x, y)
                if not candidates:  # 가능한 숫자가 없으면 실패
                    return False
                for num in candidates:  # 가능한 숫자 순회
                    sudoku_pan[y][x] = num  # 숫자 채움
                    if backtrack(sudoku_pan):  # 다음 단계 진행
                        return True
                    sudoku_pan[y][x] = 0  # 실패 시 복구
                return False  # 모든 숫자가 실패하면 종료
    return True

sudoku_pan = []
for i in range(9):
    k = list(map(int, sys.stdin.readline().rstrip().split()))
    sudoku_pan.append(k)
backtrack(sudoku_pan)
for i in range(9):
    print(" ".join(map(str,sudoku_pan[i])))