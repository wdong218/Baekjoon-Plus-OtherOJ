import sys
c = int(input())
for _ in range(c):
    score = list(map(int,sys.stdin.readline().split()))
    sum_score = sum(score) - score[0]
    ave = sum_score/score[0]
    count = 0
    for i in range(1,score[0]+1):
        if score[i] > ave:
            count += 1
    print(str(round((count / score[0]) * 100, 3)) + "%")

