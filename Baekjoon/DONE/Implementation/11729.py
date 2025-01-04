k = int(input())

count = 2**k - 1


def hanoi(start,sub,goal, k):
    if k == 1:
        return [(start, goal)]
    second_moves = hanoi(start,goal,sub, k - 1)
    middle_move = [(start, goal)]
    third_moves = hanoi(sub,start,goal ,k - 1)

    return second_moves + middle_move + third_moves
print(count)
result = hanoi(1,2,3,k)
for i in range(len(result)):
    print(" ".join(map(str, result[i])))


