while True:
    try:
        print(input())
    except EOFError:
        break
#무한반복문을 사용하여 한 줄씩 입력받아 출력한다.

#만약 더이상 입력이 없다면 EOFError 예외처리로 무한반복문을 나오게 된다.

#EOFError : 'End of File Eorror'의 약자로 파일에서 더 이상 읽을 내용이 없거나 입력 값이 없을 때 발생하는 에러.