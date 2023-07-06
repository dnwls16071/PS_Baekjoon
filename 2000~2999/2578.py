# 빙고 게임은 다음과 같은 방식으로 이루어진다.
#
# 먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다
#
# 다음은 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.
#
# 차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.
#
# 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.
#
# 철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

# 빙고판에서 그어진 라인의 개수가 3개 이상이 되는 시점에서 "빙고"를 외친다.
def isBingo(arr):
    bingo_line = 0
    for i in arr:
        if i.count(1) == 5:
            bingo_line += 1

    for i in range(5):
        temp_height = 0
        for j in range(5):
            if arr[j][i] == 1:
                temp_height += 1
        if temp_height == 5:
            bingo_line += 1

    temp_diagonal1 = 0
    for i in range(5):
        if arr[i][i] == 1:
            temp_diagonal1 += 1
    if temp_diagonal1 == 5:
        bingo_line += 1

    temp_diagonal2 = 0
    for i in range(5):
        if arr[4-i][i] == 1:
            temp_diagonal2 += 1
    if temp_diagonal2 == 5:
        bingo_line += 1
    return bingo_line

# 5 * 5 사이즈의 2차원 배열 리스트를 선언해줌
bingo = [list(map(int, input().strip().split())) for _ in range(5)]

# 사회자가 부르는 빙고판 숫자의 순서를 1차월 배열 리스트로 만들기 위해 선언
# for i in range(5):
#     lst = list(map(int, input().strip().split()))
#     for num in lst:
#         line.append(num)
line1 = list(map(int, input().strip().split()))
line2 = list(map(int, input().strip().split()))
line3 = list(map(int, input().strip().split()))
line4 = list(map(int, input().strip().split()))
line5 = list(map(int, input().strip().split()))
line = line1 + line2 + line3 + line4 + line5

for Turn, num in enumerate(line):
    for t in bingo:
        if num in t:
            t[t.index(num)] = 1
            break

    result = isBingo(bingo)
    if result >= 3:
        print(Turn+1)
        sys.exit(0)